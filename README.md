# 📑 AI Contract Review Assistant

> An AI-powered Contract Review Assistant that leverages **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Search**, **Sentence Transformers**, **Google Gemini**, and **Streamlit** to analyze contracts, answer legal questions, and provide intelligent insights from uploaded PDF and DOCX documents.

---

## 🚀 Live Demo

🔗 **Application:**

> *https://contractreviewassistant-ve6b2fuvnbwu4wg7vqpmm8.streamlit.app/*

---

## 📌 Project Overview

The AI Contract Review Assistant enables users to upload legal contracts and interact with them using natural language. Instead of manually reading lengthy agreements, users can ask questions such as:

- What is the termination clause?
- Is there a confidentiality agreement?
- What are the payment terms?
- What is the notice period?
- Are there any non-compete clauses?

The system retrieves the most relevant sections using semantic search and generates accurate AI-powered responses using Google's Gemini model.

---

# ✨ Features

- 📄 Upload PDF and DOCX contracts
- 📝 Automatic text extraction
- ✂️ Intelligent text chunking
- 🧠 Semantic embeddings using Sentence Transformers
- ⚡ High-speed vector search using FAISS
- 🤖 AI-powered contract question answering using Google Gemini
- 🔍 Retrieval-Augmented Generation (RAG)
- 📊 Processing statistics dashboard
- 📑 Source chunk visualization
- 🎯 Semantic search instead of keyword matching
- 🌐 Streamlit web interface
- ☁️ Ready for Streamlit Cloud deployment

---

# 🏗️ System Architecture

```text
                     User

                      │

                      ▼

            Upload Contract

                      │

                      ▼

            Text Extraction

                      │

                      ▼

              Text Chunking

                      │

                      ▼

        Sentence Transformer

             Embeddings

                      │

                      ▼

              FAISS Index

                      │

                      ▼

             User Question

                      │

                      ▼

           Query Embedding

                      │

                      ▼

           Semantic Retrieval

                      │

                      ▼

         Retrieved Chunks

                      │

                      ▼

          Google Gemini AI

                      │

                      ▼

             AI Response
```

---

# 📂 Project Structure

```
ContractReviewAssistant/

│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
│
├── src/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embedding_generator.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── llm.py
│
├── uploads/
│
└── vector_db/
```

---

# 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / NLP

- Google Gemini
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

### Vector Database

- FAISS

### Document Processing

- PyPDF
- python-docx

### Machine Learning

- PyTorch

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ContractReviewAssistant.git

cd ContractReviewAssistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named:

```
.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

## AI Chat

```
Question:

What is the termination clause?

↓

AI Response

↓

Supporting Contract Sections
```

---

# 🧠 How It Works

### Step 1

Upload a PDF or DOCX contract.

↓

### Step 2

The application extracts the text.

↓

### Step 3

The text is divided into overlapping chunks.

↓

### Step 4

Sentence Transformer generates embeddings.

↓

### Step 5

Embeddings are stored in a FAISS vector database.

↓

### Step 6

User asks a natural language question.

↓

### Step 7

The query is converted into an embedding.

↓

### Step 8

FAISS retrieves the most relevant chunks.

↓

### Step 9

Retrieved context is sent to Gemini.

↓

### Step 10

Gemini generates an accurate response grounded in the uploaded contract.

---

# 📊 Example Questions

- What is the termination clause?
- What are the payment terms?
- Is confidentiality included?
- What is the governing law?
- Does the contract contain a non-compete clause?
- What are the responsibilities of the employee?
- What happens during probation?
- What are the working hours?
- Is severance compensation provided?
- How are disputes resolved?

---

# 🎯 Future Enhancements

- Risk Clause Detection
- Missing Clause Identification
- AI-generated Contract Summary
- Clause Risk Scoring
- Downloadable PDF Review Report
- Multi-document Comparison
- Chat History
- User Authentication
- Cloud Database Integration
- Enterprise Dashboard

---

# 📈 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- Natural Language Processing
- Information Retrieval
- Streamlit Application Development
- Python Development
- FAISS
- Sentence Transformers
- Google Gemini API Integration

---

# 👨‍💻 Author

**Sachin Yaganti**

B.Tech Computer Science Engineering

KL University

GitHub: (https://github.com/sachinyaganti)

LinkedIn: (https://www.linkedin.com/in/yaganti-deepak-sachin-sai-chowdary-a374482a5/?skipRedirect=true)

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

💡 Contribute improvements

📢 Share your feedback
