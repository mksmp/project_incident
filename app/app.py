import time
from flask import Flask, jsonify, request, Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge

logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s - %(funcName)s')

app = Flask(__name__)
application = app

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed request.')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1,2,5,6,10,_INF))


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@pr_incident_db/project_incident_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://std_1760_pd1:std_1760_pd1@std-mysql.ist.mospolytech.ru/std_1760_pd1'

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

logging.info("successful connection to DB")

migrate = Migrate(app, db)

logging.info("successful start application")

from models import Accidents

@app.route('/', methods=['GET'])
def some_method():
    start = time.time()
    graphs['c'].inc()
    time.sleep(0.5)
    end = time.time()
    graphs['h'].observe(end - start)
    resp = {
          "status": "ok",
        }
    return jsonify(resp)

@app.route("/metrics")
def request_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

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
