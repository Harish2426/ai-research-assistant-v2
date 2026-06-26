import os
from dotenv import load_dotenv

try:
    import streamlit as st
except ImportError:
    st = None

# Load .env locally
load_dotenv()


def get_secret(key, default=None):
    # First try environment variables (.env or system env)
    value = os.getenv(key)

    if value:
        return value

    # Then try Streamlit Cloud secrets
    if st is not None:
        try:
            return st.secrets[key]
        except Exception:
            pass

    return default


GEMINI_API_KEY = get_secret("GEMINI_API_KEY")

SERPER_API_KEY = get_secret("SERPER_API_KEY")

MODEL_NAME = get_secret(
    "MODEL_NAME",
    "gemini-2.0-flash"
)