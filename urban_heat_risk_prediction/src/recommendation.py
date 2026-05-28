def recommend_action(risk_level: str, tree_cover_pct: float, distance_to_cooling_center_km: float) -> str:
    """Return a practical city-planning action for the predicted risk level."""
    risk = risk_level.lower()

    if risk == "critical":
        return "Open emergency cooling shelters, issue heat alerts, and prioritize medical outreach."
    if risk == "high":
        if distance_to_cooling_center_km > 2.5:
            return "Expand cooling-center access and run targeted awareness for vulnerable residents."
        return "Increase public cooling points and monitor elderly residents during heat waves."
    if risk == "medium":
        if tree_cover_pct < 20:
            return "Increase tree cover and add shaded public spaces."
        return "Monitor night-time heat and maintain public hydration points."
    return "Maintain existing heat-prevention measures and continue routine monitoring."


def risk_score(features: dict) -> float:
    """Calculate a transparent heuristic score for quick explanation."""
    score = 0.0
    score += max(features["max_temperature"] - 34, 0) * 4
    score += max(features["night_temperature"] - 25, 0) * 3
    score += features["population_density"] / 2500
    score += features["elderly_population_pct"] * 1.2
    score += features["children_population_pct"] * 0.5
    score += max(30 - features["tree_cover_pct"], 0) * 1.1
    score += features["concrete_surface_pct"] * 0.4
    score += features["distance_to_cooling_center_km"] * 5
    score += features["hospital_distance_km"] * 2
    score += features["historical_heat_cases"] * 0.35
    score -= min(features["median_income_usd"] / 10000, 8)
    return round(score, 2)
