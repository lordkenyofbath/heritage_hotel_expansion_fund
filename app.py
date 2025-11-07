# --- MBBB CONSULTING : STREAMKIT v1 ---
# Run locally:   streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Heritage Hotel Expansion Fund | MBBB Streamkit",
    layout="wide",
    page_icon="🏰"
)

# -------------------------------
# HEADER
# -------------------------------
st.title("🏰 Heritage Hotel Expansion Fund")
st.markdown("### Raising £10 Million Equity for Portfolio Growth Across UK Historic Hotels")

st.write("""
The Fund acquires and revitalises heritage hotels across the UK market,
driving value through refurbishment, rebranding and operational uplift.
It targets undercapitalised assets with strong character and tourism demand.
""")

st.divider()

# -------------------------------
# FINANCIAL SNAPSHOT
# -------------------------------
st.subheader("📊 Financial Snapshot")

data = {
    "Year": ["Y0", "Y1", "Y2", "Y3", "Y4", "Y5"],
    "Revenue (£M)": [8, 12, 17, 23, 30, 38],
    "EBITDA (£M)": [1.5, 2.5, 3.8, 5.6, 7.5, 9.8],
}
df = pd.DataFrame(data)

col1, col2 = st.columns([1.5, 1])

fig = px.bar(
    df,
    x="Year",
    y=["Revenue (£M)", "EBITDA (£M)"],
    barmode="group",
    color_discrete_sequence=["#0A2E65", "#F47B20"],
    title="Revenue and EBITDA Growth (5-Year Forecast)"
)
fig.update_layout(
    xaxis_title="",
    yaxis_title="£ Millions",
    legend_title="",
    template="simple_white",
)
col1.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Target IRR", "20%")
    st.metric("Leverage", "45%")
    st.metric("Exit Strategy", "UK Hospitality REIT Listing")
    st.metric("Portfolio", "3 Freeholds Under Offer")

st.divider()

# -------------------------------
# KEY HIGHLIGHTS
# -------------------------------
st.subheader("💡 Key Investment Highlights")
st.markdown("""
- Proven heritage hospitality team with 40+ years of collective experience  
- Target portfolio IRR 20% over 5 years  
- Low leverage (45%) and asset-backed returns  
- First-phase assets include 3 operating freeholds under offer  
- Clear exit via UK Hospitality REIT listing  
""")

# -------------------------------
# STRATEGIC PILLARS
# -------------------------------
st.subheader("🧭 Strategic Pillars")

cols = st.columns(4)
pillars = [
    ("🏦 Acquire", "Identify heritage hotels below replacement cost"),
    ("🛠 Refurbish", "Reposition assets to 4★ premium standard"),
    ("🌟 Rebrand", "Enhance ADR & occupancy via brand narrative"),
    ("♻️ Refinance", "Recycle profits into next growth cycle")
]

for i, (icon, desc) in enumerate(pillars):
    with cols[i]:
        st.markdown(f"### {icon}")
        st.write(desc)

st.divider()

# -------------------------------
# FOOTER
# -------------------------------
st.caption("© 2025 MBBB Consulting | Built with Streamkit (Streamlit)")
