from flask import Flask, render_template, request, url_for, redirect
import pymysql.cursors
from config import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER

app = Flask(__name__)
application = app

# app.config.from_pyfile('config.py')

# mysql = pymysql(app)

connection = pymysql.connect(host=MYSQL_HOST,
                            user=MYSQL_USER,
                            password=MYSQL_PASSWORD,
                            database=MYSQL_DATABASE,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM tbl_msgs'
        cursor.execute(sql)
        data_msgs = cursor.fetchall()
    return render_template('index.html', data_msgs=data_msgs)

@app.route('/', methods=["GET", "POST"])
def post_new():

    form = request.form.get('message')
    with connection.cursor() as cursor:
        sql = """INSERT INTO tbl_msgs VALUES (%s)"""
        cursor.execute(sql, (form))
    connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM tbl_msgs'
        cursor.execute(sql)
        data_msgs = cursor.fetchall()
        # cursor.close()
    return render_template('index.html', data_msgs=data_msgs)

# if __name__=='__main__':
#     app.run()