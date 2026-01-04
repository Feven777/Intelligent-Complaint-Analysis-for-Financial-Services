DATA_PATH = "data/processed/complaints_clean.csv"

TEXT_COLUMN = "Consumer complaint narrative"

METADATA_COLUMNS = [
    "Product",
    "Company",
    "Issue",
    "Date received"
]

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

VECTOR_STORE_DIR = "vector_store/chroma"
SAMPLE_SIZE = 10_000
