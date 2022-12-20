from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s - %(funcName)s')

app = Flask(__name__)
application = app

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@pr_incident_db/project_incident_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://std_1760_pd1:std_1760_pd1@std-mysql.ist.mospolytech.ru/std_1760_pd1'

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

logging.info("successful connection to DB")

migrate = Migrate(app, db)

logging.info("successful start application")

from models import Accidents


@app.route('/', methods=['GET'])
def some_method():
  resp = {
          "status": "ok",
        }
  return jsonify(resp)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    logging.debug("request to /get_my_ip")
    return jsonify({'ip': request.remote_addr})

@app.route('/accident/getAll', methods=['GET'])
def getAllAccidents():
    logging.debug("request to /accident/getAll")
    s = Accidents.query.all()
    print(s)
    l = list()
    for i in s:
        data = {
            'id': i.id,
            'Название': i.name,
            'Описание': i.description,
            'Тип': i.type_id,
            'Дата': i.date,
        }
        l.append(data)


    return jsonify(l)
