from flask import Flask, render_template, request, redirect
import requests
import json

# importing the spotipy library and spotipy credentials
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

app = Flask(__name__)

# setting route
@app.route('/')
def index():
  # connect to the spotipy API
  sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="117b49902060434fb6640e9332867736",
                                                             client_secret="27eb9a6630c54fecb484f12876eb6ce6"))
  # set parameters
  artist = 'Coldplay'
  number_of_tracks = 10

  # pass into the spotify search
  results = sp.search(q=artist, limit=number_of_tracks)

  # create variable to pass to html template
  tracks = []

  # loop over the items in the search result (accessed by results['tracks']['items'])
  # results is a python dictionary type object
  for track in results['tracks']['items']:
      # append track name to a list
      tracks.append(track['name'])

  # render the index.html template along with the variables
  return render_template('index.html', num_tracks=number_of_tracks, tracks=tracks, artist=artist)
