import json
import os
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Model path: prefer the promoted champion artifact.
MODEL_PATH = PROJECT_ROOT / "artifacts" / "model.joblib"

if not MODEL_PATH.exists():
    MODEL_PATH = PROJECT_ROOT / "model.joblib"

# Metadata path.
METADATA_PATH = PROJECT_ROOT / "metadata.json"

if not METADATA_PATH.exists():
    METADATA_PATH = PROJECT_ROOT / "artifacts" / "metadata.json"

# Build lineage information.
COMMIT_SHA = os.getenv("GIT_SHA", "unknown")
IMAGE_TAG = os.getenv("IMAGE_TAG", "unknown")

FEATURES = [
    "tenure_months",
    "monthly_charges",
    "support_calls",
    "contract",
    "internet_service",
]

app = FastAPI(title="AI381 Churn Prediction API")

# Load the promoted champion model and its metadata.
model = joblib.load(MODEL_PATH)
metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))


class CustomerInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenure_months: int = Field(ge=0)
    monthly_fee: float = Field(ge=0)
    support_calls: int = Field(ge=0)
    contract: str = Field(min_length=1)
    internet_service: str = Field(min_length=1)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": COMMIT_SHA,
        "commit_sha": COMMIT_SHA,
        "image_tag": IMAGE_TAG,
        "mlflow_run_id": metadata["mlflow_run_id"],
    }


@app.post("/predict")
def predict(customer: CustomerInput):
    data = customer.model_dump()

    # Convert the API field name to the model's expected feature name.
    data["monthly_charges"] = data.pop("monthly_fee")

    X = pd.DataFrame([data], columns=FEATURES)

    probability = float(model.predict_proba(X)[0, 1])

    return {
        "churn_probability": round(probability, 3)
    }
