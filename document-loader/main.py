# from document_loader import load_document


# if __name__ == "__main__":

#     file_path = input("Enter document path: ")

#     try:
#         extracted_text = load_document(file_path)

#         print("\n========== EXTRACTED TEXT ==========\n")
#         print(extracted_text)

#         print("\n=========== SUMMARY ===========")
#         print("Document loaded successfully!")

#     except Exception as e:
#         print(f"Error: {e}")
# ------------------------------------------------------------------------

# from document_loader import load_document
# from text_chunker import chunk_text


# if __name__ == "__main__":

#     file_path = "document-loader\data\sample.txt"

#     # Step 1: Load document
#     text = load_document(file_path)

#     # Step 2: Split document into chunks
#     chunks = chunk_text(
#         text,
#         chunk_size=500,
#         overlap=100
#     )

#     # Step 3: Print chunks
#     for i, chunk in enumerate(chunks):

#         print(f"\nChunk {i + 1}")
#         print("-" * 50)
#         print(chunk)

#     print("\nTotal chunks:", len(chunks))

#--------------------------------------------------------------------------
# from document_loader import load_document
# from text_chunker import chunk_text
# from embedding_generator import (
#     generate_document_embeddings,
#     generate_query_embedding
# )


# if __name__ == "__main__":

#     # 1. Load document
#     file_path = "document-loader\data\sample.txt"

#     text = load_document(file_path)

#     # 2. Chunk document
#     chunks = chunk_text(
#         text,
#         chunk_size=500,
#         overlap=100
#     )
#     for i, chunk in enumerate(chunks):
#                 print(f"\nChunk {i + 1}:")
#                 print(chunk)
#     print("Total chunks:", len(chunks))

#     # 3. Generate document embeddings
#     doc_embeddings = generate_document_embeddings(chunks)

#     # 4. Generate query embedding
#     query = "What is the company's leave policy?"

#     query_embedding = generate_query_embedding(query)

#     print("Document embeddings:", doc_embeddings.shape)
#     print("Query embedding:", query_embedding.shape)

#------------------------------------------------------------------------
# from embedding_generator import (
#     generate_document_embeddings,
#     generate_query_embedding
# )

# from cosine_similarity import cosine_similarity


# documents = [
#     "Python is a programming language",
#     "LangChain builds LLM applications",
#     "Pinecone is a vector database"
# ]

# query = "What is Python?"


# # Generate embeddings
# doc_embeddings = generate_document_embeddings(documents)
# query_embedding = generate_query_embedding(query)


# Calculate similarity
# for i, doc_embedding in enumerate(doc_embeddings):

#     score = cosine_similarity(
#         query_embedding.tolist(),
#         doc_embedding.tolist()
#     )

#     print(f"\nDocument: {documents[i]}")
#     print(f"query:{query}")
#     print(f"Similarity Score: {score:.4f}")
#---------------------------------------------------------------------------------
from document_loader import load_document
from text_chunker import chunk_text

from embedding_generator import (
    generate_document_embeddings,
    generate_query_embedding
)

from semantic_search import semantic_search


# 1. Load document
text = load_document("document-loader\data\sample.txt")


# 2. Chunk document
chunks = chunk_text(
    text,
    chunk_size=500,
    overlap=100
)


# 3. Generate document embeddings
document_vectors = generate_document_embeddings(chunks)


# 4. Generate query embedding
query = "What is the company leave policy?"

query_vector = generate_query_embedding(query)


# 5. Perform semantic search
results = semantic_search(
    query_vector.tolist(),
    document_vectors.tolist(),
    chunks,
    top_k=3
)


# 6. Display results
for result in results:

    print("\nDocument:", result["document"])
    print("Similarity:", round(result["score"], 4))