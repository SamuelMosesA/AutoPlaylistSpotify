import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

cl_id = "93aa3ecce4404e418c4148ff724f02ca"
cl_secret_id = "e0730d4395e4459c9c09dcb660eb6d37"
# userid = '314d3ezdac6rkng2gbrrf6s7qcea'

webbrowser.register('chromium', None)

scopes = 'playlist-modify-public playlist-modify-private user-library-read'

# Getting username from terminal

if len(sys.argv) > 1:
    username = sys.argv[1]

try:
    token = util.prompt_for_user_token(
        username, client_id=cl_id, client_secret=cl_secret_id, redirect_uri="http://google.com/", scope=scopes)
except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)

# spotify object

spotifyObject = spotipy.Spotify(auth=token)

currUser = spotifyObject.current_user()
# print(json.dumps(currUser, sort_keys=True, indent=4))

# saved_tracks = spotifyObject.current_user_saved_tracks(1)
# track_name = saved_tracks['track']['name']
# added_at = saved_tracks['added_at']
# artist_name = saved_tracks['track']['artists'][0]['name']
# artist_id = saved_tracks['track']['artists'][0]['id']
# artist_data = spotifyObject.artist(artist_id)
# genres = artist_data['genres']
# print(f'{ track_name}\n {added_at}\n {artist_name}\n {artist_id}\n {genres}')

# print(json.dumps(Variable, sort_keys=True, indent =4))
genres_list = ['indian classical', 'neo-classical', 'indian folk', 'world folk', 'world fusion',
               'hindustani classical', 'indian jazz', 'indian rock', 'sitar', 'sufi', 'indian indie',
               'bansuri', 'afropop', 'arab folk']
# getting all the new liked songs
# print(json.dumps(saved_tracks, sort_keys=True, indent =4))
tracks_uris = []

for of in range(19):
    saved_tracks = spotifyObject.current_user_saved_tracks(50, 50 * of)

    for track in saved_tracks['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        added_at = track['added_at']
        artist_id = track['track']['artists'][0]['id']
        artist_data = spotifyObject.artist(artist_id)
        genres = artist_data['genres']

        if set(genres) & set(genres_list):
            tracks_uris.append(track['track']['uri'])
            print(f'\n {track_name}\n {artist_name}\n {added_at}\n {genres}\n')

playlist_id = '6fS9KlKycuyyPBEZIpyyL0'

with open('song.json', 'w') as json_write:
    json.dump(tracks_uris, json_write, indent=4)

spotifyObject.trace = False

result = spotifyObject.user_playlist_add_tracks(
    username, playlist_id, tracks_uris)

print(result)
