import json
from src.main import lambda_handler

def test_lambda_handler():
    event = {"path": "/rates"}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert isinstance(json.loads(response["body"]), dict)

    event = {"path": "/rates/delta"}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert isinstance(json.loads(response["body"]), list)

    event = {"path": "/unknown"}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 404