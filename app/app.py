import pymysql.cursors
from config import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER
from flask import Flask, jsonify, request

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

# mysql = pymysql(app)

connection = pymysql.connect(host=MYSQL_HOST,
                            user=MYSQL_USER,
                            password=MYSQL_PASSWORD,
                            database=MYSQL_DATABASE,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)



@app.route('/', methods=['GET'])
def some_method():
  resp = {
          "status": "ok",
        }
  return jsonify(resp)

@app.route('/accident/getAll', methods=['GET'])
def getAllAccidents():
    with connection.cursor() as cursor:
        sql = 'SELECT accidents.name, accidents.description, types.type, accidents.date FROM accidents INNER JOIN types on accidents.type_id = types.id;'
        cursor.execute(sql)
        res = cursor.fetchall()
    if len(res) == 0:
        return jsonify({'error': "Данных нет"})
    print(res)
    l = list()
    for i in range(len(res)):
        data = {
            'Название': res[i]["name"],
            'Описание': res[i]["description"],
            'Тип': res[i]["type"],
            'Дата': res[i]["date"],
        }
        l.append(data)

    return jsonify(l)

@app.route('/accident/getById:<int:id>', methods=['GET'])
def getAccidentsById(id):
    with connection.cursor() as cursor:
        sql = 'SELECT accidents.name, accidents.description, types.type, accidents.date FROM accidents INNER JOIN types on accidents.type_id = types.id WHERE accidents.id = %s;'
        cursor.execute(sql, (str(id)))
        res = cursor.fetchall()
    if len(res) == 0:
        return jsonify({'error': "Данных нет"})
    data = {
        'Название': res[0]["name"],
        'Описание': res[0]["description"],
        'Тип': res[0]["type"],
        'Дата': res[0]["date"],
    }


    return jsonify(data)


@app.route('/accident/getBetween', methods=['GET'])
def getBetween():
    data = {
        'start': request.json['start'],
        'end': request.json['end'],
    }

    with connection.cursor() as cursor:
        sql = "SELECT accidents.name, accidents.description, types.type, accidents.date FROM accidents INNER JOIN types on accidents.type_id = types.id WHERE accidents.date BETWEEN %s and %s;"
        cursor.execute(sql, (data['start'], data['end']))
        res = cursor.fetchall()
    if len(res) == 0:
        return jsonify({'error': "Данных нет"})

    l = list()
    for i in range(len(res)):
        data = {
            'Название': res[i]["name"],
            'Описание': res[i]["description"],
            'Тип': res[i]["type"],
            'Дата': res[i]["date"],
        }
        l.append(data)

    return jsonify(l)


@app.route('/accident/create', methods=['POST'])
def create():
    data = {
        'name': request.json['name'],
        'description': request.json['description'],
        'date': request.json['date'],
        'type': request.json['type'],
        'members': request.json['members'],
    }
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Members'
        cursor.execute(sql)
        members = cursor.fetchall()
    
    # добавляю тех members, которых нет в БД 
    d_members = dict()
    for i in members:
        full_name = i['first_name'] + " " + i['initials']
        for j in data['members']:
            if full_name == j:
                d_members[j] = i['id']
    for j in data['members']:
        if d_members.get(j) == None:
            s = j.split(" ")
            if len(s) != 2:
                err = "неверный формат участника '%s'" % (j)
                return jsonify({'ошибка': err })
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `Members` (`id`, `first_name`, `initials`) VALUES (NULL, %s, %s);'
                cursor.execute(sql, (s[0], s[1]))
                connection.commit()

    # получаю все members (могут изменится после добавления)
    members_list = list()

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Members'
        cursor.execute(sql)
        members = cursor.fetchall()

    for i in members:
        full_name = i['first_name'] + " " + i['initials']
        for j in data['members']:
            if full_name == j:
                members_list.append(i['id'])

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM types'
        cursor.execute(sql)
        types = cursor.fetchall()

    type_id = 0
    for i in types:
        if i['type'] == data['type']:
            type_id = i['id']
    if type_id == 0:
        err = "данного типа происшествия не существует '%s'" % (data['type'])
        return jsonify({'ошибка': err })

    with connection.cursor() as cursor:
        sql = 'SELECT MAX(id) FROM Members'
        cursor.execute(sql)
        max = cursor.fetchall()

    max_ind = int(max[0]['MAX(id)']) + 1

    with connection.cursor() as cursor:
                sql = "INSERT INTO `accidents` (`id`, `name`, `description`, `date`, `type_id`) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sql, (max_ind, data['name'], data['description'], data['date'], type_id))
                connection.commit()

    for i in members_list:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `accidents_members` (`accidents_id`, `members_id`) VALUES ('%s', '%s');;"
            cursor.execute(sql, (max_ind, i))
            connection.commit()

    return jsonify({'result': 'ок'})


@app.route('/accident/update', methods=['POST'])
def update():
    with connection.cursor() as cursor:
        sql = 'UPDATE'
        cursor.execute(sql)
        data_msgs = cursor.fetchall()
    return jsonify({'task': "OK"})


# if __name__=='__main__':
#     app.run()