from flask import Flask, render_template, request
import os
from yelp_api import find_bars
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	bars = []
	if address:
		bars = find_bars(address)
		print(bars)
	return render_template('index.html', bars=bars)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)