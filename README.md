# 🤖 AI Research Assistant

An AI-powered Research Assistant built with **Python**, **Streamlit**, **Google Gemini**, and **ChromaDB**. It can answer general questions, perform calculations, search the web, and chat with uploaded PDF documents using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 💬 AI Chat using Google Gemini
* 📄 Chat with PDF documents (RAG)
* 🧠 Semantic Search using ChromaDB
* 🔍 Web Search Integration
* 🧮 Calculator Tool
* 📑 PDF Processing and Chunking
* 📦 Embedding Generation using Sentence Transformers
* 🎨 Interactive Streamlit Interface

---

## 🏗️ Project Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Assistant Router
   │
   ├── Calculator
   ├── Web Search
   ├── RAG
   └── Chat
         │
         ▼
    Gemini API
         ▲
         │
   ChromaDB
         ▲
         │
Embeddings
         ▲
         │
PDF → Chunking → Vector Storage
```

---

## 🛠️ Tech Stack

* Python 3.12
* Streamlit
* Google Gemini API
* ChromaDB
* Sentence Transformers
* PyPDF
* LangChain Text Splitters
* Torch
* Requests

---

## 📂 Project Structure

```
ai-research-assistant-v2/

├── app/
│   ├── assistant.py
│   ├── config.py
│   ├── models.py
│   ├── pdf_processor.py
│   ├── rag.py
│   └── router.py
│
├── database/
│   └── chroma.py
│
├── tools/
│   ├── calculator.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── pdf_reader.py
│   └── search.py
│
├── uploads/
├── streamlit_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Harish2426/ai-research-assistant-v2.git
cd ai-research-assistant-v2
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.0-flash
SERPER_API_KEY=YOUR_SERPER_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

---

## 📸 Screenshots

Add screenshots of:

* Home Screen
* PDF Upload
* Chat Interface
* RAG Responses

---

## 🔮 Future Improvements

* Multi-PDF Support
* Chat Memory
* Source Citations
* Voice Assistant
* Authentication
* Docker Deployment
* FastAPI Backend

---

## 👨‍💻 Author

**Harish**

GitHub: https://github.com/Harish2426
