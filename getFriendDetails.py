#takes in a playlist url as input

import sys
import spotipy
import spotipy.util as util
import json
from urlparse import urlparse

def get_image(userid):

    sp = spotipy.Spotify()
    sp.trace = True
    user = sp.user(userid)
    return (user['images'][0]['url'])

scope = 'playlist-modify-public'

if len(sys.argv) > 1:
    URL = sys.argv[1]

else:
    print("Usage: %s playlist url " % (sys.argv[0],))
    sys.exit()

temp = urlparse(URL)
temp = temp.path
temp = temp.split('/')

#userid and playlistid stored as strings
userid = temp[2]
playlistid = temp[4]

#get user image
user_image = get_image(userid)

#get name of playlist

#return (user_image, namePlaylist)

