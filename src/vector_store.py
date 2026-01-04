from langchain_chroma import Chroma
from .config import VECTOR_STORE_DIR


def build_vector_store(chunks, metadatas, embedding_model):
    vector_store = Chroma.from_texts(
        texts=chunks,
        metadatas=metadatas,
        embedding=embedding_model,
        persist_directory=VECTOR_STORE_DIR
    )
    return vector_store
