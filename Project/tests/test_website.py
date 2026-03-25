import pytest
from unittest.mock import patch, MagicMock
from website import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    res = client.get('/')
    assert res.status_code == 200


def test_chatbot_route_returns_response(client):
    mock_response = MagicMock()
    mock_response.choices[0].message = {'content': 'Welcome to Landon Hotel!'}

    with patch('website.create_chat_completion', return_value=mock_response):
        res = client.post('/chatbot', json={"question": "What are your amenities?"})
        assert res.status_code == 200
        assert "response" in res.get_json()


def test_off_topic_question(client):
    mock_response = MagicMock()
    mock_response.choices[0].message = {'content': "I can't assist you with that, sorry!"}

    with patch('website.create_chat_completion', return_value=mock_response):
        res = client.post('/chatbot', json={"question": "What is the capital of France?"})
        data = res.get_json()
        assert "can't assist" in data["response"]
