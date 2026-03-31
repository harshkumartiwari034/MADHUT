from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Database.T_shirt.t_shirtDb import TshirtDatabase
from ..extensions import cache

blp = Blueprint('tshirt', __name__)


@blp.route('/user/tshirts')
class FetchTshirt(MethodView):
    def __init__(self):
        self.tshirt_db = TshirtDatabase()

    @cache.cached(timeout=60,query_string=True)
    def get(self):
        last_id = request.args.get('last_id')
        limit = int(request.args.get('limit', 20))
        if last_id:
            return jsonify(self.tshirt_db.fetch_products(last_id, limit))

        return jsonify(self.tshirt_db.fetch_products(None, limit))
