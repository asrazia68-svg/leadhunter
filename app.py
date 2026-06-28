import streamlit as st
import pandas as pd
import requests
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

st.set_page_config(
    page_title="LeadHunter",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background-color: #0d1117 !important; }
    section[data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    section[data-testid="stSidebar"] .stRadio label { color: #7d8590 !important; font-size: 13px; }
    section[data-testid="stSidebar"] .stRadio [data-checked="true"] label { color: #e6edf3 !important; }
    h1, h2, h3 { color: #e6edf3 !important; }
    p, label { color: #7d8590 !important; }
    .stTextInput input { background-color: #21262d !important; color: #e6edf3 !important; border: 1px solid #30363d !important; border-radius: 6px !important; }
    .stButton button { background-color: #238636 !important; color: white !important; border: none !important; border-radius: 6px !important; font-weight: 500 !important; }
    .stButton button:hover { background-color: #2ea043 !important; }
    .stDataFrame { background-color: #161b22 !important; }
    .stDataFrame td, .stDataFrame th { color: #e6edf3 !important; background-color: #161b22 !important; }
    div[data-testid="metric-container"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; padding: 16px !important; }
    div[data-testid="metric-container"] label { color: #7d8590 !important; }
    div[data-testid="metric-container"] div { color: #e6edf3 !important; }
    .stAlert { background-color: #161b22 !important; border: 1px solid #30363d !important; color: #e6edf3 !important; }
    .stNumberInput input { background-color: #21262d !important; color: #e6edf3 !important; border: 1px solid #30363d !important; }
    div[data-testid="stDownloadButton"] button { background-color: #238636 !important; color: white !important; }
    .stSuccess { background-color: #1a2f1a !important; color: #3fb950 !important; border: 1px solid #3fb950 !important; }
    .stWarning { background-color: #2f2a1a !important; color: #d29922 !important; }
    .stInfo { background-color: #1a2233 !important; color: #2a78d6 !important; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style='padding: 8px 0 20px;'>
    <div style='display:flex; align-items:center; gap:10px;'>
        <div style='width:32px; height:32px; background:#238636; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:16px;'>🎯</div>
        <div>
            <div style='color:#e6edf3; font-size:16px; font-weight:600;'>LeadHunter</div>
            <div style='color:#7d8590; font-size:11px;'>Find Leads. Close Deals.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='color:#7d8590; font-size:10px; padding:8px 4px 4px; font-weight:600; letter-spacing:1px;'>PLATFORM SEARCH</div>", unsafe_allow_html=True)
page = st.sidebar.radio("", [
    "🏠  Dashboard",
    "💼  LinkedIn Leads",
    "▶️  YouTube Leads",
    "📧  Email Finder",
])

st.sidebar.markdown("<div style='color:#7d8590; font-size:10px; padding:8px 4px 4px; font-weight:600; letter-spacing:1px;'>TOOLS</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>✅ Email Verifier</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>📨 Bulk Email Finder</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>🌐 Domain Search</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>🏢 Company Search</div>", unsafe_allow_html=True)

st.sidebar.markdown("<div style='color:#7d8590; font-size:10px; padding:8px 4px 4px; font-weight:600; letter-spacing:1px;'>MANAGE</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>🔖 Saved Leads</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>📢 Campaigns</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>📤 Exports</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color:#7d8590; font-size:12px; padding:4px 8px;'>📊 CRM</div>", unsafe_allow_html=True)

if page == "🏠  Dashboard":
    st.markdown("<h2 style='color:#e6edf3; margin-bottom:4px;'>📊 Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7d8590; margin-bottom:20px;'>Welcome back! 👋</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Leads", "12,540", "+8%")
    col2.metric("✅ Verified Emails", "8,420", "+5%")
    col3.metric("📧 Emails Found", "7,235", "+3%")
    col4.metric("📤 Export Count", "45", "+2%")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='background:#161b22; border:1px solid #30363d; border-radius:8px; padding:16px;'>
            <div style='color:#e6edf3; font-weight:500; margin-bottom:4px;'>🔍 Platform Search</div>
            <div style='color:#7d8590; font-size:12px; margin-bottom:12px;'>Find leads from multiple platforms</div>
            <div style='display:grid; grid-template-columns:1fr 1fr; gap:8px;'>
                <div style='background:#21262d; border:1px solid #30363d; border-radius:6px; padding:10px; display:flex; align-items:center; gap:8px;'>
                    <span style='font-size:18px;'>▶️</span>
                    <div><div style='color:#e6edf3; font-size:12px;'>YouTube</div><div