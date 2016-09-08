from flask import Flask, render_template, request
import os
from yelp_api import find_bars
from google_maps import get_map
from flask_googlemaps import GoogleMaps
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

# initialize Google maps with API key
GoogleMaps(app, key=os.environ['GOOGLE_MAPS'])

@app.route("/")
def index():
	# get user submitted address from URL
	address = request.values.get('address')

	# find bars based on address
	bars = []
	if address:
		bars = find_bars(address)

	# get map based on bars
	if bars: 
		mymap = get_map(bars)
		return render_template('index.html', bars=bars, mymap=mymap)
	else:
		return render_template('index.html', bars=bars, mymap=None)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)