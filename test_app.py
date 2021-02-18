import unittest
from app import crud_app, db
import json
import os

class UserlistTestCase(unittest.TestCase):

    def setUp(self):
        """ Define test variables and initialize app"""
        self.app = crud_app(config_name="testing")
        self.client = self.app.test_client
        self.userlist = {'name': 'rajanazirul', 'email': 'rajanazirul@gmail.com'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()
        
    def test_user_create(self):
        ''' Test create user '''
        res = self.client().post('/userlists/', data=self.userlist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('rajanazirul', str(res.data))
        self.assertIn('rajanazirul@gmail.com', str(res.data))

    def test_user_get(self):
        ''' Test get User '''
        res = self.client().post('/userlists/', data=self.userlist)
        response = json.loads(res.get_data())
        self.assertEqual('rajanazirul', response['name'])

    def test_user_edit(self):
        ''' Test edit user by id '''
        res = self.client().post('/userlists/', data=self.userlist)
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.get_data())
        self.assertEqual('rajanazirul', response['name'])
        res = self.client().put('/userlists/1', data={'name': 'john', 'email': 'john@gmail.com'})
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/userlists/1')
        response = json.loads(res.get_data())
        self.assertEqual('john', response['name'])
    
    def test_user_delete(self):
        ''' Test delete user by id '''
        res = self.client().post('/userlists/', data=self.userlist)
        self.assertEqual(res.status_code, 201)
        res = self.client().delete('/userlists/1')
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/userlists/1')
        self.assertEqual(res.status_code, 404)

    def test_user_duplicate(self):
        ''' Test duplicate user '''
        res = self.client().post('/userlists/', data={'name': 'john', 'email': 'john@gmail.com'})
        rv = self.client().post('/userlists/', data={'name': 'john', 'email': 'john@gmail.com'})
        self.assertEqual(res.status_code, 201)
        response = json.loads(rv.get_data())
        self.assertEqual(response['message'], 'user already exist')

    def tearDown(self):
        """" teardown all initialized variables. """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

