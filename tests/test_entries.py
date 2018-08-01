from .base import *


class TestEntry(BaseTestClass):

    def test_get_all_entries(self):
        res = self.signup_user()
        self.assertEqual(res.status_code, 201)

        res = self.login_user()
        print(res)
        self.assertEqual(res.status_code, 200)

        self.client.post('/api/v1/entries',
                         data=json.dumps(self.entry),
                         content_type='application/json')

        response = self.client.get('/api/v1/entries',
                                   headers={
                                       'content_type': 'application/json'
                                   },
                                   data=json.dumps(self.entry),
                                   )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[u'message'], 'Entries found successfully')

#     def test_get_entry_by_id(self):
#         self.client.post('/api/v1/entries/<int:entry_id>',
#                          data=json.dumps(self.entry),
#                          content_type='application/json')
#         response = self.client.get('/api/v1/entries/1',
#                                    data=json.dumps(self.entry),
#                                    content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Entry retrieved successfully')
#
#     def test_add_entry(self):
#         response = self.client.post('/api/v1/entries',
#                                     data=json.dumps(self.entry),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Entry successfully created')
#
#     def test_add_entry_without_title(self):
#         response = self.client.post('/api/v1/entries',
#                                     data=json.dumps(self.entry_without_title),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Title is required')
#
#     def test_add_entry_without_entry(self):
#         response = self.client.post('/api/v1/entries',
#                                     data=json.dumps(self.entry_without_entry),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Entry is required')
#
#     def test_delete_entry(self):
#         self.client.post('/api/v1/entries',
#                          data=json.dumps(self.entry),
#                          content_type='application/json')
#         response = self.client.delete('/api/v1/entries/1',
#                                       content_type='application/json')
#         self.assertEqual(response.status_code, 204)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Entry deleted successfully')
#
#     def test_update_entry(self):
#         self.client.post('/api/v1/entries',
#                          data=json.dumps(self.entry),
#                          content_type='application/json')
#         response = self.client.put('/api/v1/entries/1',
#                                    data=json.dumps({
#                                        'title': 'Mimi',
#                                        'entry': 'Mimi na wewe, wewe na mimi'}),
#                                    content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['message'], 'Updated successful')
