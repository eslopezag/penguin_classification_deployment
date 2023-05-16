from fastapi.testclient import TestClient

from main import app


home = TestClient(app)


def test_get_func():
    response = home.get('/get?cl=1.0&cd=1.0&fl=1.0')
    assert response.status_code == 200
    assert 'features' in response.json()
    assert 'prediction' in response.json()
    assert response.json()['prediction'] in {'Adelie', 'Chinstrap', 'Gentoo'}


def test_post_json_validation():
    json = {
        'culmen_length': 'This is not a float',
        'culmen_depth': 1.0,
        'flipper_length': 2.0,
    }
    response = home.post('/json', json=json)
    assert response.status_code == 422
