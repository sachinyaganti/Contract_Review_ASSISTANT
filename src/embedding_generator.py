"""
embedding_generator.py

Generates embeddings using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer
import numpy as np


# ===========================================
# Load Embedding Model (Loads Only Once)
# ===========================================

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


# ===========================================
# Generate Embeddings
# ===========================================

def generate_embeddings(texts):
    """
    Generate embeddings for a list of texts.

    Parameters
    ----------
    texts : list[str]

    Returns
    -------
    numpy.ndarray
    """

    if isinstance(texts, str):
        texts = [texts]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    return embeddings.astype(np.float32)


# ===========================================
# Generate Single Embedding
# ===========================================

def generate_query_embedding(query):
    """
    Generate embedding for one query.
    """

    return generate_embeddings(query)[0]


# ===========================================
# Embedding Dimension
# ===========================================

def get_embedding_dimension():
    """
    Returns embedding dimension.
    """

    return model.get_sentence_embedding_dimension()


# ===========================================
# Model Information
# ===========================================

def get_model_name():

    return MODEL_NAME