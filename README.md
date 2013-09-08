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


Models:
------

###HypemTrack
*	*mediaid* - "1yy5b"
*	*artist* - "Wild Child"
*	*title* - "Crazy Bird"
*	*dateposted* - 1378404070
*	*siteid* - 1497
*	*sitename* - "Covert Curiosity"
*	*posturl* - "http://covertcuriosity.blogspot.com/2013/09/wild-child-crazy-bird.html"
*	*postid* - 2292677
*	*loved_count* - 2897
*	*posted_count* - 8
*	*thumb_url* - "http://static.hypem.net/thumbs_new/c5/2292677.jpg"
*	*thumb_url_medium* - "http://static.hypem.net/thumbs_new/df/2294751_120.jpg"
*	*thumb_url_large* - "http://static.hypem.net/thumbs_new/df/2294751_320.jpg"
*	*thumb_url_artist* - null
*	*time* - 238
*	*description* - "Here's a catchy new song from Wild Child called \"Crazy Bird\". This comes from Wild Child's upcoming album The Runaround, which will be released on October 8th via Ben Kweller's new label, Noise Company. Kweller contacted the band upon first hearing Pillow"	
*	*itunes_link* - "http://hypem.com/go/itunes_search/Wild%20Child"

###HypemUser
*	*username* - "systemizer"
*	*profile_url*: "http://hypem.com/systemizer",
*	*fullname*: "Rob McQueen",
*	*twitter_username*: "systemizer",
*	*userpic*: "http://static.hypem.net/images/bg-album-art.gif",
*	*joined_ts*: 1317063850,
*	*favorites_count*: {"user": 0,"item":106,"site":0,"query":0,"followers":0}
*	*location*: "San Francisco, CA, US",
*	*is_friend*: false,
*	*is_follower*: false
