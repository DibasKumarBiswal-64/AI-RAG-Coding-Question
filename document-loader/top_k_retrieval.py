import heapq


def top_k_retrieval(documents, similarity_scores, top_k):

    if len(documents) != len(similarity_scores):
        raise ValueError("Documents and scores must have the same length")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    # Store document index and similarity score
    scores = []

    for i in range(len(documents)):
        scores.append((i, similarity_scores[i]))

    # Retrieve only top K scores
    top_results = heapq.nlargest(
        top_k,
        scores,
        key=lambda x: x[1]
    )

    results = []

    for index, score in top_results:
        results.append({
            "document": documents[index],
            "score": score
        })

    return results


if __name__ == "__main__":

    documents = [
        "Python is a programming language.",
        "LangChain helps build LLM applications.",
        "Pinecone is a vector database.",
        "Python supports machine learning.",
        "FastAPI is used to build APIs."
    ]

    similarity_scores = [0.72, 0.95, 0.81, 0.98, 0.65]

    results = top_k_retrieval(
        documents,
        similarity_scores,
        top_k=3
    )

    for result in results:
        print(result)