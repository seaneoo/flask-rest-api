from flask import Flask, render_template
from .api import routes as api_routes

app = Flask(__name__)
app.register_blueprint(api_routes, url_prefix='/api')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def errorhandler_404(error):
    return render_template('404.html', error=error), 404
