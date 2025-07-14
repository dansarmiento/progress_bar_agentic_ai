from pathlib import Path
from llama_index import SimpleDirectoryReader

def load_documents(folder_path: str):
    reader = SimpleDirectoryReader(input_dir=folder_path)
    docs = reader.load_data()
    return docs