from .models import (HypemPlaylist,
                     HypemUser)

def get_popular(filter="3day",page=1):
    return HypemPlaylist("popular",
                         filter,
                         page=page)

def get_latest(filter="all",page=1):
    return HypemPlaylist("latest",
                         filter,
                         page=page)

def get_artist(artist_name,page=1):
    return HypemPlaylist(type="artist",
                         filter=artist_name,
                         page=page)

def get_favorites(username,page=1):
    return HypemPlaylist(type="loved",
                         filter=username,
                         page=page)

def get_listening_history(username,page=1):
    return HypemPlaylist(type="history",
                         filter=username,
                         page=page)

def get_obsessed(username,page=1):
    return HypemPlaylist(type="obsessed",
                         filter=username,
                         page=page)
                         
def get_user(username):
    return HypemUser(username)

def search(query,page=1):
    return HypemPlaylist(type="search",
                         filter=query,
                         page=page)
    
