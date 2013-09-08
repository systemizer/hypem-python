import logging
import urllib2
import json

class HypemModel(object):
    _attributes = []
    _data = None

    @property
    def endpoint(self):
        raise NotImplementedError

    @property
    def _parse_raw_data(self):
        raise NotImplementedError

    @property
    def data(self):
        if not self._data:
            self._data = self._parse_raw_data(json.loads(urllib2.urlopen(self.endpoint).read()))
        return self._data

    def __getattr__(self,name):
        if name in self._attributes:
            return self.data[name]
        return super(HypemModel,self).__getattr__(name)

class HypemUser(HypemModel):    
    _attributes = ["username","profile_url","fullname","twitter_username",
                   "userpic","joined_ts","favorites_count","location"]
    def __init__(self,username,_data=None):
        self.username = username
        self._data = _data

    @property
    def endpoint(self):
        return "http://api.hypem.com/api/get_profile?username=%(username)s" % {'username':self.username}

    def _parse_raw_data(self,raw_data):
        return raw_data


class HypemTrack(HypemModel):
    _attributes = ["mediaid","artist","title","dateposted","siteid","sitename",
                   "posturl","postid","loved_count","posted_count","thumb_url",
                   "thumb_url_medium","thumb_url_large","thumb_url_artist","time",
                   "description","itunes_line"]

    def __init__(self,mediaid,_data=None):
        self.mediaid = mediaid
        if _data:
            self._data = _data

    @property
    def endpoint(self):
        return 

class HypemPlaylist(HypemModel):

    def __init__(self,type,filter,page=1,_data=None):
        self.type=type
        self.filter = filter
        self.page = page
        self._data = _data

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
            parsed_result.append(HypemTrack(mediaid=track_data['mediaid'],_data=track_data))

        return parsed_result

    def __iter__(self):
        for track in self.data:
            yield track

    def __getitem__(self,key):
        return self.data[key]

    def __len__(self):
        return len(self.data)
            
        



    

