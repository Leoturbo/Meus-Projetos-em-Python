from flask import Flask, render_template
from newsapi import NewsApiClient
from config import API_KEY, endpoint, country
import json

app = Flask(__name__)


def services(category='general'):
  new_api = NewsApiClient(API_KEY)
  articles = new_api.get_top_headlines(endpoint, country='br')


  result = json.loads(str(articles['sources']))
  articles = None

  return result.articles




@app.route("/")
def index():
  meme_pic = services()
  return render_template("index.html", meme_pic=meme_pic)



if __name__=="__main__":
  app.run(debug=True)