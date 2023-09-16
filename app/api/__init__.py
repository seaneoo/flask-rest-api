from flask import Blueprint
from ..database import col
from bson import json_util
import json

routes = Blueprint('api', __name__)


@routes.route('/', methods=['get'])
def api_root():
    cur = col.find({})
    data = list(cur.sort('release_date', 1))
    return {'data': json.loads(json_util.dumps(data))}
