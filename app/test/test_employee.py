import unittest
import requests
import json


class TestApi(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self.base_url = 'http://127.0.0.1:5000/emps'
        self.headers = {'content-type': 'application/json'}

    def test_get_emp(self):
        response = requests.get(self.base_url + '/3', headers=self.headers)
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(resp_json.get('emp_name', None), (str, None)))


    def test_get_emps(self):
        response = requests.get(self.base_url, headers=self.headers)
        json_re = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json_re, list))

    def test_create_emp(self):
        payload = {"emp_name": "Alexis ROLLAND", "email": "Alexis@gmail.com"}
        response = requests.post(self.base_url, headers=self.headers, data=json.dumps(payload))
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(resp_json.get('emp_name', None), (str, None)))

    def test_update_emp(self):
        payload = {"emp_name": "Alexis ROLLAND", "email": "Alexis@gmail.com"}
        response = requests.put(self.base_url + '/3', headers=self.headers, data=json.dumps(payload))
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(resp_json.get('emp_name', None), (str, None)))

    def test_delete_emp(self):
        response = requests.delete(self.base_url + '/5', headers=self.headers)
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(resp_json.get('emp_name', None), (str, None)))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=2).run(suite)


