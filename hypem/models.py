import logging
import requests

class HypemModel(object):
    def api_endpoint(self):
        raise NotImplementedError

class HypemTrack(HypemModel):
    _attributes = ["mediaid","artist","title","dateposted","siteid","sitename",
                   "posturl","postid","loved_count","posted_count","thumb_url",
                   "thumb_url_medium","thumb_url_large","thumb_url_artist","time",
                   "description","itunes_link"]
    def __init__(self,**kwargs):
        for attr in self._attributes:
            setattr(self,attr,kwargs.get(attr))

class HypemPlaylist(HypemModel):
    _playlist_data = None

    def __init__(self,
                 type="popular",
                 filter="3day",
                 page=1):
        self.type=type
        self.filter = filter
        self.page = page

    @property
    def endpoint(self):
        return "http://hypem.com/playlist/%(type)s/%(filter)s/json/%(page)s/data.js" % \
            {
                'type':self.type,
                'filter':self.filter,
                'page':self.page
            }

    def _parse_raw_data(self,raw_data):
        parsed_result = []
        del raw_data['version'] #hack because i dont agree with this design decision by hypem

        for rank,track_data in sorted(raw_data.items(),key=lambda x: int(x[0])):
            parsed_result.append(HypemTrack(**track_data))

        return parsed_result

    @property
    def _playlist(self):
        if not self._playlist_data:
            playlist_data_raw = requests.get(self.endpoint).json()
            self._playlist_data = self._parse_raw_data(playlist_data_raw)

        return self._playlist_data

    def __str__(self):
        return "PLAYLIST - %s - %s - %s" % (self.type,self.filter,self.page)

    def __iter__(self):
        for track in self._playlist:
            yield track

    def __getitem__(self,key):
        return self._playlist[key]

    def __len__(self):
        return len(self._playlist)
            
        



    

