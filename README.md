hypem-python
============

Simple Python Client to the Hype Machine Public API (http://hypem.com)

Example:
'''
import hypme
playlist = hypem.get_popular()
for track in playlist:
  print track.title
  
'''


Available Functions:

get_popular(filter,page)
  filter options (default:'3day') - '3day','lastweek','noremix','artists','twitter'
  page (default:1) - page offset of results
  
get_latest(filter,page)
  filter options (default:'all') - 'all','fresh','noremix','remix'
  page (default:1) - page offset of results
  
get_latest(filter,page)
  filter options (default:'all') - 'all','fresh','noremix','remix'
  page (default:1) - page offset of results
  
get_artist(artist_name,page)

get_favorites(username,page)

get_listening_history(username,page)

get_obsessed(username,page)

get_user(username)

search(query,page)
