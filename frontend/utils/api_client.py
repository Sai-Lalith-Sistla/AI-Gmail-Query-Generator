import streamlit as st

BACKEND_URL = "http://localhost:5000"

def get_auth_headers():
    return {
        "X-Gemini-Key": st.session_state.get("gemini_api_key", ""),
        "X-Google-Client-Id": st.session_state.get("google_client_id", ""),
        "X-Google-Client-Secret": st.session_state.get("google_client_secret", "")
    }

def check_auth():
    if not st.session_state.get("gemini_api_key"):
        st.warning("⚠️ Setup Required: Please configure your API keys in the Setup page.")
        return False
    return True
