from flask import Flask, url_for, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'index'


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
    query = "SELECT * FROM public.measurements ORDER BY measurementtime ASC, measurementtype ASC, bedname ASC, gardenname ASC LIMIT 1"
    cursor.execute(query)
    # save return of query to variable rows
    rows = cursor.fetchall()

    conn.commit()
    # close connection
    conn.close()
    cursor.close()

    # create string
    return_string = ""
    return_dict = {}

    for row in range(0, len(rows)):
        return_dict
        for y in range(0, len(rows[row])):
            return_string += str(rows[row][y]).strip()
        return_string += "<br/>"

    print(return_string)
    return jsonify(return_string)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


if __name__ == '__main__':
    app.run()
