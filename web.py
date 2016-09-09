from flask import Flask, render_template, request, redirect, session
from find_bars import find_bars
from get_map import get_map
from flask_googlemaps import GoogleMaps
from dotenv import load_dotenv, find_dotenv
from send_text import send_text 
import os
import random
import string
load_dotenv(find_dotenv())

app = Flask(__name__)

app.secret_key = os.urandom(24)

# initialize Google maps with API key
GoogleMaps(app, key=os.environ['GOOGLE_MAPS'])

@app.route("/")
def index():
	# generate random code
	code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

	return render_template('index.html', code=code)

@app.route("/verify")
def verify():
	# get user submitted address from URL
	number = request.values.get('number')
	session['number'] = number
	code = request.values.get('code')
	verify = request.values.get('verify')

	print(number)
	print(code)
	print(verify)

	if verify == '':
		# send code to user in a text
		verified = send_text(code, "+1{}".format(number))
		return render_template('verify.html', number=number, code=code, verify=verify)
	else:
		print(code == verify)
		if code == verify:
			return redirect('search')
		else:
			return render_template('verify.html', number=number, code=code, verify=verify)


@app.route("/search")
def search():
	address = request.values.get('address')
	number = session['number']

	print(number)

	# find bars based on address
	bars = []
	if address:
		bars = find_bars(address)

	# get map based on bars
	if bars: 
		mymap = get_map(bars)

		for bar in bars:
			send_text(
				'{} is located at {}. Contact them at {}'.format(
					bar['name'], bar['location'], bar['phone']
				), 
				"+1{}".format(number)
			)

		return render_template('search.html', bars=bars, mymap=mymap)
	else:
		return render_template('search.html', bars=None, mymap=None)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)