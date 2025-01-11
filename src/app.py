import streamlit as st
from utils.database import get_inventory_status, get_sales_trends, get_customer_insights
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Insights Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
selected_section = st.sidebar.radio(
    "Select a Section:",
    ["Overview", "Inventory Status", "Sales Trends", "Customer Insights"],
)

# Dashboard Header
st.markdown(
    """
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #2C3E50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 18px;
            color: #7F8C8D;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="title">📊 E-Commerce Insights Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Unlock actionable insights to drive better business decisions</div>', unsafe_allow_html=True)

# Overview Section
if selected_section == "Overview":
    st.header("📄 Overview")
    st.markdown(
        """
        Welcome to the E-Commerce Insights Dashboard! This platform provides:
        - **Inventory Tracking:** Monitor stock levels and avoid shortages.
        - **Sales Trends:** Analyze revenue over time to identify peak periods.
        - **Customer Insights:** Understand spending behavior to tailor marketing strategies.
        """
    )
    st.image("assets/overview_banner.png", use_column_width=True)

# Inventory Status Section
if selected_section == "Inventory Status":
    st.header("📦 Inventory Status")
    inventory_data = get_inventory_status()
    if inventory_data.empty:
        st.warning("No inventory data available.")
    else:
        st.dataframe(
            inventory_data.style.format({"TotalStock": "{:.0f}"}).highlight_max(
                subset=["TotalStock"], color="lightgreen", axis=0
            ),
            use_container_width=True,
        )

# Sales Trends Section
if selected_section == "Sales Trends":
    st.header("📈 Sales Trends")
    sales_data = get_sales_trends()
    if sales_data.empty:
        st.warning("No sales data available.")
    else:
        fig = px.line(
            sales_data,
            x="date",
            y="TotalSales",
            title="Total Sales Over Time",
            labels={"date": "Date", "TotalSales": "Total Sales"},
            template="plotly_white",
            markers=True,
        )
        fig.update_traces(line=dict(color="royalblue", width=3), marker=dict(size=8))
        st.plotly_chart(fig, use_container_width=True)

# Customer Insights Section
if selected_section == "Customer Insights":
    st.header("🏆 Customer Insights")
    customer_data = get_customer_insights()
    if customer_data.empty:
        st.warning("No customer insights available.")
    else:
        fig = px.bar(
            customer_data,
            x="customerid",
            y="TotalSpend",
            title="Top Customers by Spend",
            labels={"customerid": "Customer ID", "TotalSpend": "Total Spend"},
            template="plotly_white",
            color="TotalSpend",
            color_continuous_scale="Blues",
        )
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown(
    """
    <style>
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #2C3E50;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        © 2025 E-Commerce Insights | Nitish Malang
    </div>
    """,
    unsafe_allow_html=True,
)
