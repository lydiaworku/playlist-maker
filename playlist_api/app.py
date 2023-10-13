from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import date
from random import randint
import random


app = Flask(__name__, template_folder='templates')
CORS(app)


CLIENT_ID = "523af5a59f764c14971ce95056ea5ea6"
CLIENT_SECRET = "520e80e828dd491cb0721e1c40095852"
REDIRECT_URI = "http://127.0.0.1:5000/playlist"

token_url = 'https://accounts.spotify.com/api/token'


headers = {'Content-Type': 'application/x-www-form-urlencoded'}


username = "lydiaw2882"




sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public user-top-read user-library-read"))

@app.route('/login')
def login():
    return redirect(f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=user-read-private user-read-email")


@app.route('/callback')
def callback():
    AUTH_CODE = request.args.get('code')

    response = requests.post(

    token_url,
        data={
            'grant_type': 'authorization_code',
            'code': AUTH_CODE,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
    )


    response = requests.post(token_url, headers=headers, data=data)

    token_data = response.json()

    global access_token, refresh_token

    access_token = token_data['access_token']
    refresh_token = token_data['refresh_token']


    data = response.json()

    return jsonify({'access_token': data.get('access_token')})



def current_month():
    today = date.today()
    number_month = today.month
    year = str(today.year)
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}
    month = months.get(number_month)
    month_year = month + " " + year
    return month_year + " playlist"


    
class SongPicker:

    def __init__(self):
        self.saved_list = []
        self.short_list = []
        self.medium_list = []
        self.long_list = []
        self.top_list = []

    def saved_songs(self):
        saved = sp.current_user_saved_tracks(limit=50)
        random_saved_nums = []
        for item in range(23):
            num = randint(0, 49)
            if num not in random_saved_nums:
                random_saved_nums.append(num)
        #print(' ')
        #print('SAVED')
        #print(' ')
        #print(random_saved_nums)
        for item in random_saved_nums:
            self.saved_list.append(saved['items'][item]['track']['uri'])
        #print(self.saved_list)


    def top_songs(self):

        short_top = sp.current_user_top_tracks(limit=50, time_range='short_term')
        short_nums = []
        for item in range(27):
            num = randint(0, 49)
            if num not in short_nums:
                short_nums.append(num)
        #print(' ')
        #print('SHORT')
        #print(' ')
        #print(short_nums)
        for item in short_nums:
            if short_top['items'][item]['uri'] not in self.saved_list:
                self.short_list.append(short_top['items'][item]['uri'])
        #print(self.short_list)


        medium_top = sp.current_user_top_tracks(limit=50, time_range='medium_term')
        medium_nums = []
        for item in range(6):
            num = randint(0, 39)
            if num not in medium_nums:
                medium_nums.append(num)
        #print(' ')
        #print('MEDIUM')
        #print(' ')
        #print(medium_nums)
        for item in medium_nums:
            if medium_top['items'][item]['uri'] not in self.saved_list and medium_top['items'][item]['uri'] not in self.short_list:
                self.medium_list.append(medium_top['items'][item]['uri'])
        #print(self.medium_list)


        long_top = sp.current_user_top_tracks(limit=50, time_range='long_term')
        long_nums = []
        for item in range(2):
            num = randint(0, 24)
            if num not in long_nums:
                long_nums.append(num)
        #print(' ')
        #print('LONG')
        #print(' ')
        #print(long_nums)
        for item in long_nums:
            if long_top['items'][item]['uri'] not in self.saved_list and long_top['items'][item]['uri'] not in self.short_list and long_top['items'][item]['name'] not in self.medium_list:
                self.long_list.append(long_top['items'][item]['uri'])
        #print(self.long_list)


        for item in self.saved_list:
            self.top_list.append(item)

        for item in self.short_list:
            self.top_list.append(item)

        for item in self.medium_list:
            self.top_list.append(item)
            
        for item in self.long_list:
            self.top_list.append(item)



        #print(' ')
        #print('TOP LIST')
        #print(str(len(self.top_list)) + ' songs')
        #print(' ')
        #print(self.top_list)
        global playlist_length
        playlist_length = len(self.top_list)
        global global_top_list
        global_top_list = []
        for item in self.top_list:
            global_top_list.append(item)
        return self.top_list
    
            


def new_playlist(name):
    playlist = sp.user_playlist_create(sp.user(username)["id"], name, public=True)
    return playlist


def add_songs(playlist_id, track_uris):
    sp.user_playlist_add_tracks(sp.user(username)["id"], playlist_id, track_uris)
    return playlist_id

def delete_songs(playlist_id, items):
    sp.user_playlist_remove_specific_occurrences_of_tracks(sp.user(username)["id"], playlist_id, items)

def reorder_songs(playlist_id, range_start, insert_before):
    sp.user_playlist_reorder_tracks(sp.user(username)["id"], playlist_id, range_start, insert_before)
    return ("hello" + playlist_id)

def shuffle_songs(playlist_id, items):
    results = sp.playlist_tracks(playlist_id)
    items = results['items']
    random.shuffle(items)
    sp.user_playlist_replace_tracks(sp.user(username)["id"], playlist_id, [item['track']['uri'] for item in items])



@app.route('/playlist', methods=['GET']) 
def main():

    playlist_name = current_month()

    playlist = new_playlist(playlist_name)

    songs = SongPicker()
    
    songs.saved_songs()
    
    add_songs(playlist["id"], [item for item in songs.top_songs()])

    
    shuffle_songs(playlist["id"], global_top_list)

    #reorder_songs(playlist["id"], playlist_length - 1, 0)

    name='playlist maker'

    link = "https://open.spotify.com/playlist/" + playlist["id"]

    print(link)

    #print("Access Token:", access_token)
    #print("Refresh Token:", refresh_token)

    print(sp.user(username)["id"])
    print(sp.current_user()["id"])
    print('LENGTH: ')
    print(playlist_length)

    return render_template('index.html', name=name, link=link)


    

if __name__ == "__main__":


    app.run()


