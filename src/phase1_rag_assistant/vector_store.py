from llama_index.vector_stores import ChromaVectorStore

def create_vector_store(persist_dir="chroma_db"):
    return ChromaVectorStore(persist_dir=persist_dir)