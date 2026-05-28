# Urban Heat Risk Prediction

A Python backend data science project that predicts urban heat-risk levels using climate, population, and infrastructure indicators, then recommends priority actions such as cooling shelters, tree cover expansion, and public-health alerts.

## Why This Project

Extreme heat is a growing public-health risk, but every neighborhood is affected differently. Dense areas with low tree cover, high elderly population, high concrete surface, and limited access to cooling centers can become critical heat-risk zones.

This project turns those signals into a decision-support system for city planning and public-health response.

## Problem Statement

Given neighborhood-level climate, demographic, and infrastructure features, classify the heat-risk level as:

- `Low`
- `Medium`
- `High`
- `Critical`

The model also returns a recommended action for the neighborhood.

## Project Structure

```text
urban_heat_risk_prediction/
├── README.md
├── data/
│   ├── raw/
│   │   └── urban_heat_sample.csv
│   └── processed/
├── notebooks/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   └── recommendation.py
├── tests/
│   ├── test_preprocessing.py
│   └── test_recommendation.py
├── requirements.txt
├── app.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── results/
    └── model_metrics.json
```

## Features Used

- Average temperature
- Maximum temperature
- Night temperature
- Population density
- Elderly population percentage
- Children population percentage
- Tree cover percentage
- Concrete surface percentage
- Distance to nearest cooling center
- Median income
- Distance to hospital
- Historical heat cases

## Backend API

The backend is built with FastAPI.

Run locally:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Example request:

```json
{
  "average_temperature": 35.2,
  "max_temperature": 42.1,
  "night_temperature": 31.4,
  "population_density": 18500,
  "elderly_population_pct": 18.5,
  "children_population_pct": 14.2,
  "tree_cover_pct": 6.0,
  "concrete_surface_pct": 82.0,
  "distance_to_cooling_center_km": 3.6,
  "median_income_usd": 18000,
  "hospital_distance_km": 5.2,
  "historical_heat_cases": 88
}
```

## Train And Evaluate

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python -m src.models
```

Evaluate the model:

```bash
python -m src.evaluation
```

Run tests:

```bash
pytest
```

## Model

The default model is a RandomForest classifier because it handles non-linear patterns and mixed urban-risk indicators well. The project is structured so other classifiers can be added later.

Current sample-data result:

```text
Accuracy: 87.5%
Evaluation: stratified train-test split
```

This is a starter dataset for demonstrating the workflow. With a larger real city dataset, the same structure can support stronger validation and geospatial analysis.

## Recommendation Logic

The API does not stop at prediction. It adds an action recommendation:

- `Critical`: open emergency cooling shelters and issue public-health alerts.
- `High`: expand cooling-center access and prioritize vulnerable groups.
- `Medium`: increase tree cover and monitor night-time heat.
- `Low`: maintain current heat-prevention measures.

## Future Scope

- Add real geospatial data.
- Add map visualization for priority zones.
- Compare RandomForest with XGBoost and Logistic Regression.
- Add SHAP explainability.
- Deploy the FastAPI backend.
- Create a dashboard for urban planners.

## License

This project is released under the MIT License.
