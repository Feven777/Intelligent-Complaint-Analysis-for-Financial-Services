from src.retrieval import semantic_search


def generate_answer(query: str, k: int = 5):
    """
    Retrieval-only RAG answer generator.

    Args:
        query (str): User question
        k (int): Number of similar documents to retrieve

    Returns:
        answer (str): Generated response based on retrieved documents
        docs (List[Document]): Source documents used
    """

    # 1. Retrieve top-k semantically similar complaint documents
    docs = semantic_search(query, k=k)

    # 2. Handle case where no documents are found
    if not docs:
        return (
            "No relevant complaints were found for your query. "
            "Please try rephrasing your question.",
            []
        )

    # 3. Build a clear, explainable response from retrieved documents
    answer_lines = []
    answer_lines.append(
        "Based on similar historical consumer complaints, here are the most relevant findings:\n"
    )

    for idx, doc in enumerate(docs[:3], start=1):
        text_snippet = doc.page_content.strip().replace("\n", " ")
        text_snippet = text_snippet[:300] + "..." if len(text_snippet) > 300 else text_snippet

        product = doc.metadata.get("Product", "Unknown Product")
        issue = doc.metadata.get("Issue", "Unknown Issue")
        company = doc.metadata.get("Company", "Unknown Company")

        answer_lines.append(
            f"{idx}. Complaint related to **{product}** involving **{company}**.\n"
            f"   Issue: {issue}\n"
            f"   Summary: {text_snippet}\n"
        )

    answer = "\n".join(answer_lines)

    # 4. Return answer and full source documents for UI display
    return answer, docs
