import os
import streamlit as st

from src.rag_pipeline import ContractRAG

# -----------------------------
# Streamlit Configuration
# -----------------------------

st.set_page_config(
    page_title="Contract Review Assistant",
    page_icon="📑",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "pipeline" not in st.session_state:
    st.session_state.pipeline = ContractRAG()

if "processed" not in st.session_state:
    st.session_state.processed = False

# -----------------------------
# Title
# -----------------------------

st.title("📑 Contract Review Assistant")

st.markdown(
"""
Upload your contract and ask AI questions using
Retrieval-Augmented Generation (RAG).
"""
)

st.divider()

# -----------------------------
# Upload
# -----------------------------

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["pdf","docx"]
)

if uploaded_file:

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path,"wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success("Contract Uploaded")

    col1,col2=st.columns(2)

    with col1:

        st.write(
            "**File Name**",
            uploaded_file.name
        )

    with col2:

        st.write(
            "**File Size**",
            f"{uploaded_file.size/(1024*1024):.2f} MB"
        )

    if st.button("Process Contract"):

        with st.spinner(
            "Processing..."
        ):

            info = st.session_state.pipeline.process_document(
                file_path
            )

            st.session_state.processed=True

            st.session_state.info=info

# -----------------------------
# Processing Stats
# -----------------------------

if st.session_state.processed:

    st.divider()

    st.success("Contract Processed Successfully")

    info=st.session_state.info

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Characters",
        info["characters"]
    )

    c2.metric(
        "Chunks",
        info["chunks"]
    )

    c3.metric(
        "Embedding Size",
        info["dimension"]
    )

    c4.metric(
        "Vectors",
        info["vectors"]
    )

    st.divider()

    # -----------------------------
    # AI Question
    # -----------------------------

    st.header("🤖 Ask AI")

    question=st.text_input(
        "Ask anything about your contract"
    )

    if st.button("Ask AI"):

        if question.strip()=="":

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Gemini is analyzing your contract..."
            ):

                result=st.session_state.pipeline.ask(
                    question
                )

            st.subheader("🤖 AI Answer")

            st.success(
                result["answer"]
            )

            st.divider()

            st.subheader(
                "📄 Supporting Contract Sections"
            )

            for chunk in result[
                "retrieved_chunks"
            ]:

                with st.expander(
                    f"Chunk {chunk['chunk_id']}"
                ):

                    st.write(
                        chunk["text"]
                    )

                    st.caption(
                        f"Distance : {chunk['distance']:.4f}"
                    )