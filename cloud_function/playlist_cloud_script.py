import spotipy
import spotipy.util as util
from datetime import datetime
from info import *


def conv_time(t):
    return datetime.strptime(t, '%Y-%m-%dT%H:%M:%SZ')


# 2020-03-19T07:33:43Z
class Track:
    def __init__(self, usr, client_id, client_secret, redirect_url):
        self.username = usr
        self.scope = 'playlist-modify-public playlist-modify-private user-library-read'
        self.token = util.prompt_for_user_token(self.username, client_id=client_id,
                                                client_secret=client_secret, redirect_uri=redirect_url,
                                                scope=self.scope)

        if self.token:
            self.spotifyObject = spotipy.Spotify(auth=self.token)
            self.spotifyObject.trace = False

        self.min_time = conv_time('2020-03-22T18:48:39Z')
        try:
            with open('time.txt', 'r') as timeread:
                self.min_time = conv_time(timeread.read())
                print(self.min_time)
        except FileNotFoundError:
            pass

        package = self.spotifyObject.current_user_saved_tracks(30)
        self.tracks = package['items']

        with open('time.txt', 'w') as timewrite:
            timewrite.write(self.tracks[0]['added_at'])

        self.hiphop_track_uris = []
        self.ambstudy_track_uris = []
        self.rock_track_uris = []
        self.scottish_track_uris = []
        self.carnatic_track_uris = []
        self.ccm_track_uris = []
        # self.instrumental_track_uris = []

    def remove_old(self):
        for element in self.tracks:
            print(element['added_at'])
            print(element['track']['name'])
            if conv_time(element['added_at']) <= self.min_time:
                ind = self.tracks.index(element)
                self.tracks = self.tracks[:ind]
                break

    # def instrumental(self,item):
    #     item

    def playlister(self):
        for song in self.tracks:
            artist_id = song['track']['artists'][0]['id']
            artist_data = self.spotifyObject.artist(artist_id)
            genres = Genre(artist_data['genres'])

            if not artist_data['genres']:
                self.ambstudy_track_uris.append(song['track']['uri'])
                continue

            if genres == c_rap_genres:
                self.hiphop_track_uris.append(song['track']['uri'])
            if genres == c_rock_genres:
                self.rock_track_uris.append(song['track']['uri'])
            if genres == ccm_genres:
                self.ccm_track_uris.append(song['track']['uri'])
            elif genres == scottish_folk_genres:
                self.scottish_track_uris.append(song['track']['uri'])
            elif genres == carnatic_fusion_genres:
                self.carnatic_track_uris.append(song['track']['uri'])
            elif genres == ambient_study_genres:
                self.ambstudy_track_uris.append(song['track']['uri'])
            # if self.instrumental(song):
            #     self.instrumental_track_uris.append(song['track']['uri'])

    def pusher(self):
        if self.hiphop_track_uris:
            self.spotifyObject.user_playlist_add_tracks(
                self.username, rap_playlist_id, self.hiphop_track_uris)
        if self.rock_track_uris:
            self.spotifyObject.user_playlist_add_tracks(
                self.username, rock_playlist_id, self.rock_track_uris)
        if self.carnatic_track_uris:
            self.spotifyObject.user_playlist_add_tracks(
                self.username, carnatic_playlist_id, self.carnatic_track_uris)
        if self.scottish_track_uris:
            self.spotifyObject.user_playlist_add_tracks(
                self.username, scottish_playlist_id, self.scottish_track_uris)
        if self.ccm_track_uris:
            print(self.ccm_track_uris)
            self.spotifyObject.user_playlist_add_tracks(
                self.username, ccm_playlist_id, self.ccm_track_uris)
        if self.ambstudy_track_uris:
            self.spotifyObject.user_playlist_add_tracks(
                self.username, ambient_playlist_id, self.ambstudy_track_uris)


def run():
    task = Track('314d3ezdac6rkng2gbrrf6s7qcea', '93aa3ecce4404e418c4148ff724f02ca',
                 'e0730d4395e4459c9c09dcb660eb6d37', 'https://google.com/')
    task.remove_old()
    task.playlister()
    task.pusher()
    print("run")
