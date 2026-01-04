# src/embedding.py

from langchain.embeddings import HuggingFaceEmbeddings
from .config import EMBEDDING_MODEL_NAME


def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
