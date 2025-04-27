# app/routes_test.py

from flask import Blueprint, jsonify

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Pong! ArcanApp fonctionne.'})
