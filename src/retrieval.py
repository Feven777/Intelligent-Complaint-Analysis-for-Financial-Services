from langchain_chroma import Chroma
from .embedding import load_embedding_model
from .config import VECTOR_STORE_DIR


def load_vector_store():
    """
    Load the persisted Chroma vector store.
    """
    embedding_model = load_embedding_model()

    vector_store = Chroma(
        persist_directory=VECTOR_STORE_DIR,
        embedding_function=embedding_model
    )
    return vector_store


def semantic_search(query: str, k: int = 5):
    """
    Perform semantic similarity search.
    """
    vector_store = load_vector_store()
    results = vector_store.similarity_search(query, k=k)
    return results
