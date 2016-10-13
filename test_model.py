from models import *
from ext_models.address import Address
from models.extension import Extension
from models.humanname import HumanName
from models.patient import Patient

p = Patient()
p.name = [HumanName()]
p.name[0].use = 'official'
p.name[0].familyname = ['Reenen']
p.name[0].given = ['Hendrikus', 'Herman', 'Johannes']
p.name[0].extension = [Extension()] #niet zeker van juistheid hiervan
p.name[0].extension[0].url = 'http://nictiz.org/huham_name_def_nl/prefix'
p.name[0].extension[0].valueString = 'van'
p.name[0].text = 'Hendrikus Herman Johannes van Reenen'
, 'H', 'H', 'J']
p.active = True
p.address = [Address.from_str("Reigersberg 10, 6865NL, Doorwerth, NL")]

json = p.as_json()
print(json)
import json
s = """{'name': [{'given': ['Pieter', 'H', 'H', 'J']}], 'resourceType': 'Patient'}"""
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)

p2 = Patient(d)
json = p2.as_json()
print(json)

p4 = Patient({'resourceType': 'Patient', 'name': [{'given': ['Henk-Jan', 'H', 'H', 'J']}]})

module = __import__('models.patient')
module = getattr(module, "patient")
cls = getattr(module, "Patient")

instance = cls()

# mod = __import__('models.patient')
# cls = getattr(mod, "Patient")
p3 = instance
json = p3.as_json()
print(json)
