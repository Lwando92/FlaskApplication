#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for flaskbasic.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

# import pytest
import pytest
from src.flaskbasic import create_app, db
from src.flaskbasic.models import Student


@pytest.fixture(scope='module')
def new_student():
    student = Student('Lwando', 10, 20, 30)
    return student


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    student1 = Student('Lwando', 10, 20, 30)
    student2 = Student('Lihle', 100, 200, 300)
    # user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    # user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    db.session.add(student1)
    db.session.add(student2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
