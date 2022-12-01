import json
import unittest

import requests
from flask import request


class TestAPI(unittest.TestCase):

    def test1(self):
        resp = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(resp.status_code, 200)
        print("test1: OK")
        
    def test2(self):
        resp = requests.get("http://127.0.0.1:5000/accident/getAll")
        self.assertEqual(resp.status_code, 200)
        print("test2: OK")
    
    def test3(self):
        resp = requests.get("http://127.0.0.1:5000/accident/getAll")

        d_req = {
            "id": 1
        }

        d_resp = {
            "Дата": "Sun, 20 Nov 2022 00:00:00 GMT",
            "Название": "Убийство на ул.Совесткая",
            "Описание": "Убийство совершено в подвале дома по адресу ул.Советская, д.1",
            "Тип": "Убийство"
        }

        headers = {'content-type': 'application/json'}

        resp = requests.get("http://127.0.0.1:5000/accident/getById", data=json.dumps(d_req), headers=headers)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), d_resp)
        print("test3: OK")
        
    def test4(self):

        headers = {'content-type': 'application/json'}
        data = {
        'start': "2022-11-01",
        'end': "2022-11-02"
        }

        resp = requests.get("http://127.0.0.1:5000/accident/getBetween", data=json.dumps(data), headers=headers)
        self.assertEqual(resp.status_code, 200)
        print("test4: OK")

    def test5(self):
        resp = requests.post("http://127.0.0.1:5000/accident/create")
        self.assertEqual(resp.status_code, 200)
        print("test5: OK")

        
if __name__ == '__main__':
    tester = TestAPI()
    tester.test1()
    tester.test2()
    tester.test3()
    tester.test4()