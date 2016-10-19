from http import server
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.httpauth import HTTPBasicAuth

from config import config
from database import Database
from models.patient import Patient
from models.humanname import HumanName
from models.identifier import Identifier
from models.fhirdate import FHIRDate

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


@app.route('/Patient/<int:id>', methods=['GET'])
def get_patient(id):
    try:
        db = Database(config)
        row = db.read_patient(id)
        p = Patient()
        p.name=[HumanName()]
        p.name[0].family = [row['achternaam'], row['partnerachternaam']]
        p.name[0].prefix = [row['tussenvoegsel'], row['partnertussenvoegsel']]
        p.name[0].text = str(row['achternaam'])+' '+str(row['partnerachternaam'] or '')
        p.gender = str(row['geslacht']).lower().replace('m', 'male').replace('v', 'female')
        p.birthDate = FHIRDate(row['geboortedatum'])
        p.identifier = [Identifier()]
        p.identifier[0].value = row['patientid']
        p.identifier[0].use = 'usual'
        p.identifier[0].system = 'Promedico'
        p.identifier[1].value = row['bsn']
        p.identifier[1].use = 'official'
        p.identifier[1].system = 'BSN'
        json = p.as_json()
        if not json:
            return "niet gevonden", 404
        return jsonify(json)
    except Exception as ex:
        print(ex.args[0])
        return 'Er is een fout' + ex.args[0], 500



@app.route('/Patient', methods=['POST'])
def create_patient(res_name: str):
    if not request.json:
        print('400')
        abort(400)
    db = Database(config)
    # db.insert_patient(request.json)
    return jsonify({}), 201

@app.route('/Patient/<int:id>', methods=['PUT'])
def update_patient(id):
    db = Database(config)
    # db.update_patient(id, request.json)
    return jsonify({}), 201


if __name__ == '__main__':
    app.run()
