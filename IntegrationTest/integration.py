import pytest
import os
from database import create_db

#to run the test:
#coverage run -m pytest

@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ['DATABASE_FILENAME'] = str(database_filename)

@pytest.fixture(scope='module')
def test_createnote_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h1>Todo App</h1>"
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data

def test_createnote_post(test_client):
    # Given
    expected_status_code = 200
    expected_note_text = b"TEST"
    data_to_add={"text":"TEST"}
    # When
    response = test_client.post('/',data=data_to_add,follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
    assert expected_note_text in response.data


def test_updatenote_get(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"<h1>Todo App</h1>"
    id_to_update=1
    # When
    response = test_client.get(f'/edit/{id_to_update}')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data


def test_deletenote_post(test_client):
    # Given
    expected_status_code = 200
    expected_note_text = b"test"
    id_to_delete = 1
    # When
    response = test_client.post(f'/{id_to_delete}',follow_redirects=True )
    # Then
    assert expected_status_code == response.status_code
    assert expected_note_text not in response.data