from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.llms import OpenAI

def create_agent(db_uri: str):
    db = SQLDatabase.from_uri(db_uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
    agent = create_sql_agent(llm=OpenAI(temperature=0), toolkit=toolkit)
    return agent