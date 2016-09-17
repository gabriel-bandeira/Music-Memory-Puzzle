import pprint
import sys

import spotipy
import spotipy.util as util
#import simplejson as json
#from artistTopTracks import getImages
import artistTopTracks as atop

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #ranges = ['short_term', 'medium_term', 'long_term']
    ranges = ['short_term']
    for range in ranges:
        print "range:", range
        results = sp.current_user_top_artists(time_range=range, limit=5)
        for i, item in enumerate(results['items']):
            print i, item['name']
        print
else:
    print("Can't get token for", username)

atop.getImages(sp, 'red hot')
print ""
print ""
atop.getSamples(sp, 'red hot')
