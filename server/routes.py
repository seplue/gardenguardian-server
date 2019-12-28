from flask import render_template, url_for, flash, redirect, jsonify
from server import app, db
from server.models import Measurement
from json import dumps


@app.route('/')
def index():
    return 'standard index page'


@app.route('/test_latest')
def test_latest():
    return "test_latest"


@app.route('/garden/<garden_name>')
def get_specific_measurement(garden_name):
    print(garden_name)
    measurements = db.session.query(Measurement)\
        .filter(Measurement.garden_name == garden_name) \
        .order_by(Measurement.measurement_time.desc()) \
        .limit(4)\
        .all()
    measurements_list = []
    for m in measurements:
        measurements_list.append(m.serialize)
    jsonified_measurements_list = jsonify(measurements_list)
    print(jsonified_measurements_list)
    print(type(jsonified_measurements_list))
    return jsonify(measurements_list)


@app.route('/allMeasurements')
def get_all_measurements():
    measurements = db.session.query(Measurement)\
        .order_by(Measurement.measurement_time.desc())\
        .all()
    measurements_list = []
    for m in measurements:
        measurements_list.append(m.serialize)
    jsonified_measurements_list = jsonify(measurements_list)
    print(jsonified_measurements_list)
    print(type(jsonified_measurements_list))
    return jsonify(measurements_list)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

