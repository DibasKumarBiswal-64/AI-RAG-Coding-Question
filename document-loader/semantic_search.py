from cosine_similarity import cosine_similarity


def semantic_search(
    query_vector,
    document_vectors,
    documents,
    top_k=3
):
    """
    Perform semantic search using cosine similarity.
    """

    # Validate input
    if len(documents) != len(document_vectors):
        raise ValueError(
            "Number of documents and document vectors must match"
        )

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    if len(query_vector) == 0:
        raise ValueError("Query vector cannot be empty")

    if not documents:
        return []

    # Store similarity scores
    scores = []

    # Calculate similarity for each document
    for i in range(len(document_vectors)):

        score = cosine_similarity(
            query_vector,
            document_vectors[i]
        )

        scores.append((i, score))

    # Sort documents by similarity score
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Return Top-K documents
    results = []

    for index, score in scores[:top_k]:

        results.append({
            "document": documents[index],
            "score": score,
            "index": index
        })

    return results