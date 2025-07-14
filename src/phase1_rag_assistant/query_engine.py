from llama_index import VectorStoreIndex, ServiceContext
from .embed import get_embedding_model
from .vector_store import create_vector_store

def build_query_engine(documents):
    embedding_model = get_embedding_model()
    service_context = ServiceContext.from_defaults(embed_model=embedding_model)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    return index.as_query_engine()