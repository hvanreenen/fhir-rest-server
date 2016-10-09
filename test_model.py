from models import *
from models.humanname import HumanName
from models.patient import Patient

p = Patient()
p.name = [HumanName()]
p.name[0].given = ['Henk-Jan', 'H', 'H', 'J']
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
