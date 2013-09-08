import logging
import requests

class HypemModel(object):
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
            self._data = self._parse_raw_data(requests.get(self.endpoint).json())
        return self._data

class HypemUser(HypemModel):    
    def __init__(self,username,_data=None):
        self.username = username
        self._data = _data

    @property
    def endpoint(self):
        return "http://api.hypem.com/api/get_profile?username=%(username)s" % {'username':self.username}

    def _parse_raw_data(self,raw_data):
        return raw_data


class HypemTrack(HypemModel):
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

    @property
    def data(self):
        if not self._data:
            playlist_data_raw = requests.get(self.endpoint).json()
            self._data = self._parse_raw_data(playlist_data_raw)

        return self._data

    def __iter__(self):
        for track in self._data:
            yield track

    def __getitem__(self,key):
        return self._data[key]

    def __len__(self):
        return len(self._data)
            
        



    

