from src.recommendation import recommend_action, risk_score


def test_critical_recommendation_mentions_cooling_shelters():
    action = recommend_action("Critical", tree_cover_pct=5, distance_to_cooling_center_km=4)

    assert "cooling shelters" in action


def test_risk_score_increases_for_hotter_area():
    base = {
        "average_temperature": 30,
        "max_temperature": 35,
        "night_temperature": 25,
        "population_density": 7000,
        "elderly_population_pct": 10,
        "children_population_pct": 10,
        "tree_cover_pct": 30,
        "concrete_surface_pct": 40,
        "distance_to_cooling_center_km": 1,
        "median_income_usd": 50000,
        "hospital_distance_km": 1,
        "historical_heat_cases": 10,
    }
    hotter = base | {"max_temperature": 43, "night_temperature": 32, "tree_cover_pct": 4}

    assert risk_score(hotter) > risk_score(base)
