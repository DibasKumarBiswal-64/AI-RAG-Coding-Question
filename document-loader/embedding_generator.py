from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_document_embeddings(documents: list[str]):
    """
    Generate embeddings for multiple documents.
    """

    if not documents:
        return []

    embeddings = model.encode(
        documents,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings


def generate_query_embedding(query: str):
    """
    Generate embedding for a user query.
    """

    if not query or not query.strip():
        raise ValueError("Query cannot be empty")

    embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding


if __name__ == "__main__":

    documents = [
        "Python is a programming language.",
        "LangChain helps developers build LLM applications.",
        "Vector databases store numerical embeddings."
    ]

    query = "What is Python?"

    # Generate document embeddings
    doc_embeddings = generate_document_embeddings(documents)

    # Generate query embedding
    query_embedding = generate_query_embedding(query)

    print("Document Embeddings Shape:", doc_embeddings.shape)
    print("Query Embedding Shape:", query_embedding.shape)

    print("\nDocument Embedding:")
    print(doc_embeddings[0])

    print("\nQuery Embedding:")
    print(query_embedding)