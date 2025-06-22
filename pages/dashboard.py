import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from pages.chatbot import chatbot_page

# Dashboard Page Function
def dashboard_page():

    # Top navigation menu (buttons)
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    # Create buttons for navigation
    button_cols = st.columns(4)  # Removed Settings option
    with button_cols[0]:
        if st.button("Overview", key="overview"):
            st.session_state.page = "Overview"
    with button_cols[1]:
        if st.button("Analytics", key="analytics"):
            st.session_state.page = "Analytics"
    with button_cols[2]:
        if st.button("Crowdfunding", key="crowdfunding"):
            st.session_state.page = "Crowdfunding"
    with button_cols[3]:
        if st.button("Chatbot", key="chatbot"):
            st.session_state.page = "Chatbot"

    st.markdown('</div>', unsafe_allow_html=True)

    # Default page set to Overview if not defined
    page = st.session_state.get('page', "Overview")  # Load page from session state

    # Overview Page
    if page == "Overview":
        st.title("Overview")
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Key Metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Daily Revenue", "$1,200", "+5%")
        with col2:
            st.metric("Customer Satisfaction", "94%", "+2%")
        with col3:
            st.metric("Active Customers", "150", "-3%")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Revenue Trend")
        chart_data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=30),
            'Revenue': np.random.randn(30).cumsum()
        })
        fig = px.line(chart_data, x='Date', y='Revenue', title='Revenue Trend')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Analytics Page
    elif page == "Analytics":
        st.title("Dynamic Business Analytics")
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Analytics of Your Business Performance")
        time_period = st.selectbox(
            "Select Time Period",
            ["Last 7 days", "Last 30 days", "Last 90 days", "Custom Range"],
            index=1
        )

        if time_period == "Last 7 days":
            start_date = datetime.today() - timedelta(days=7)
            end_date = datetime.today()
        elif time_period == "Last 30 days":
            start_date = datetime.today() - timedelta(days=30)
            end_date = datetime.today()
        elif time_period == "Last 90 days":
            start_date = datetime.today() - timedelta(days=90)
            end_date = datetime.today()
        else:
            start_date = st.date_input("Start Date", datetime.today() - timedelta(days=30))
            end_date = st.date_input("End Date", datetime.today())

        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        revenue = np.random.randn(len(dates)).cumsum() + 1000

        revenue_data = pd.DataFrame({'Date': dates, 'Revenue': revenue})
        fig = px.line(revenue_data, x='Date', y='Revenue', title=f'Revenue Trend for {time_period}')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Sales by Category")
        categories = ['Tech', 'Clothing', 'Furniture', 'Food', 'Sports', 'Beauty']
        sales_data = pd.DataFrame({
            'Category': categories,
            'Sales': np.random.randint(500, 5000, size=len(categories))
        })
        fig = px.bar(sales_data, x='Category', y='Sales', title="Sales by Category")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Crowdfunding Page
    elif page == "Crowdfunding":
        st.title("Crowdfunding Campaigns - Real-time Progress")
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("### Real-time Crowdfunding Campaign Statistics")
        campaigns = ['Tech Innovation', 'Eco-Friendly Packaging', 'AI for Healthcare', 'Smart Home Solutions']
        funding = np.random.randint(1000, 50000, size=4)
        goals = [50000, 20000, 100000, 70000]
        data = pd.DataFrame({
            'Campaign': campaigns,
            'Funds Raised': funding,
            'Goal': goals
        })

        fig = px.bar(data, x='Campaign', y=['Funds Raised', 'Goal'], title='Crowdfunding Progress')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chatbot Page
    elif page == "Chatbot":
        chatbot_page()

    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("Business Dashboard | All rights reserved", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
dashboard_page()