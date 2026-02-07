import streamlit as st

def apply_custom_styles():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* FIX: High-contrast Labels for input boxes */
    .stTextInput label, .stSelectbox label, .stSlider label, .stNumberInput label, .stMultiSelect label {
        color: #f1f5f9 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.5);
    }

    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .category-badge {
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    
    .badge-important { background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid #22c55e; }
    .badge-sensitive { background: rgba(234, 179, 8, 0.15); color: #facc15; border: 1px solid #eab308; }
    .badge-other { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid #3b82f6; }

    /* Custom scrollbar for glass cards */
    .glass-card::-webkit-scrollbar {
        width: 8px;
    }
    .glass-card::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.05);
    }
    .glass-card::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.1);
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)
