from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def index():
	bar = request.values.get('bar')
	print(bar)
	return render_template('index.html', bar=bar)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)