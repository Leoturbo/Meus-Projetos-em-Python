from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
	r = requests.get('https://api.github.com/events')
	my_data = json.loads(r.text)
	api = my_data[0]
	return render_template ('index.html',meme_pic=my_data)

if __name__ == '__main__':
	app.run(debug=True)
