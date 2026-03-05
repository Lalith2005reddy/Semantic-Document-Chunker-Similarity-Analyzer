import streamlit as st
from src.embeddings import load_embeddings
from src.chunker import semantic_chunk
from src.similarity import check_similarity

st.title("📄 Semantic Document Chunker")

embeddings = load_embeddings()

option = st.sidebar.selectbox(
    "Choose Function",
    ["Semantic Chunking", "Text Similarity"]
)

# -------- Chunking --------

if option == "Semantic Chunking":

    text = st.text_area("Enter Document", height=300)

    if st.button("Split Document"):
        chunks = semantic_chunk(text, embeddings)

        st.write(f"Total Chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):
            st.write(f"Chunk {i+1}")
            st.info(chunk)


# -------- Similarity --------

if option == "Text Similarity":

    text1 = st.text_area("Text 1")
    text2 = st.text_area("Text 2")

    if st.button("Check Similarity"):

        score = check_similarity(text1, text2, embeddings)

        percent = int(score * 100)

        st.subheader("Similarity Score")

        # Progress bar
        st.progress(percent)

        # Numeric value
        st.metric("Similarity %", f"{percent}%")

        # Interpretation
        if score > 0.8:
            st.success("Highly Similar")
        elif score > 0.5:
            st.warning("Moderately Similar")
        else:
            st.error("Low Similarity")