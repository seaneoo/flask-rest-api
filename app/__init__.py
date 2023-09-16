from flask import render_template
from .database import DatabaseManager
from .app import create_app

app = create_app(config='config.py')
db_manager = DatabaseManager().connect()


@app.teardown_appcontext
def teardown(error):
    if not db_manager.client:
        db_manager.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def errorhandler_404(error):
    return render_template('404.html', error=error), 404
