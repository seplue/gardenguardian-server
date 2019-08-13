from flask import Flask, url_for, jsonify
from flask_cors import CORS
import psycopg2
import mysql.connector

app = Flask(__name__)
CORS(app)

# development database configuration
database_address = "192.168.1.31"
database_user = "gardenguardian"
database_password = "Passwort123"
database_name = "gardenguardian_test"

# create connection to database
mydb = mysql.connector.connect(
    host=database_address,
    user=database_user,
    passwd=database_password,
    database=database_name
)
mycursor = mydb.cursor()


@app.route('/')
def index():
    return 'standard index page'


@app.route('/test_latest')
def test_latest():

    # get latest measurements from database
    # ordered by newest measurementTime and by alphabetical measurementType
    sql = "SELECT * FROM measurements ORDER BY measurementTime DESC, MeasurementType ASC LIMIT 4"
    mycursor.execute(sql)
    # save return of query to variable rows
    rows = mycursor.fetchall()

    # create a json with a list of arrays with the data from the database
    return_list = []
    for row in range(0, len(rows)):
        return_dict = {}
        # add the values of the row to return_dict
        return_dict["measurement_time"] = rows[row][0].strip()
        return_dict["measurement_type"] = rows[row][1].strip()
        return_dict["measurement_value"] = rows[row][2]
        return_dict["bed_name"] = rows[row][3].strip()
        return_dict["garden_name"] = rows[row][4].strip()

        # add a copy of return_dict to the return_list
        return_list.append(dict(return_dict))

    return jsonify(return_list)


@app.route('/<garden_name>/<bed_name>/<measurementType>')
def get_specific_measurement():
    pass


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


if __name__ == '__main__':
    app.run()
