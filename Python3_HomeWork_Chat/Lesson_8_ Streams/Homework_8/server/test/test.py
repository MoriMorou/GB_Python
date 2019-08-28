import pytest
from datetime import datetime
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from protocol import make_response


@pytest.fixture
def action_fixture():
    return 'some_action'


@pytest.fixture
def time_fixture():
    return datetime.now().timestamp()


@pytest.fixture
def data_fixture():
    return 'some data'


@pytest.fixture
def code_fixture():
    return 200


@pytest.fixture
def valid_request_fixture(action_fixture, time_fixture, data_fixture):
    return {
        'action': action_fixture,
        'time': time_fixture,
        'data': data_fixture
    }

@pytest.fixture
def invalid_request():
    return {}


def test_valid_make_response(valid_request_fixture, code_fixture, data_fixture):
    response = make_response(valid_request_fixture, code_fixture, data_fixture)
    assert response.get('code') == code_fixture