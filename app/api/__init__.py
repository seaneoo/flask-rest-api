from flask import Blueprint

routes = Blueprint('api', __name__)


@routes.route('/')
def api_root():
    return {'hello': 'world'}
