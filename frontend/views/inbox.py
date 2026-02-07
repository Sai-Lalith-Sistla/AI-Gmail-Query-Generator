import streamlit as st
import requests
from utils.api_client import BACKEND_URL, get_auth_headers, check_auth

def fetch_labels():
    try:
        resp = requests.get(f"{BACKEND_URL}/api/labels", headers=get_auth_headers())
        if resp.status_code == 200: return resp.json()
    except: return []
    return []

def show_inbox():
    st.title("📥 Inbox Analysis")
    
    if check_auth():
        col_labels, col_count = st.columns([2, 1])
        
        with col_labels:
            labels = fetch_labels()
            if isinstance(labels, dict) and "error" in labels:
                st.error(labels["error"])
                label_options = ["INBOX"]
            else:
                label_options = ["INBOX"] + ([l['name'] for l in labels] if labels else [])
            selected_label = st.selectbox("Select Gmail Label", label_options)
        
        with col_count:
            email_count = st.number_input("Fetch Count", 5, 100, 10)

        if st.button("Fetch & Classify Unread Emails", use_container_width=True, type="primary"):
            with st.spinner("Processing with Gemini..."):
                try:
                    resp = requests.get(f"{BACKEND_URL}/api/emails?count={email_count}&label={selected_label}", headers=get_auth_headers())
                    if resp.status_code == 200:
                        st.session_state.unread_emails = resp.json()
                        st.success(f"Successfully processed {len(st.session_state.unread_emails)} unread emails.")
                    else:
                        st.error(f"Error: {resp.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")

    if "unread_emails" in st.session_state:
        for email in st.session_state.unread_emails:
            with st.container():
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"### {email.get('subject', '(No Subject)')}")
                    st.write(f"**From:** `{email.get('from', 'Unknown')}`")
                    if email.get('sensitive'):
                        st.markdown("<p style='color: #facc15; font-style: italic;'>⚠️ Content masked due to sensitivity rating.</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='color: #cbd5e1;'>{email.get('snippet', '')}</p>", unsafe_allow_html=True)
                with c2:
                    if email.get('sensitive'):
                        st.markdown("<span class='category-badge badge-sensitive'>SENSITIVE</span>", unsafe_allow_html=True)
                    else:
                        st.markdown("<span class='category-badge badge-other'>STANDARD</span>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_inbox()
