from .base import *


class TestUser(BaseTestClass):

    def test_signup(self):
        response = self.client.post('/auth/signup',
                                    data=json.dumps({
                                        'username': 'Maureen',
                                        'email': 'nansubuga@gmail.com',
                                        'password': 'carol1234'}),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'User created successfully')

    def test_signup_invalid_email(self):
        response = self.client.post('/auth/signup',
                                    data=json.dumps({
                                        'username': 'Maureen',
                                        'email': 'nansubuga@gmail',
                                        'password': 'carol1234'}),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Invalid email format.')

    def test_signup_same_username(self):
        self.signup_user()
        response = self.signup_user()
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Username already exists')

    def test_signup_no_username(self):
        response = self.client.post('/auth/signup',
                                    data=json.dumps(self.user_1),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Username is required')

    def test_signup_no_email(self):
        response = self.client.post('/auth/signup',
                                    data=json.dumps(self.user_3),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertEqual(data[u'message'], 'Email is required')

    def test_signup_no_password(self):
        response = self.client.post('/auth/signup',
                                    data=json.dumps(self.user_5),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Password is required')

    def test_login_no_username(self):
        response = self.client.post('/auth/login',
                                    data=json.dumps(self.user_6),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Username is required')

    def test_login_no_password(self):
        response = self.client.post('/auth/login',
                                    data=json.dumps(self.user_5),
                                    headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Password is required')
