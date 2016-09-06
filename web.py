from flask import Flask, render_template, request
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
    app.run()