from .monitor import get_at_risk_patients
from .risk_scoring import predict_risk
from .emr_extraction import extract_emr_notes

def run_workflow(rag_query_engine, db_uri):
    patients = get_at_risk_patients(db_uri)
    alerts = []

    for _, patient in patients.iterrows():
        risk = predict_risk(patient.to_frame().T)
        if risk > 0.8:
            notes = extract_emr_notes(patient['patient_id'], rag_query_engine)
            alert = f"""
            Patient ID: {patient['patient_id']}
            Risk Score: {risk:.2f}
            Notes: {notes}
            """
            alerts.append(alert)

    return alerts