from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.httpauth import HTTPBasicAuth

from config import config
from database import Database
from models.patient import Patient
from resource_convert import ResourceConverter
import os

app = Flask(__name__)
auth = HTTPBasicAuth()


@app.route('/')
def index():
    with open(os.path.dirname(__file__)+ '/templates/index.html', 'r') as f:
        return f.read()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.get_password
def get_password(username):
    if username == 'hj':
        return 'pass'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/<string:name>/<int:id>', methods=['GET'])
@auth.login_required
def get_resource(name, id):
    db = Database(config)
    json =  db.get_resource(name, id)
    if not json:
        return "niet gevonden"
    return json

@app.route('/<string:name>', methods=['GET'])
def get_resources(name):
    return name

@app.route('/<string:res_name>', methods=['POST'])
def create_resource(res_name: str):
    if not request.json:
        print('400')
        abort(400)
    msg = try_parse_resource(res_name, request.json)
    if msg:
        return msg
    db = Database(config)
    db.insert_resource(res_name, request.json)
    return jsonify({}), 201

@app.route('/<string:res_name>/<int:id>', methods=['PUT'])
def update_resource(res_name, id):
    msg = try_parse_resource(res_name, request.json)
    if msg:
        return msg
    db = Database(config)
    db.update_resource(id, request.json)
    return jsonify({}), 201

@app.route('/<string:res_name>/<int:id>', methods=['DELETE'])
def delete_resource(res_name, id):
    db = Database(config)
    db.delete_resource(id)
    return jsonify({'result': True}), 201

def try_parse_resource(res_name, json):
    try:
        resource = ResourceConverter.from_json(res_name, json)
    except Exception as ex:
        return 'geen geldige json voor ' + res_name

if __name__ == '__main__':
    app.run()
