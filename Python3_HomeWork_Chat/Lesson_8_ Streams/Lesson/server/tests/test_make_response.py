import pytest
from datetime import datetime

from protocol import make_response


@pytest.fixture
def expected_action():
    return 'test'

@pytest.fixture
def expected_code():
    return 200

@pytest.fixture
def expected_data():
    return 'Some data'

@pytest.fixture
def initial_request(expected_action, expected_data):
    return {
        'action': expected_action,
        'time': datetime.now().timestamp(),
        'data': expected_data,
    }


def test_action_make_response(initial_request, expected_action, expected_code, expected_data):
    actual_response = make_response(
        initial_request, expected_code, expected_data
    )
    assert actual_response.get('action') == expected_action

def test_code_make_response(initial_request, expected_code, expected_data):
    actual_response = make_response(
        initial_request, expected_code, expected_data
    )
    assert actual_response.get('code') == expected_code

def test_data_make_response(initial_request, expected_code, expected_data):
    actual_response = make_response(
        initial_request, expected_code, expected_data
    )
    assert actual_response.get('data') == expected_data
