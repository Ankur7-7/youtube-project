# import sys
# sys.path.append('./../app')
from flask import Flask


# from flask_cors import CORS

# ABC comment

# from app.helpers.db.db import MySQL, Redshift
from app.config.config import set_config
from flask_cors import CORS

# starting the app
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*", "allow_headers":"*"}})
# CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/comments": {"origins": "https://main.d1n263dwto7ico.amplifyapp.com"}})
#cors = CORS(app, resources={r"/comments": {"origins": "*"}})

# setting the environment configuration
app.config.from_object(set_config())

# opening the db connection
# mysql = MySQL(app=app)
# redshift = Redshift(app=app)


