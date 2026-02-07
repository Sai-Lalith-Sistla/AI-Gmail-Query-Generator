import streamlit as st

def show_home():
    st.markdown("<h1 class='main-header'>Next-Gen Email Intelligence</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
        <div class='glass-card'>
            <h3>Automate Your Inbox Cleanup</h3>
            <p style='color: #94a3b8;'>Inbox AI leverages Model Context Protocol (MCP) and Google Gemini to classify your unread emails into actionable groups.</p>
            <hr style='border: 0.5px solid rgba(255,255,255,0.1); margin: 20px 0;'>
            <h4 style='color: #f1f5f9;'>Core Workflow:</h4>
            <p>1. <b>Configure</b> your Gemini and Gmail API keys securely.</p>
            <p>2. <b>Analyze</b> unread emails with privacy-aware sensitivity masking.</p>
            <p>3. <b>Manage</b> custom tags to group related engineering or design topics.</p>
            <p>4. <b>Batch Delete</b> using AI-generated Gmail search keys.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Get Started ⚡", use_container_width=True, type="primary"):
            st.session_state.page = "🔐 Setup"
            st.rerun()

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <h4>🔒 Privacy First</h4>
            <p style='font-size: 0.9rem; color: #94a3b8;'>Your keys are stored only in volatile session memory. No data is saved to our server disks except for non-sensitive email metadata in your local cache.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
