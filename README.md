# Urban Heat Risk Prediction

Python backend data science project that predicts neighborhood-level heat-risk and recommends cooling actions using climate, population, and infrastructure indicators.

## Project Snapshot

Extreme heat is becoming a serious public-health challenge in cities. The impact is not equal everywhere: neighborhoods with low tree cover, dense population, high elderly population, high concrete surface, and poor access to cooling centers can face much higher risk.

This project builds a small decision-support system that classifies urban heat risk and suggests practical actions for city planners and public-health teams.

## What The Project Does

- Predicts heat-risk level: `Low`, `Medium`, `High`, or `Critical`.
- Uses a RandomForest machine learning model.
- Provides a FastAPI backend with a `/predict` endpoint.
- Returns a transparent risk score.
- Recommends an action such as opening cooling shelters, improving tree cover, or monitoring vulnerable residents.
- Includes tests, CI workflow, Dockerfile, and model evaluation output.

## Use Case

This project can help answer questions like:

- Which neighborhoods need urgent cooling support?
- Where should temporary cooling shelters be placed?
- Which zones need more trees or shaded spaces?
- Which areas should receive public-health alerts during heat waves?

## Tech Stack

| Area | Tools |
| --- | --- |
| Backend | FastAPI, Pydantic, Uvicorn |
| Data Science | Pandas, scikit-learn |
| Model | RandomForestClassifier |
| Testing | Pytest |
| Deployment Ready | Docker |
| Automation | GitHub Actions |

## Dataset

The repository includes a sample neighborhood-level dataset:

```text
data/raw/urban_heat_sample.csv
```

Features used:

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

Target:

```text
heat_risk_level
```

## Model Result

Current result on the sample dataset:

```text
Model: RandomForestClassifier
Accuracy: 87.5%
Evaluation: Stratified train-test split
Tests: 4 passed
```

Note: the included dataset is a compact sample dataset designed to demonstrate the full workflow. The same structure can be extended with larger real-world city, climate, geospatial, or public-health datasets.

## Project Structure

```text
urban_heat_risk_prediction/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- app.py
|-- Dockerfile
|-- data/
|   |-- raw/
|   |   |-- urban_heat_sample.csv
|   |-- processed/
|-- notebooks/
|   |-- README.md
|-- src/
|   |-- __init__.py
|   |-- preprocessing.py
|   |-- models.py
|   |-- evaluation.py
|   |-- recommendation.py
|-- tests/
|   |-- test_preprocessing.py
|   |-- test_recommendation.py
|-- results/
|   |-- model_metrics.json
|-- .github/
|   |-- workflows/
|       |-- ci.yml
```

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/rujpuj/urban-heat-risk-prediction.git
cd urban-heat-risk-prediction
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Train the model:

```bash
python -m src.models
```

5. Evaluate the model:

```bash
python -m src.evaluation
```

6. Run tests:

```bash
pytest
```

## Run The API

Start the FastAPI backend:

```bash
uvicorn app:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## Example API Request

Endpoint:

```text
POST /predict
```

Request body:

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

Example response:

```json
{
  "heat_risk_level": "Critical",
  "risk_score": 160.43,
  "recommended_action": "Open emergency cooling shelters, issue heat alerts, and prioritize medical outreach."
}
```

## Recommendation Logic

The model predicts risk level, and the backend adds an action layer:

| Risk Level | Recommended Action |
| --- | --- |
| Critical | Open emergency cooling shelters and issue public-health alerts |
| High | Expand cooling-center access and prioritize vulnerable groups |
| Medium | Increase tree cover and monitor night-time heat |
| Low | Maintain current heat-prevention measures |

## Docker

Build the image:

```bash
docker build -t urban-heat-risk-api .
```

Run the container:

```bash
docker run -p 8000:8000 urban-heat-risk-api
```

## Future Improvements

- Use real city-level geospatial datasets.
- Add heat-risk map visualization.
- Compare RandomForest with Logistic Regression, XGBoost, and Decision Tree.
- Add SHAP explainability for feature impact.
- Build a dashboard for urban planners.
- Deploy the FastAPI backend to a cloud platform.

## License

This project is licensed under the MIT License.

