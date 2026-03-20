from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..Database.T_shirt.t_shirtDb import TshirtDatabase
from ..extensions import cache

blp = Blueprint('user seen recent product', __name__)


@blp.route('/new/arrival/t-shirt')
class GetRecentProduct(MethodView):
    def __init__(self):
        self.recent_product = TshirtDatabase()

    @cache.cached(timeout=120, query_string=True)
    def get(self):
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 15))
        result = self.recent_product.fetch_new_arrival(page, limit)
        return jsonify(result)
