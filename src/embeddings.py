from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


def load_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en",
        model_kwargs={"device": "cuda"}  # GPU
    )
    return embeddings