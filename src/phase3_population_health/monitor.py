import pandas as pd
from sqlalchemy import create_engine

def get_at_risk_patients(db_uri):
    engine = create_engine(db_uri)
    query = """
    SELECT * FROM discharges WHERE chronic_condition = TRUE AND days_since_discharge <= 7
    """
    return pd.read_sql(query, engine)