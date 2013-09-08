hypem-python
============

Simple Python Client to the Hype Machine Public API (http://hypem.com)

Example:

```python
import hypem
playlist = hypem.get_popular()
for track in playlist:
  print track.title
  
```


Available Functions:
--------------------

**hypem.get_popular**(filter,page)
  filter options (default:'3day') - '3day','lastweek','noremix','artists','twitter'
  page (default:1) - page offset of results
  
**hypem.get_latest**(filter,page)
  filter options (default:'all') - 'all','fresh','noremix','remix'
  page (default:1) - page offset of results
  
**hypem.get_latest**(filter,page)
  filter options (default:'all') - 'all','fresh','noremix','remix'
  page (default:1) - page offset of results
  
**hypem.get_artist**(artist_name,page)

**hypem.get_favorites**(username,page)

**hypem.get_listening_history**(username,page)

**hypem.get_obsessed**(username,page)

**hypem.get_user**(username)

**hypem.search**(query,page)
