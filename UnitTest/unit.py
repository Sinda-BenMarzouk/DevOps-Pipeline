import sqlite3
from unittest import TestCase
from unittest.mock import patch
from main import create_note, update_note, delete_note
import os

os.environ['DATABASE_FILENAME'] = 'todo.db'

#to run the test:
#coverage run -m unittest UnitTest\unit.py


class TestCreateNote(TestCase):
    @patch("main.sqlite3", spec=sqlite3)
    def test_createNotet(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        create_note('test')
        # Then
        mock_execute.assert_called_once()

class TestUpdateNote(TestCase):
    @patch("main.sqlite3", spec=sqlite3)
    def test_updateProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        update_note(0,'test','on')
        # Then
        mock_execute.assert_called_once()

class TestDeleteNote(TestCase):
    @patch("main.sqlite3", spec=sqlite3)
    def test_deleteProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        delete_note(0)
        # Then
        mock_execute.assert_called_once()


