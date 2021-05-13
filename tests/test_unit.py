import unittest
# Import the necessary modules
from flask import url_for
from flask.wrappers import Response
from flask_testing import TestCase
import os
from os import getenv

# import the app's classes and objects
from application import app, db
from application.models import YogaMove, YogaSequence

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        SECRET_KEY = os.urandom(32)

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
                SECRET_KEY=SECRET_KEY,
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        test_move = YogaMove(description="Test the flask app", instruction="Lay on the ground", difficulty="Beginner")
        test_sequence = YogaSequence(name="Test sequence name", difficulty="Beginner", time=15)
        db.session.add(test_move)
        db.session.add(test_sequence)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_create_sequence_get(self):
        response = self.client.get(url_for('createsequence'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_sequence_get(self):
        response = self.client.get(url_for('updatesequences', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_sequence_get(self):
        response = self.client.get(url_for('deletesequence', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_move(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test the flask app",response.data)

    def test_read_sequence(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test sequence name", response.data)

class TestCreate(TestBase):
    def test_create_move(self):
        response = self.client.post(
            url_for('create'),
            data=dict(description="Create a new move", instruction="do something", difficulty="Intermediate"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new move", response.data)
        self.assertIn(b"Intermediate", response.data)

    def test_create_sequence(self):
        response = self.client.post(
            url_for('createsequence'),
            data=dict(name="Create a new sequence", difficulty="Intermediate", time=25, instruction=1, add_instruction=True),
            follow_redirects=True
        )
        self.assertIn(b"Create a new sequence", response.data)
        self.assertIn(b"Intermediate", response.data)
        self.assertIn(b"Test the flask app", response.data)
        
        response = self.client.post(
            url_for('createsequence'),
            data=dict(name="Create a new sequence", difficulty="Intermediate", time=25, instruction=1, submit=True),
            follow_redirects=True
        )
        self.assertIn(b"Create a new sequence", response.data)
        self.assertIn(b"Intermediate", response.data)


        

class TestUpdate(TestBase):
    def test_update_move(self):
        response = self.client.post(
            url_for('update', id=1),
            data=dict(description="Test the flask app update", instruction="stand up tall", difficulty="Advanced"),
            follow_redirects=True
        )
        self.assertIn(b"Test the flask app update", response.data)
        self.assertIn(b"Advanced", response.data)


    def test_update_sequence(self):
        response = self.client.post(
            url_for('updatesequences', id=1),
            data=dict(name="Update a new sequence", difficulty="Advanced", time=30, instruction=1, add_instruction=True),
            follow_redirects=True
        )
        self.assertIn(b"Update a new sequence", response.data)
        self.assertIn(b"Advanced", response.data)
        self.assertIn(b"Test the flask app", response.data)
        
        response = self.client.post(
            url_for('updatesequences', id=1),
            data=dict(name="Update a new sequence", difficulty="Advanced", time=30, instruction=1, submit=True),
            follow_redirects=True
        )
        self.assertIn(b"Update a new sequence", response.data)
        self.assertIn(b"Advanced", response.data)


class TestDelete(TestBase):
    def test_delete_move(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test the flask app", response.data)
        self.assertNotIn(b"Lay on the ground", response.data)
       # self.assertNotIn(b"Beginner", response.data)


    def test_delete_sequence(self):
        response = self.client.get(
            url_for('deletesequence', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test sequence name", response.data)
        self.assertNotIn(b"15", response.data)
