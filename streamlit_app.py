import streamlit as st

from app.assistant import assistant
from app.pdf_processor import pdf_processor

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# Title
# =====================================

st.title("🤖 AI Research Assistant")

st.markdown(
    """
Ask questions, upload PDFs and chat with your documents.

Supported Tools:

- 💬 Chat
- 🧮 Calculator
- 🌐 Web Search
- 📄 RAG (PDF Question Answering)
"""
)

st.divider()

# =====================================
# Sidebar
# =====================================

st.sidebar.title("📄 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Processing PDF..."):

        try:

            chunks = pdf_processor.process(uploaded_file)

            st.sidebar.success(
                f"PDF Indexed Successfully!\n\nChunks Created: {chunks}"
            )

        except Exception as e:

            st.sidebar.error(str(e))

# =====================================
# Chat History
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================
# Chat Input
# =====================================

question = st.chat_input(
    "Ask me anything..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = assistant.get_response(question)

            except Exception as e:

                answer = f"Error: {e}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )