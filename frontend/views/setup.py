import streamlit as st

def show_setup():
    st.title("🔐 Secure Setup")
    st.markdown("<p style='color: #94a3b8;'>Enter your API keys below. They are stored only in your browser's session and are never saved to disk on the server.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    with st.form("auth_setup", clear_on_submit=False):
        gemini_key = st.text_input("Gemini API Key", value=st.session_state.get("gemini_api_key", ""), type="password", help="Get from Google AI Studio")
        client_id = st.text_input("Google Client ID", value=st.session_state.get("google_client_id", ""), help="From Google Cloud Console")
        client_sec = st.text_input("Google Client Secret", value=st.session_state.get("google_client_secret", ""), type="password")
        
        if st.form_submit_button("Save Session Configuration", use_container_width=True):
            st.session_state.gemini_api_key = gemini_key
            st.session_state.google_client_id = client_id
            st.session_state.google_client_secret = client_sec
            st.success("✅ Configuration updated for this session!")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_setup()
