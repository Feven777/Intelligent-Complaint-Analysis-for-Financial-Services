from src.retrieval import semantic_search

query = "I was charged fees on my credit card that I did not authorize"
results = semantic_search(query, k=5)

for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content[:300])
    print("Metadata:", doc.metadata)
