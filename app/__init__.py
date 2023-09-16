from flask import Flask, render_template
from .api import routes as api_routes
from .database import close
import atexit

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static',
            static_url_path='')

app.config.from_pyfile('config.py')

app.register_blueprint(api_routes, url_prefix='/api')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def errorhandler_404(error):
    return render_template('404.html', error=error), 404


atexit.register(lambda: close())
