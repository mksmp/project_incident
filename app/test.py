import json
import unittest
import requests
from flask import request


class TestAPI(unittest.TestCase):

    def test1(self):
        resp = requests.get("http://127.0.0.1:10080/")
        self.assertEqual(resp.status_code, 200)
        print("test1: OK")
        
    def test2(self):
        resp = requests.get("http://127.0.0.1:10080/accident/getAll")
        self.assertEqual(resp.status_code, 200)
        print("test2: OK")
        
    def test3(self):

        headers = {'content-type': 'application/json'}
        data = {
        'start': "2022-11-01",
        'end': "2022-11-02"
        }

        resp = requests.get("http://127.0.0.1:10080/accident/getBetween", data=json.dumps(data), headers=headers)
        self.assertEqual(resp.status_code, 200)
        print("test3: OK")

    def test4(self):
        resp = requests.post("http://127.0.0.1:10080/accident/create")
        self.assertEqual(resp.status_code, 200)
        print("test4: OK")

        
if __name__ == '__main__':
    tester = TestAPI()
    print(request.remote_addr)
    tester.test1()
    tester.test2()
    tester.test3()
