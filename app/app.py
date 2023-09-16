from flask import Flask
from .api import routes as api_routes


def create_app(config: str):
    app = Flask(__name__,
                template_folder='./templates',
                static_folder='./static',
                static_url_path='')
    app.config.from_pyfile(config)
    app.register_blueprint(api_routes, url_prefix='/api')
    return app
