import streamlit as st
import pandas as pd
import requests
import os
import streamlit.components.v1 as components
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
    h1, h2, h3 { color: #e6edf3 !important; }
    p, label { color: #7d8590 !important; }
    .stTextInput input { background-color: #21262d !important; color: #e6edf3 !important; border: 1px solid #30363d !important; border-radius: 6px !important; }
    .stButton button { background-color: #238636 !important; color: white !important; border: none !important; border-radius: 6px !important; font-weight: 500 !important; }
    .stDataFrame { background-color: #161b22 !important; }
    div[data-testid="metric-container"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; padding: 16px !important; }
    .stSuccess { background-color: #1a2f1a !important; color: #3fb950 !important; }
    .stWarning { background-color: #2f2a1a !important; color: #d29922 !important; }
    .stInfo { background-color: #1a2233 !important; color: #2a78d6 !important; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""<div style='padding: 8px 0 20px;'><div style='display:flex; align-items:center; gap:10px;'><div style='width:32px; height:32px; background:#238636; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:16px;'>🎯</div><div><div style='color:#e6edf3; font-size:16px; font-weight:600;'>LeadHunter</div><div style='color:#7d8590; font-size:11px;'>Find Leads. Close Deals.</div></div></div></div>""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='color:#7d8590; font-size:10px; padding:8px 4px 4px; font-weight:600; letter-spacing:1px;'>PLATFORM SEARCH</div>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["🏠  Dashboard", "💼  LinkedIn Leads", "▶️  YouTube Leads", "📧  Email Finder"])

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
        st.markdown("<div style='background:#161b22; border:1px solid #30363d; border-radius:8px; padding:16px;'><div style='color:#e6edf3; font-weight:500; margin-bottom:4px;'>🔍 Platform Search</div><div style='color:#7d8590; font-size:12px; margin-bottom:12px;'>Find leads from multiple platforms</div><div style='display:grid; grid-template-columns:1fr 1fr; gap:8px;'><div style='background:#21262d; border:1px solid #30363d; border-radius:6px; padding:10px; display:flex; align-items:center; gap:8px;'><span style='font-size:18px;'>▶️</span><div><div style='color:#e6edf3; font-size:12px;'>YouTube</div><div style='color:#7d8590; font-size:10px;'>Extract leads</div></div></div><div style='background:#21262d; border:1px solid #30363d; border-radius:6px; padding:10px; display:flex; align-items:center; gap:8px;'><span style='font-size:18px;'>📸</span><div><div style='color:#e6edf3; font-size:12px;'>Instagram</div><div style='color:#7d8590; font-size:10px;'>Extract leads</div></div></div><div style='background:#21262d; border:1px solid #30363d; border-radius:6px; padding:10px; display:flex; align-items:center; gap:8px;'><span style='font-size:18px;'>💼</span><div><div style='color:#e6edf3; font-size:12px;'>LinkedIn</div><div style='color:#7d8590; font-size:10px;'>Extract leads</div></div></div><div style='background:#21262d; border:1px solid #30363d; border-radius:6px; padding:10px; display:flex; align-items:center; gap:8px;'><span style='font-size:18px;'>🌐</span><div><div style='color:#e6edf3; font-size:12px;'>Website</div><div style='color:#7d8590; font-size:10px;'>Scrape leads</div></div></div></div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='background:#161b22; border:1px solid #30363d; border-radius:8px; padding:16px;'><div style='color:#e6edf3; font-weight:500; margin-bottom:12px;'>🕐 Recent Searches</div><div style='display:flex; flex-direction:column; gap:8px;'><div style='color:#7d8590; font-size:12px;'>🏢 Digital Agency</div><div style='color:#7d8590; font-size:12px;'>🏠 Real Estate</div><div style='color:#7d8590; font-size:12px;'>💻 SaaS</div><div style='color:#7d8590; font-size:12px;'>🛒 E-commerce</div><div style='color:#7d8590; font-size:12px;'>💪 Fitness</div></div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='color:#e6edf3; font-weight:500; margin-bottom:12px;'>👥 Recent Leads</div>", unsafe_allow_html=True)

    data = {
        "Name": ["John Smith", "Emma Wilson", "David Lee", "Sarah Clark", "Michael Tan"],
        "Title": ["CEO", "Marketing Manager", "Founder", "Co-founder", "Sales Director"],
        "Company": ["TechSolutions", "GrowthLab", "AI Startups", "BrandBoost", "SalesHub"],
        "Email": ["✓ Verified", "✓ Verified", "✓ Verified", "✓ Verified", "✓ Verified"],
        "Source": ["LinkedIn", "Instagram", "LinkedIn", "YouTube", "LinkedIn"],
        "Added": ["2 mins ago", "10 mins ago", "25 mins ago", "1 hour ago", "2 hours ago"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='color:#e6edf3; font-weight:500; margin-bottom:8px;'>📊 Leads Overview</div>", unsafe_allow_html=True)
        chart_data = pd.DataFrame({"Leads": [800, 1200, 900, 1800, 1400, 1100, 1600]}, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        st.line_chart(chart_data, color="#2a78d6")
    with col2:
        components.html("""
        <div style='background:#161b22; border:1px solid #30363d; border-radius:8px; padding:16px;'>
            <div style='color:#e6edf3; font-weight:500; margin-bottom:8px; font-family:sans-serif;'>✅ Email Verification Stats</div>
            <div style='font-size:11px; color:#7d8590; margin-bottom:8px; font-family:sans-serif;'>
                🟢 Valid 8,420 (67%) &nbsp; 🔴 Invalid 2,546 (17%)<br>
                🟡 Disposable 1,252 (10%) &nbsp; ⚫ Catch-all 726 (5.8%)
            </div>
            <canvas id="donutChart" style="max-height:180px;"></canvas>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
        <script>
        new Chart(document.getElementById('donutChart'), {
            type: 'doughnut',
            data: {
                labels: ['Valid', 'Invalid', 'Disposable', 'Catch-all'],
                datasets: [{
                    data: [8420, 2546, 1252, 726],
                    backgroundColor: ['#3fb950', '#f85149', '#d29922', '#7d8590'],
                    borderWidth: 2,
                    borderColor: '#161b22'
                }]
            },
            options: {
                cutout: '65%',
                plugins: { legend: { display: false } }
            }
        });
        </script>
        """, height=280)
elif page == "💼  LinkedIn Leads":
    st.markdown("<h2 style='color:#e6edf3;'>💼 LinkedIn Lead Finder</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        job_title = st.text_input("Job Title", placeholder="e.g. CEO, Marketing Manager")
    with col2:
        industry = st.text_input("Industry", placeholder="e.g. Technology, Finance")
    if st.button("🔍 Search Leads"):
        if job_title:
            with st.spinner("Searching leads..."):
                demo_data = [
                    {"Name": "John Smith", "Title": job_title, "Company": "Tech Corp", "Email": "john@techcorp.com", "Location": "New York"},
                    {"Name": "Sarah Johnson", "Title": job_title, "Company": "StartupXYZ", "Email": "sarah@startup.com", "Location": "San Francisco"},
                    {"Name": "Mike Wilson", "Title": job_title, "Company": "Digital Co", "Email": "mike@digital.com", "Location": "London"},
                    {"Name": "Emma Davis", "Title": job_title, "Company": "Growth Hub", "Email": "emma@growthhub.com", "Location": "Dubai"},
                    {"Name": "Ali Hassan", "Title": job_title, "Company": "AI Startup", "Email": "ali@aistartup.com", "Location": "Karachi"},
                ]
                df = pd.DataFrame(demo_data)
                st.success(f"Found {len(demo_data)} leads!")
                st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.warning("Please enter a job title!")

elif page == "▶️  YouTube Leads":
    st.markdown("<h2 style='color:#e6edf3;'>▶️ YouTube Lead Finder</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        channel_keyword = st.text_input("Channel Keyword", placeholder="e.g. Digital Marketing")
    with col2:
        max_results = st.number_input("Max Results", min_value=1, max_value=50, value=10)
    if st.button("🔍 Search YouTube Channels"):
        if channel_keyword:
            with st.spinner("Searching YouTube..."):
                api_key = os.getenv("YOUTUBE_API_KEY")
                url = "https://www.googleapis.com/youtube/v3/search"
                params = {
                    "part": "snippet",
                    "q": channel_keyword,
                    "type": "channel",
                    "maxResults": int(max_results),
                    "key": api_key
                }
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    channels = data.get("items", [])
                    if channels:
                        results = []
                        for ch in channels:
                            snippet = ch.get("snippet", {})
                            results.append({
                                "Channel": snippet.get("channelTitle", ""),
                                "Description": snippet.get("description", "")[:50] + "...",
                                "Channel ID": ch.get("id", {}).get("channelId", "")
                            })
                        df = pd.DataFrame(results)
                        st.success(f"Found {len(results)} channels!")
                        st.dataframe(df, use_container_width=True, hide_index=True)
                    else:
                        st.warning("No channels found!")
                else:
                    st.error(f"Error: {response.status_code}")
        else:
            st.warning("Please enter a keyword!")

elif page == "📧  Email Finder":
    st.markdown("<h2 style='color:#e6edf3;'>📧 Email Finder</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name", placeholder="e.g. John")
        last_name = st.text_input("Last Name", placeholder="e.g. Smith")
    with col2:
        company = st.text_input("Company Name", placeholder="e.g. Google")
        domain = st.text_input("Domain", placeholder="e.g. google.com")
    if st.button("🔍 Find Email"):
        if first_name and company:
            with st.spinner("Finding email..."):
                st.success("Email found!")
                st.info(f"📧 {first_name.lower()}.{last_name.lower()}@{domain if domain else company.lower()+'.com'}")
        else:
            st.warning("Please fill in the required fields!")