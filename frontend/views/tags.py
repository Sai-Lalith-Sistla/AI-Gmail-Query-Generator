import streamlit as st
import requests
from utils.api_client import BACKEND_URL

def show_tags():
    st.title("🏷️ Tag Management")
    st.write("Organize your emails by creating custom topics.")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    new_tag = st.text_input("Add Specific Interest (e.g., 'System Design')")
    if st.button("Add Tag", use_container_width=True):
        if new_tag:
            requests.post(f"{BACKEND_URL}/api/tags", json={"tag": new_tag})
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
            
    try:
        tags = requests.get(f"{BACKEND_URL}/api/tags").json()
    except:
        tags = []
        
    if tags:
        for tag in tags:
            with st.container():
                c1, c2 = st.columns([5, 1])
                c1.markdown(f"#### {tag}")
                if c2.button("🗑️", key=f"del_{tag}"):
                    requests.delete(f"{BACKEND_URL}/api/tags?tag={tag}")
                    st.rerun()
    else:
        st.info("No focus tags registered. Add some above!")

if __name__ == "__main__":
    show_tags()
