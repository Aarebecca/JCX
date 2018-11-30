from app import utils
from flask import jsonify, make_response, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    s = utils.SQL()
    sql = "select * from account"
    return jsonify({"status": "ok", "data": s.query(sql)})


@main.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)