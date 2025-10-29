import os
import pickle
from typing import List, Dict

import numpy as np


def _load_pickle(filename: str):
    here = os.path.dirname(__file__)
    path = os.path.join(here, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required model file not found: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)


def _confidence_label(score: float) -> str:
    if score >= 0.8:
        return "Very High"
    if score >= 0.6:
        return "High"
    if score >= 0.4:
        return "Moderate"
    return "Low"


def predict_careers(assessment_data: Dict, top_k: int = 5) -> List[Dict]:
    """Load ML artifacts and produce career predictions.

    Expects pickles in the same folder as this file:
      - trained_model.pkl
      - label_encoder.pkl
      - education_encoder.pkl
      - work_style_encoder.pkl
      - skills_list.pkl
      - interests_list.pkl  (optional)

    assessment_data should be a dict with keys used elsewhere in the project,
    for example: { 'skills': [...], 'interests': [...], 'education': '...', 'work_style': '...' }

    Returns a list of dicts with the keys the code expects in services.create_assessment_with_recommendations
    (career_name, match_score, confidence_level, rank, matching_skills, missing_skills, completeness_percent).
    """

    # Load artifacts
    model = _load_pickle("trained_model.pkl")
    label_encoder = _load_pickle("label_encoder.pkl")
    education_encoder = _load_pickle("education_encoder.pkl")
    work_style_encoder = _load_pickle("work_style_encoder.pkl")
    skills_list = _load_pickle("skills_list.pkl")
    try:
        interests_list = _load_pickle("interests_list.pkl")
    except FileNotFoundError:
        interests_list = None

    # Prepare feature vector in the same order used during training
    # training_assests.py used: ["education_encoded", "work_style_encoded", "interest_encoded"] + all_skills
    education = assessment_data.get("education", "")
    work_style = assessment_data.get("work_style", "")
    # For interests, the training used a single interest value; take first if list
    interests = assessment_data.get("interests")
    interest_val = ""
    if isinstance(interests, (list, tuple)) and len(interests) > 0:
        interest_val = interests[0]
    elif isinstance(interests, str):
        interest_val = interests

    # Encode categorical fields. If unseen value, try to handle gracefully.
    try:
        education_encoded = int(education_encoder.transform([education])[0])
    except Exception:
        # fallback to 0 if unseen
        education_encoded = 0
    try:
        work_style_encoded = int(work_style_encoder.transform([work_style])[0])
    except Exception:
        work_style_encoded = 0
    try:
        if interests_list is not None:
            interest_encoded = 0
            if interest_val in interests_list:
                # if interests_list was saved as the encoder's classes, try to transform
                try:
                    interest_encoded = int(education_encoder.transform([interest_val])[0])
                except Exception:
                    interest_encoded = 0
            else:
                interest_encoded = 0
        else:
            interest_encoded = 0
    except Exception:
        interest_encoded = 0

    # Build skill features
    user_skills = set(assessment_data.get("skills") or [])
    skill_features = [1 if skill in user_skills else 0 for skill in skills_list]

    feature_vector = [education_encoded, work_style_encoded, interest_encoded] + skill_features
    X = np.array(feature_vector, dtype=float).reshape(1, -1)

    # Predict probabilities if available
    try:
        proba = model.predict_proba(X)[0]
        # proba aligns with label_encoder.classes_
        indices = np.argsort(proba)[::-1][:top_k]
        scores = proba[indices]
        classes = label_encoder.inverse_transform(indices)
    except Exception:
        # fallback to single predict (no probability)
        pred = model.predict(X)[0]
        classes = label_encoder.inverse_transform([pred])
        scores = [1.0]

    results = []
    for rank, (cls, score) in enumerate(zip(classes, scores), start=1):
        matching_skills = [s for s in skills_list if s in user_skills]
        missing_skills = [s for s in skills_list if s not in user_skills]
        completeness = 0.0
        try:
            completeness = round((len(matching_skills) / max(1, len(skills_list))) * 100, 2)
        except Exception:
            completeness = 0.0

        results.append({
            "career_name": str(cls),
            "match_score": float(round(float(score) * 100, 2)),
            "confidence_level": _confidence_label(float(score)),
            "rank": rank,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills[:10],
            "completeness_percent": completeness,
        })

    return results
