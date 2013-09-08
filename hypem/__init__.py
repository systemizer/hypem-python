from .models import HypemPlaylist

def get_popular(filter="3day",page=1):
    return HypemPlaylist("popular",
                         filter,
                         page)

def get_latest(filter="all",page=1):
    return HypemPlaylist("latest",
                         filter,
                         page)
