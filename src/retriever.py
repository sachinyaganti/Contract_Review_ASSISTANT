"""
retriever.py

Handles semantic retrieval from the FAISS vector database.
"""

from src.embedding_generator import generate_embeddings
from src.vector_store import (
    load_index,
    load_chunks,
    search
)


class ContractRetriever:

    def __init__(self):

        self.index = load_index()

        self.chunks = load_chunks()

    def retrieve(self, query, top_k=5):
        """
        Retrieve the most relevant chunks.

        Parameters
        ----------
        query : str
            User question.

        top_k : int
            Number of chunks to retrieve.

        Returns
        -------
        list
            Retrieved chunks with distance score.
        """

        query_embedding = generate_embeddings([query])[0]

        distances, indices = search(
            self.index,
            query_embedding,
            top_k
        )

        results = []

        for distance, idx in zip(
            distances[0],
            indices[0]
        ):

            if idx < len(self.chunks):

                results.append(
                    {
                        "chunk_id": idx + 1,
                        "distance": float(distance),
                        "text": self.chunks[idx]
                    }
                )

        return results


retriever = ContractRetriever()


def retrieve_chunks(
    query,
    top_k=5
):
    """
    Simple wrapper function.
    """

    return retriever.retrieve(
        query,
        top_k
    )