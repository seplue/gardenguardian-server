from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gardenguardian_db_test.db' + '?check_same_threads=False'
db = SQLAlchemy(app)
CORS(app)

# this import needs to be here, not at the top of the file
from server import routes
