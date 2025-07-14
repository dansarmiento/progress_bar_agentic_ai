def extract_emr_notes(patient_id, rag_query_engine):
    question = f"Summarize clinical history for patient ID {patient_id}"
    return rag_query_engine.query(question)