from .base import *


class TestEntry(BaseTestClass):

    def test_get_all_entries(self):
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                         data=json.dumps(self.entry),
                         content_type='application/json',
                         headers={"Authorization": "Bearer {}".format(token)})
        response = self.client.get('/api/v1/entries',
                                   data=json.dumps(self.entry),
                                   content_type='application/json',
                                   headers={"Authorization": "Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'All entries found successfully')

    def test_get_entry_by_id(self):
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                         data=json.dumps(self.entry),
                         content_type='application/json',
                         headers={"Authorization": "Bearer {}".format(token)})
        response = self.client.get('/api/v1/entries/1',
                                   data=json.dumps(self.entry),
                                   content_type='application/json',
                                   headers={"Authorization": "Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Entry retrieved successfully')

    def test_add_entry_without_title(self):
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        response = self.client.post('/api/v1/entries',
                                    data=json.dumps(self.entry_without_title),
                                    content_type='application/json',
                                    headers={"Authorization": "Bearer {}".format(token)})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Title is required')

    def test_update_entry(self):
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                         data=json.dumps(self.entry),
                         content_type='application/json',
                         headers={"Authorization": "Bearer {}".format(token)})
        response = self.client.put('/api/v1/entries/1',
                                   data=json.dumps({
                                       'title': 'Mimi',
                                       'entry': 'Mimi na wewe, wewe na mimi'}),
                                   content_type='application/json',
                                   headers={"Authorization": "Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Updated successful')

    def test_delete_entry(self):
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                         data=json.dumps(self.entry),
                         content_type='application/json',
                         headers={"Authorization": "Bearer {}".format(token)})
        response = self.client.delete('/api/v1/entries/1',
                                      content_type='application/json',
                                      headers={"Authorization": "Bearer {}".format(token)})
        self.assertEqual(response.status_code, 204)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Entry deleted successfully')
