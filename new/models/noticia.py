from flask import Flask, render_template
import request
from newsapi import NewsApiClient
import json
import api_key

app = Flask(__name__)


doc = {
"status": "ok",
"totalResults": 10,
-"articles": [
-{
-"source": {
"id": "techcrunch",
"name": "TechCrunch"
},
"author": "Rebecca Szkutak",
"title": "How a pivot helped HopSkipDrive emerge successful in a sector where many failed",
"description": "Working with school districts has allowed HopSkipDrive to flourish in the children's transportation market.",
"url": "https://techcrunch.com/2022/09/23/how-a-pivot-helped-hopskipdrive-emerge-successful-in-a-sector-where-many-failed/",
"urlToImage": "https://techcrunch.com/wp-content/uploads/2022/09/CareDriver-and-Rider.jpg?resize=1200,800",
"publishedAt": "2022-09-23T19:01:30Z",
"content": "Joanna McFarland got the idea for HopSkipDrive in 2014 because she needed a solution to a problem that many working parents like herself face: How do you consistently get your kids where they need to… [+1215 chars]"
}
]
}





def new_api():
    # Init
    newsapi = NewsApiClient(api_key)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                              sources='bbc-news,the-verge',
                                              category='business',
                                              language='en',
                                              country='us')

    # /v2/everything
    all_articles = newsapi.get_everything(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2017-12-01',
                                          to='2017-12-12',
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)

     # /v2/top-headlines/sources
    sources = newsapi.get_sources()


@app.route("/")
def index():
  meme_pic = new_api()
  return render_template("index.html", meme_pic=meme_pic)



if __name__=="__main__":
  app.run(debug=True)