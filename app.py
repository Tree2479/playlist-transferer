from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

app = Flask(__name__)

playlist_uri = '503usGZp5YHvy1FuEmxdG7'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0727f52c40f84a72900e7e75522291df",
                                               client_secret="9a0761b8368943a88f28366c25928e95",
                                               redirect_uri="http://127.0.0.1:5000/redirect",
                                               scope="playlist-read-private"))

spotify_access_token_request_url = 'https://accounts.spotify.com/api/token'

payload = {
    "Content-Type: application/x-www-form-urlencoded"
    "grant_type=client_credentials&client_id=0727f52c40f84a72900e7e75522291df&client_secret=9a0761b8368943a88f28366c25928e95"
}

access_token = requests.post(spotify_access_token_request_url, payload)
print(access_token)

@app.route("/")
def spotify_get():
    access_token = requests.post(spotify_access_token_request_url, json=payload)
    #results = sp.playlist(playlist_uri, fields="name,tracks.items(track(name,artists(name)))", additional_types=('track',))
    #print('test')
    #print(results)
    return render_template("index.html", title='hi')

@app.route("/redirect")
def redirect_page():
    return render_template("redirect.html")

if __name__ == '__main__': 
    app.run(debug = True, use_reloader=False) # Runs the application with ssl enabled in order to use https


