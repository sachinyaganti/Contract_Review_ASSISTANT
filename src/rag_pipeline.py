"""
rag_pipeline.py

Main RAG pipeline.
"""

from src.document_loader import extract_text
from src.text_chunker import chunk_text

from src.embedding_generator import (
    generate_embeddings,
    get_embedding_dimension
)

from src.vector_store import (
    create_index,
    add_embeddings,
    save_index,
    save_chunks
)

from src.retriever import retrieve_chunks
from src.llm import generate_answer


class ContractRAG:

    def __init__(self):

        self.text = ""
        self.chunks = []
        self.embeddings = None
        self.index = None

    #####################################################
    # Process Uploaded Contract
    #####################################################

    def process_document(self, file_path):

        self.text = extract_text(file_path)

        self.chunks = chunk_text(
            self.text,
            chunk_size=500,
            overlap=100
        )

        self.embeddings = generate_embeddings(
            self.chunks
        )

        dimension = get_embedding_dimension()

        self.index = create_index(dimension)

        add_embeddings(
            self.index,
            self.embeddings
        )

        save_index(self.index)

        save_chunks(self.chunks)

        return {

            "characters": len(self.text),

            "chunks": len(self.chunks),

            "dimension": dimension,

            "vectors": self.index.ntotal
        }

    #####################################################
    # Semantic Retrieval
    #####################################################

    def retrieve(
        self,
        question,
        top_k=5
    ):

        try:

            return retrieve_chunks(
                question,
                top_k
            )

        except FileNotFoundError:

            return []

    #####################################################
    # AI Answer
    #####################################################

    def ask(
        self,
        question,
        top_k=5
    ):

        retrieved = self.retrieve(
            question,
            top_k
        )

        if len(retrieved) == 0:

            return {

                "answer":
                "Please upload and process a contract before asking questions.",

                "retrieved_chunks": []
            }

        context = "\n\n".join(
            item["text"] for item in retrieved
        )

        answer = generate_answer(
            context,
            question
        )

        return {

            "answer": answer,

            "retrieved_chunks": retrieved
        }