import pytest
import requests

host = 'http://127.0.0.1:5000'

def test_time_response():
    """
    GIVEN: The Flask API application running on the host defined above
    WHEN: the /api/v1/time endpoint is invoked
    THEN: the response shall have a status code of 200
    """
    r = requests.get(host + '/api/v1/time')  # Assumses that it has a path of "/"
    assert r.status_code == 200  # Assumes that it will return a 200 response

def test_status_response():
    """
    GIVEN: The Flask API application running on the host defined above
    WHEN: the /api/v1/status endpoint is invoked
    THEN: the response shall have a status code of 200
    """
    r = requests.get(host + '/api/v1/status')  # Assumses that it has a path of "/"
    assert r.status_code == 200  # Assumes that it will return a 200 response

def test_serializer_response():
    """
    GIVEN: The Flask API application running on the host defined above
    WHEN: the /api/v1/serializer/test-string endpoint is invoked
    THEN: the response shall have a status code of 200
    """
    r = requests.get(host + '/api/v1/serializer/test-string')  # Assumses that it has a path of "/"
    assert r.status_code == 200  # Assumes that it will return a 200 response

def test_serializer_json_response():
    """
    GIVEN: The Flask API application running on the host defined above
    WHEN: the /api/v1/serializer/test-string endpoint is invoked
    THEN: the response shall be in a json format having a "param" key with a value of "test-string"
    """
    r = requests.get(host + '/api/v1/serializer/test-string')  # Assumses that it has a path of "/"
    data = r.json()
    assert data["param"] == "test-string"  # Assumes that it will return a 200 response
