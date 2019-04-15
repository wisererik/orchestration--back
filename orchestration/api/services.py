from flask import jsonify
from flask import Blueprint
# from flask import request

service = Blueprint("service", __name__)


@service.route("/v1/orchestration/services/<string:id>", methods=['GET'])
def get_service(id):
    return jsonify(id=id, name="Hello World!"), 200
