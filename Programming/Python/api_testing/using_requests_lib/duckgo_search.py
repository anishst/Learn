import requests

# API info: https://api.duckduckgo.com/api?kp=1

def test_duckduckgo_instant_answer_api_search():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    # Act
    response = requests.get(url)
    body = response.json()
    print(body)

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']

