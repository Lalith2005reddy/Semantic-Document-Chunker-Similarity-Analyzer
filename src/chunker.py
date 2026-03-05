from langchain_experimental.text_splitter import SemanticChunker

def semantic_chunk(text,embeddings):

    if not text.strip():
        return []
    
    text_splitter = SemanticChunker(
        embeddings,
        breakpoint_threshold_type="standard_deviation",
        breakpoint_threshold_amount=0.5,
    )

    docs = text_splitter.create_documents([text])

    chunks = [doc.page_content for doc in docs]

    return chunks