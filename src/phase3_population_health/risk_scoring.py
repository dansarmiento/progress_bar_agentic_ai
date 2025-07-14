import joblib
import pandas as pd

model = joblib.load("models/readmission_risk/model.pkl")

def predict_risk(patient_df: pd.DataFrame) -> float:
    return model.predict_proba(patient_df)[:, 1][0]  # risk score