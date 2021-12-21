from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}


# test to check if Iris Versicolour is classified correctly
def test_pred_versicolour():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3.1,
        "sepal_width": 1,
        "petal_length": 1,
        "petal_width": 1,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Versicolour"}


# test to check if invalid param in payload is passed
def test_pred_invalid_payload():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 2,
        "sepal_wid": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 422
        assert response.json() == {'detail': [{'loc': ['body', 'sepal_width'], 'msg': 'field required', 'type': 'value_error.missing'}]}


# test to check if invalid param in payload is passed
def test_pred_empty_payload():
    # defining a sample payload for the testcase
    payload = {
        
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 422
        assert response.json() == {'detail': [{'loc': ['body', 'sepal_length'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'sepal_width'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'petal_length'], 'msg': 'field required', 'type': 'value_error.missing'},  {'loc': ['body', 'petal_width'], 'msg': 'field required', 'type': 'value_error.missing'}]}


# test to check if Iris Setosa is classified correctly
def test_pred_setosa():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] ==  "Iris Setosa"

# test to check if Iris Virginica is classified correctly with different payload
def test_pred_virginica_diff_payload():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.2,
        "sepal_width": 5.4,
        "petal_length": 10.4,
        "petal_width": 6.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] == "Iris Virginica"

#test to check feedback_loop method for Iris Virginica
def test_feedback_loop_virginica():
# defining a sample payload for the testcase
    payload = [{
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
        "flower_class":"Iris Virginica"
    }]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful"}

#test to check feedback_loop method
def test_feedback_loop():
# defining a sample payload for the testcase
    payload = [{
        "sepal_length": 3.8,
        "sepal_width": 8,
        "petal_length": 5.2,
        "petal_width": 4.4,
        "flower_class":"Iris Setosa"
    }]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful"}