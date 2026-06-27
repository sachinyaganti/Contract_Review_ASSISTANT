from src.llm import generate_answer

context = """
Termination:
Either party may terminate the agreement
with 30 days written notice.

Confidentiality:
The employee shall not disclose company secrets.
"""

question = "What is the termination clause?"

answer = generate_answer(
    context,
    question
)

print(answer)