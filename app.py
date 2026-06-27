import os
import tempfile
import streamlit as st

from src.rag_pipeline import ContractRAG

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Contract Review Assistant",
    page_icon="📑",
    layout="wide"
)

# -------------------------------------------------------
# Session State
# -------------------------------------------------------

if "pipeline" not in st.session_state:
    st.session_state.pipeline = ContractRAG()

if "processed" not in st.session_state:
    st.session_state.processed = False

if "info" not in st.session_state:
    st.session_state.info = {}

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("📑 Contract Review Assistant")

st.write(
    """
Upload a PDF or DOCX contract and ask AI-powered questions
using Retrieval-Augmented Generation (RAG).
"""
)

st.divider()

# -------------------------------------------------------
# Upload Section
# -------------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose Contract",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success("File Uploaded Successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**File Name**")
        st.write(uploaded_file.name)

    with col2:
        st.write("**File Size**")
        st.write(f"{uploaded_file.size/(1024*1024):.2f} MB")

    if st.button("🚀 Process Contract"):

        with st.spinner("Processing contract..."):

            try:

                suffix = os.path.splitext(uploaded_file.name)[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as tmp:

                    tmp.write(uploaded_file.getbuffer())

                    temp_path = tmp.name

                info = st.session_state.pipeline.process_document(
                    temp_path
                )

                st.session_state.info = info
                st.session_state.processed = True

                os.remove(temp_path)

                st.success("Contract processed successfully!")

            except Exception as e:

                st.session_state.processed = False

                st.error(f"Processing failed:\n\n{e}")

# -------------------------------------------------------
# Statistics
# -------------------------------------------------------

if st.session_state.processed:

    st.divider()

    st.subheader("📊 Contract Statistics")

    info = st.session_state.info

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Characters",
        info.get("characters", 0)
    )

    c2.metric(
        "Chunks",
        info.get("chunks", 0)
    )

    c3.metric(
        "Embedding Size",
        info.get("dimension", 0)
    )

    c4.metric(
        "Vectors",
        info.get("vectors", 0)
    )

    st.divider()

    # -------------------------------------------------------
    # Ask AI
    # -------------------------------------------------------

    st.subheader("🤖 Ask AI")

    question = st.text_input(
        "Ask a question about the uploaded contract"
    )

    if st.button("Ask AI"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is reviewing the contract..."):

                try:

                    result = st.session_state.pipeline.ask(
                        question
                    )

                    st.success(result["answer"])

                    if len(result["retrieved_chunks"]) > 0:

                        st.divider()

                        st.subheader("📄 Supporting Contract Sections")

                        for chunk in result["retrieved_chunks"]:

                            with st.expander(
                                f"Chunk {chunk['chunk_id']}"
                            ):

                                st.write(chunk["text"])

                                st.caption(
                                    f"Similarity Distance: {chunk['distance']:.4f}"
                                )

                    else:

                        st.info(
                            "No relevant contract sections were found."
                        )

                except Exception as e:

                    st.error(f"AI Error:\n\n{e}")

else:

    st.info(
        "Upload a contract and click 'Process Contract' to begin."
    )