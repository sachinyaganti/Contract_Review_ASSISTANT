"""
llm.py

Google Gemini integration for Contract Review Assistant.
"""

import os

import google.generativeai as genai

from dotenv import load_dotenv


# ======================================
# Load Environment Variables
# ======================================

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )


# ======================================
# Configure Gemini
# ======================================

genai.configure(api_key=API_KEY)


# ======================================
# Load Model
# ======================================

MODEL_NAME = "gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)


# ======================================
# Prompt Builder
# ======================================

def build_prompt(context, question):

    prompt = f"""
You are an expert Legal Contract Review Assistant.

Use ONLY the contract information provided below.

If the answer is not present in the contract,
reply exactly:

"The requested information is not available in the uploaded contract."

-------------------------------
Contract Context
-------------------------------

{context}

-------------------------------
User Question
-------------------------------

{question}

-------------------------------
Instructions
-------------------------------

1. Answer only from the contract.
2. Do not make assumptions.
3. Be concise.
4. Use bullet points where appropriate.
5. Mention if any important clause appears missing.
"""

    return prompt


# ======================================
# Generate Answer
# ======================================

def generate_answer(context, question):

    prompt = build_prompt(
        context,
        question
    )

    response = model.generate_content(
        prompt
    )

    return response.text


# ======================================
# Model Info
# ======================================

def get_model_name():

    return MODEL_NAME