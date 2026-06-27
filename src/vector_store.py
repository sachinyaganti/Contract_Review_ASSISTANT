"""
vector_store.py

Handles FAISS vector database operations.
"""

import os
import pickle
import faiss
import numpy as np


# ============================
# Vector Database Directory
# ============================

VECTOR_DB = "vector_db"

os.makedirs(VECTOR_DB, exist_ok=True)


INDEX_FILE = os.path.join(
    VECTOR_DB,
    "faiss_index.bin"
)

CHUNK_FILE = os.path.join(
    VECTOR_DB,
    "chunks.pkl"
)


# ============================
# Create Index
# ============================

def create_index(dimension):
    """
    Create a new FAISS index.
    """

    return faiss.IndexFlatL2(dimension)


# ============================
# Add Embeddings
# ============================

def add_embeddings(index, embeddings):
    """
    Add embeddings to FAISS.
    """

    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )

    index.add(embeddings)


# ============================
# Save Index
# ============================

def save_index(index):
    """
    Save FAISS index to disk.
    """

    faiss.write_index(
        index,
        INDEX_FILE
    )


# ============================
# Save Chunks
# ============================

def save_chunks(chunks):
    """
    Save original text chunks.
    """

    with open(
        CHUNK_FILE,
        "wb"
    ) as file:

        pickle.dump(
            chunks,
            file
        )


# ============================
# Load Index
# ============================

def load_index():
    """
    Load FAISS index.
    """

    if not os.path.exists(INDEX_FILE):

        raise FileNotFoundError(
            "FAISS index does not exist."
        )

    return faiss.read_index(
        INDEX_FILE
    )


# ============================
# Load Chunks
# ============================

def load_chunks():
    """
    Load chunk list.
    """

    if not os.path.exists(CHUNK_FILE):

        raise FileNotFoundError(
            "Chunk file does not exist."
        )

    with open(
        CHUNK_FILE,
        "rb"
    ) as file:

        chunks = pickle.load(file)

    return chunks


# ============================
# Search
# ============================

def search(
    index,
    query_embedding,
    top_k=5
):
    """
    Search similar vectors.
    """

    query_embedding = np.asarray(
        [query_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    return distances, indices


# ============================
# Check Database
# ============================

def database_exists():
    """
    Check whether vector database exists.
    """

    return (
        os.path.exists(INDEX_FILE)
        and
        os.path.exists(CHUNK_FILE)
    )


# ============================
# Number of Stored Vectors
# ============================

def total_vectors():

    if not database_exists():

        return 0

    index = load_index()

    return index.ntotal