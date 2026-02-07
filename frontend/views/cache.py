import streamlit as st
import requests
import pandas as pd
from utils.api_client import BACKEND_URL

def show_cache():
    st.title("📂 Local Cache")
    st.write("Manage emails stored on your local machine.")
    
    if st.button("Wipe Local Cache", type="primary", use_container_width=True):
        requests.delete(f"{BACKEND_URL}/api/local-data")
        st.rerun()
        
    try:
        local_emails = requests.get(f"{BACKEND_URL}/api/local-data").json()
    except:
        local_emails = []

    if local_emails:
        df = pd.DataFrame(local_emails)
        st.dataframe(df[['subject', 'from', 'sensitive']], use_container_width=True)
    else:
        st.info("Local storage is currently empty.")

if __name__ == "__main__":
    show_cache()
