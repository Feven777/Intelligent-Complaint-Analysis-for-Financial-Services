from data_loader import load_clean_data
from chunking import create_text_chunks
from embedding import load_embedding_model
from vector_store import build_vector_store
from config import TEXT_COLUMN, METADATA_COLUMNS
from config import TEXT_COLUMN, METADATA_COLUMNS, SAMPLE_SIZE


def main():
    df = load_clean_data()
    if SAMPLE_SIZE is not None:
        df = df.sample(n=SAMPLE_SIZE, random_state=42)
    embedding_model = load_embedding_model()

    all_chunks = []
    all_metadata = []

    for _, row in df.iterrows():
        chunks = create_text_chunks(row[TEXT_COLUMN])

        metadata = {
            col: row[col] for col in METADATA_COLUMNS
        }

        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadata.append(metadata)

    build_vector_store(all_chunks, all_metadata, embedding_model)


if __name__ == "__main__":
    main()
