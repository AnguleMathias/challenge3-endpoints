import json
import unittest
from unittest import TestCase
from app.app import app
from app.models import Database


class BaseTestClass(TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        #   entry case
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

        #   user case
        self.user = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com",
            "password": "angule1234"
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
        self.user_4 = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com",
            "password": "123456234"
        }

        # User with no password
        self.user_5 = {
            "username": "mathias",
            "email": "angulemathias3@gmail.com"
        }

        # User with no username
        self.user_6 = {
            "email": "angulemathias3@gmail.com",
            "password": "angule1234"
        }

    def logged_in_user(self):
        self.client.post('/auth/signup',
                         data=json.dumps(self.user),
                         headers={'content-type': 'application/json'})
        res = self.client.post('/auth/login',
                               data=json.dumps(self.user),
                               headers={'content-type': 'application/json'})
        return res

    def signup_user(self):
        return self.client.post('/auth/signup',
                                data=json.dumps(self.user),
                                headers={'content-type': 'application/json'})

    def login_user(self):
        return self.client.post('/auth/login',
                                data=json.dumps(self.user),
                                headers={'content-type': 'application/json'})

    def tearDown(self):
        Database().drop_table_user()
        Database().drop_table_entry()

    if __name__ == '__main__':
        unittest.main()
