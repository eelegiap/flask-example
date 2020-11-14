from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
  # setting parameters
  parameters = {
    'q' : 'pet adoption',
  }
  # getting the request
  response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?&api-key=oPZX74EhH9FsxNEaWqAfRi7SZ5FAsGL0", params=parameters)

  return render_template('index.html', response=response.json())


@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run(port=33507)
