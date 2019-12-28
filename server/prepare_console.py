from server import db
from server.models import Measurement
from json import dumps
from flask import jsonify

measurements = db.session.query(Measurement).filter(Measurement.garden_name == "mygarden").all()
measurements_list = []
for m in measurements:
    measurements_list.append(m.serialize)

print(jsonify(measurements_list))
print(type(jsonify(measurements_list)))

