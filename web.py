from flask import Flask, render_template, request
import os
from find_bars import find_bars
from get_map import get_map
from flask_googlemaps import GoogleMaps
import os
from dotenv import load_dotenv, find_dotenv
import random
import string
from send_text import send_text 
load_dotenv(find_dotenv())

app = Flask(__name__)

# initialize Google maps with API key
GoogleMaps(app, key=os.environ['GOOGLE_MAPS'])

@app.route("/")
def index():
	# get user submitted address from URL
	address = request.values.get('address')

	# generate random code
	code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

	# find bars based on address
	bars = []
	if address:
		bars = find_bars(address)

	# get map based on bars
	if bars: 
		mymap = get_map(bars)
		return render_template('index.html', bars=bars, mymap=mymap, address=address)
	else:
		return render_template('index.html', bars=bars, mymap=None, code=code)

@app.route("/verify")
def verify():
	# get user submitted address from URL
	number = request.values.get('number')
	code = request.values.get('code')

	print(number)
	print(code)
	# send code to user in a text
	verified = send_text(code, "+1{}".format(number))

	return render_template('verify.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)