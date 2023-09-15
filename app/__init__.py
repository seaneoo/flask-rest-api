from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.errorhandler(404)
def errorhandler_404(error):
    return render_template('404.html', error=error), 404
