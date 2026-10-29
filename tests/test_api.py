
from fastapi.testclient import TestClient

from src.app.main import app, model, FEATURES

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_is_loaded():
    assert model is not None
    assert hasattr(model, "predict_proba")


def test_predict_with_valid_input():
    customer = {
        "tenure_months": 5,
        "monthly_fee": 95.0,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200
    assert "churn_probability" in response.json()


def test_predict_rejects_invalid_input():
    customer = {
        "tenure_months": -1,
        "monthly_fee": 95.0,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_prediction_is_deterministic():
    customer = {
        "tenure_months": 5,
        "monthly_fee": 95.0,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    first_response = client.post("/predict", json=customer)
    second_response = client.post("/predict", json=customer)

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert (
        first_response.json()["churn_probability"]
        == second_response.json()["churn_probability"]
    )
