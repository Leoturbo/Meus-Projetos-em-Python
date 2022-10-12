from flask import Flask, render_template
import requests
import json


app=Flask(__name__,template_folder='templates')



def buscar_dados():
	r = requests.get('https://meme-api.herokuapp.com/gimme')
	my_data = json.loads(r.content)
	api_data = my_data["preview"][-2]
	add = my_data["subreddit"]



@app.route("/")
def index():
	_api, _add = buscar_dados()
	return render_template ('meme_index.html',meme_pic=_api,subreddit=_add)


if __name__=="__main__":
	app.run(debug=True)