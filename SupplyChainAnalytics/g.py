import streamlit as st
import plotly.express as px
from prepare_data import load_data
from forecast_model import train_prophet

# -----------------------------
# 🎨 Custom CSS Styling
# -----------------------------
st.set_page_config(page_title="📦 Supply Chain Forecasting", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #fdf6f0;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #6a1b9a;
        text-align: center;
    }
    .stSidebar {
        background-color: #fff3e0;
    }
    .block-container {
        padding-top: 2rem;
    }
    .metric-box {
        background-color: #ede7f6;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 13px !important;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧠 Load Data
# -----------------------------
@st.cache_data()
def load_model():
    return load_data()

df = load_model()
store_ids = sorted(df["Store"].unique())
dept_ids = sorted(df["Dept"].unique())

# -----------------------------
# 🧭 Sidebar Filter
# -----------------------------
st.sidebar.header("🔍 Filter Your View")
selected_store = st.sidebar.selectbox("🏬 Select Store", store_ids)
selected_dept = st.sidebar.selectbox("📦 Select Department", dept_ids)

filtered = df[(df["Store"] == selected_store) & (df["Dept"] == selected_dept)]

# -----------------------------
# 📈 Title + Plots
# -----------------------------
st.title("📈 Supply Chain Sales Forecast")

# -----------------------------
# 📈 Historical Sales Plot
# -----------------------------
st.markdown("### 🗓️ Weekly Sales History")

fig1 = px.line(
    filtered,
    x="Date",
    y="Weekly_Sales",
    title="📉 Weekly Sales Over Time",
    color_discrete_sequence=["#7b1fa2"]
)
fig1.update_layout(
    title_x=0.5,
    plot_bgcolor='#fce4ec',
    paper_bgcolor='#fce4ec',
    font=dict(size=14, color="black")
)
st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# 🔮 Forecast for Next 90 Days
# -----------------------------
st.markdown("### 🔮 Prophet Forecast: Next 90 Days")
forecast_df = train_prophet(selected_store, selected_dept)

fig2 = px.line(
    forecast_df,
    x="ds",
    y="yhat",
    title="📊 Sales Forecast",
    color_discrete_sequence=["#388e3c"]
)

fig2.add_scatter(x=forecast_df["ds"], y=forecast_df["yhat_upper"], mode="lines", name="Upper Bound")
fig2.add_scatter(x=forecast_df["ds"], y=forecast_df["yhat_lower"], mode="lines", name="Lower Bound")

fig2.update_layout(
    title_x=0.5,
    plot_bgcolor='#e8f5e9',
    paper_bgcolor='#e8f5e9',
    font=dict(size=14, color="black")
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 📊 Dashboard Metrics (Now Below)
# -----------------------------
st.markdown("## 📊 Overview Dashboard (Filtered)")

total_sales = filtered["Weekly_Sales"].sum()
avg_sales = filtered["Weekly_Sales"].mean()
num_weeks = filtered["Date"].nunique()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='metric-box'><b>🏷️ Store:</b><br>{selected_store}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-box'><b>📦 Department:</b><br>{selected_dept}</div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-box'><b>💰 Total Sales:</b><br>${total_sales:,.2f}</div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-box'><b>📆 Avg Weekly Sales:</b><br>${avg_sales:,.2f}</div>", unsafe_allow_html=True)

# -----------------------------
# 🙋 Footer
# -----------------------------
st.markdown("---")
st.caption("✨ Built using Streamlit by Archana")
