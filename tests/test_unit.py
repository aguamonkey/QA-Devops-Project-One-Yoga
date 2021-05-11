import unittest
# Import the necessary modules
from flask import url_for
from flask.wrappers import Response
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Task

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
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
        test_task = Task(description="Test the flask app")
        db.session.add(test_task)
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

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_complete_get(self):
        response = self.client.get(url_for('complete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_incomplete_get(self):
        response = self.client.get(url_for('incomplete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Test the flask app",response.data)

class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post(
            url_for('create'),
            data=dict(description="Create a new task"),
            follow_redirects=True
        )
        self.assertIn(b"Create a new task", response.data)

class TestUpdate(TestBase):
     def test_update_task(self):
        response = self.client.post(
            url_for('update', id=1),
            data=dict(description="Update a task"),
            follow_redirects=True
        )
        self.assertIn(b"Update a task", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test the flask app", response.data)