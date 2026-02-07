import streamlit as st
from utils.styles import apply_custom_styles
from views.home import show_home
from views.setup import show_setup
from views.inbox import show_inbox
from views.tags import show_tags
from views.queries import show_queries
from views.cache import show_cache

st.set_page_config(
    page_title="Inbox AI",
    page_icon="📧",
    layout="wide",
)

# Apply shared styles
apply_custom_styles()

# Initialize session state for navigation if needed
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='color: white; font-weight: 700;'>📩 Inbox AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 2rem;'>Custom Email Intelligence</p>", unsafe_allow_html=True)
    
    nav_items = [
        ("🏠 Home", show_home),
        ("🔐 Setup", show_setup),
        ("📥 Analysis", show_inbox),
        ("🏷️ Tags", show_tags),
        ("🔍 Queries", show_queries),
        ("📂 Cache", show_cache)
    ]
    
    for label, view_func in nav_items:
        is_active = st.session_state.page == label
        if st.button(label, key=f"nav_{label}", use_container_width=True, 
                    type="primary" if is_active else "secondary"):
            st.session_state.page = label
            st.rerun()

    st.markdown("---")
    st.markdown("### Status")
    if st.session_state.get("gemini_api_key"):
        st.success("✅ Keys Loaded")
    else:
        st.warning("⚠️ Setup Required")

# Render the selected page
current_page_label = st.session_state.page
for label, view_func in nav_items:
    if label == current_page_label:
        view_func()
        break
