import json
import unittest
from unittest import TestCase
from app import app
from app.models import Database
from instance.config import app_config


class BaseTestClass(TestCase):

    def setUp(self):
        self.app = app.config.from_object(app_config['testing'])
        self.client = app.test_client()

        self.entry = {
            'title': 'Day 1',
            'entry': 'Wrote an awesome blog'
        }

        self.entry_without_title = {
            'entry': 'Wrote an awesome blog'
        }

        self.entry_without_entry = {
            'title': 'Day 1'
        }

        self.user = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com",
            "password": "angule1234"
        }

        # User with wrong username
        self.user = {
            "username": "mathiassss",
            "email": "angulemathias3@gmail.com",
            "password": "123456234"
        }

        # User with no name
        self.user_1 = {
            "email": "angulemathias3@gmail.com",
            "password": "angule1234"
        }

        # User with no password
        self.user_2 = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com"
        }

        # User with no email
        self.user_3 = {
            "username": "mathias",
            "password": "angule1234"
        }

        # User with wrong password
        self.user = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com",
            "password": "123456234"
        }

        # User with no password
        self.user = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com"
        }

    def logged_in_user(self):
        self.client.post('/auth/signup',
                         data=json.dumps(self.user),
                         headers={'content-type': 'application/json'})
        res = self.client.post('/auth/login',
                               data=json.dumps(self.user),
                               headers={'content-type': 'application/json'})

        return res

    def tearDown(self):
        Database().drop_table_user()
        Database().drop_table_entry()

    if __name__ == '__main__':
        unittest.main()
