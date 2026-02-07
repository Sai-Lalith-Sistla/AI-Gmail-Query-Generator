import streamlit as st
import requests
from utils.api_client import BACKEND_URL, get_auth_headers, check_auth

def show_queries():
    st.title("🔍 Search Query Generator")
    
    try:
        tags = requests.get(f"{BACKEND_URL}/api/tags").json()
    except:
        tags = []

    if not tags:
        st.warning("Please define focus tags in the 'Tags' manager first.")
    else:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        selected_tags = st.multiselect("Select Tags to Group", tags)
        if st.button("Create Intelligent Search Key", use_container_width=True, type="primary"):
            if check_auth():
                with st.spinner("Gemini is analyzing tags..."):
                    try:
                        resp = requests.post(f"{BACKEND_URL}/api/generate-query", json={"tags": selected_tags}, headers=get_auth_headers())
                        if resp.status_code == 200:
                            query = resp.json().get('query')
                            st.markdown(f"""
                            <div style='background: rgba(0,0,0,0.2); padding: 20px; border-radius: 12px; border: 1px dashed rgba(255,255,255,0.2); margin-top: 20px;'>
                                <p style='color: #94a3b8; font-size: 0.8rem; margin-bottom: 8px;'>GMAIL SEARCH PARAMETER:</p>
                                <code style='font-size: 1.2rem; color: #4ade80;'>{query}</code>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error(f"Error: {resp.text}")
                    except Exception as e:
                        st.error(f"Connection Error: {e}")
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_queries()
