import unittest
import json
from app import create_app
from app.createdb import main, connect_to_db
from app.models import User, Entry

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'


class BaseClass(unittest.TestCase):

    def setUp(self):
        main('testing')

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {
            "username": "mathias",
            "email": "mat@yahoo.com",
            "password": "angule"
        }
        self.entry_data = {
            "title": "Day one",
            "description": "Day one was awesome"
        }

        self.user1 = User(
            username='user_!',
            email='user_1@email.com',
            password='pass')
        self.entry1 = Entry(
            title='Shopping day',
            description='I went for shopping in town',
            user_id=1)
        self.test_user = User(
            username='lubutse',
            email='lubutse92@mail.com',
            password='myname')

    def logged_in_user(self):
        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.user_data),
                         content_type='application/json')
        res = self.client.post(LOGIN_URL,
                               data=json.dumps({'username': 'mathias', 'password': 'angule'}),
                               content_type='application/json')

        return res

    def tearDown(self):
        conn = connect_to_db('testing')
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS users CASCADE""")
        cur.execute("""DROP TABLE IF EXISTS entries CASCADE""")

        cur.close()
        conn.commit()
        conn.close()
