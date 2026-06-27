from src.rag_pipeline import ContractRAG

pipeline = ContractRAG()

pipeline.process_document(
    "uploads/Employment.pdf"
)

result = pipeline.ask(
    "What is the termination clause?"
)

print(result["answer"])