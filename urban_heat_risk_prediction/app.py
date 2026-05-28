from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.models import MODEL_PATH, train_model
from src.preprocessing import FEATURE_COLUMNS
from src.recommendation import recommend_action, risk_score


app = FastAPI(
    title="Urban Heat Risk Prediction API",
    description="Predicts neighborhood heat-risk levels and recommends city-planning actions.",
    version="1.0.0",
)


class HeatRiskRequest(BaseModel):
    average_temperature: float = Field(..., ge=0)
    max_temperature: float = Field(..., ge=0)
    night_temperature: float = Field(..., ge=0)
    population_density: float = Field(..., ge=0)
    elderly_population_pct: float = Field(..., ge=0, le=100)
    children_population_pct: float = Field(..., ge=0, le=100)
    tree_cover_pct: float = Field(..., ge=0, le=100)
    concrete_surface_pct: float = Field(..., ge=0, le=100)
    distance_to_cooling_center_km: float = Field(..., ge=0)
    median_income_usd: float = Field(..., ge=0)
    hospital_distance_km: float = Field(..., ge=0)
    historical_heat_cases: float = Field(..., ge=0)


def get_model():
    model_path = Path(MODEL_PATH)
    if not model_path.exists():
        train_model()
    return joblib.load(model_path)


@app.get("/")
def home():
    return {
        "message": "Urban Heat Risk Prediction API",
        "docs": "/docs",
        "model": "RandomForestClassifier",
    }


@app.post("/predict")
def predict_heat_risk(payload: HeatRiskRequest):
    model = get_model()
    input_data = payload.model_dump()
    frame = pd.DataFrame([[input_data[column] for column in FEATURE_COLUMNS]], columns=FEATURE_COLUMNS)
    predicted_risk = str(model.predict(frame)[0])

    return {
        "heat_risk_level": predicted_risk,
        "risk_score": risk_score(input_data),
        "recommended_action": recommend_action(
            predicted_risk,
            payload.tree_cover_pct,
            payload.distance_to_cooling_center_km,
        ),
    }
