from flask import Flask, url_for, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'standard index page'


@app.route('/test_latest')
def test_latest():
    database_address = "192.168.1.31"
    database_user = "pi"
    database_password = "PzFhr2017"
    database_name = "plantguardian_test"
    # open connection
    conn = psycopg2.connect('host={} user={} password={} dbname={}'
                            .format(database_address, database_user, database_password, database_name))
    cursor = conn.cursor()

    # get latest measurements from database
    query = "SELECT * FROM public.measurements ORDER BY measurementtime ASC, measurementtype ASC, bedname ASC, gardenname ASC LIMIT 4"
    cursor.execute(query)
    # save return of query to variable rows
    rows = cursor.fetchall()

    conn.commit()
    # close connection
    conn.close()
    cursor.close()

    # create string
    return_list = []
    return_dict = {}

    for row in range(0, len(rows)):

        # add the values of the row to return_dict
        return_dict["measurement_time"] = rows[row][0].strip()
        return_dict["measurement_type"] = rows[row][1].strip()
        return_dict["measurement_value"] = rows[row][2]
        return_dict["bed_name"] = rows[row][3].strip()
        return_dict["garden_name"] = rows[row][4].strip()

        # add a copy of return_dict to the return_list
        return_list.append(dict(return_dict))

        # empty return_dict
        return_dict.clear()

    return jsonify(return_list)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


if __name__ == '__main__':
    app.run()
