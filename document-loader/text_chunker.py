def chunk_text(text:str,chunk_size:int=50,overlap:int=10)->list:
    """
    Split text into smaller chunks with configurable overlap.
    """

    # Validate input
    if chunk_size<0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if not text:
        return []

    chunks=[]
    start=0
    step = chunk_size - overlap

    while start<=len(text):
        end=start+chunk_size
        chunk=text[start:end]

        chunks.append(chunk)

        start+=step

    return chunks

if __name__ == "__main__":
     

     text = """
            Python is a programming language.
            LangChain helps build LLM applications.
             RAG improves information retrieval.
             Vector databases store embeddings.
            """

     chunks = chunk_text(
        text,
        chunk_size=50,
        overlap=10
        )
     for i, chunk in enumerate(chunks):
            print(f"\nChunk {i + 1}:")
            print(chunk)
