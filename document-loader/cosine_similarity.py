import math


def cosine_similarity(vector_a, vector_b):

    # Check vector dimensions
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions")

    if len(vector_a) == 0:
        raise ValueError("Vectors cannot be empty")

    # Calculate dot product
    dot_product = 0

    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]

    # Calculate magnitude of vector A
    magnitude_a = 0

    for value in vector_a:
        magnitude_a += value ** 2

    magnitude_a = math.sqrt(magnitude_a)

    # Calculate magnitude of vector B
    magnitude_b = 0

    for value in vector_b:
        magnitude_b += value ** 2

    magnitude_b = math.sqrt(magnitude_b)

    # Handle zero vectors
    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot calculate similarity for zero vectors")

    # Calculate cosine similarity
    similarity = dot_product / (magnitude_a * magnitude_b)

    return similarity


if __name__ == "__main__":

    vector_a = [1, 2, 3]
    vector_b = [2, 3, 4]

    result = cosine_similarity(vector_a, vector_b)

    print("Cosine Similarity:", result)