import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Behavior vs Market Sentiment")

# Load data
@st.cache_data
def load_data():
    return pd.read_pickle("dashboard_data.pkl")

data = load_data()

# Sidebar filters
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=data["classification"].unique(),
    default=data["classification"].unique()
)

filtered_data = data[data["classification"].isin(sentiment_filter)]

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(filtered_data.head())

# --- PnL Distribution ---
st.subheader("PnL Distribution by Sentiment")

fig, ax = plt.subplots()

sns.boxplot(x="classification", y="Closed PnL", data=filtered_data, ax=ax)

st.pyplot(fig)

# --- Trade Direction ---
st.subheader("Trade Direction (Long vs Short)")

side_counts = filtered_data["Side"].value_counts()

st.bar_chart(side_counts)

# --- Trade Frequency ---
st.subheader("Trades Per Day")

trades_per_day = filtered_data.groupby("date").size()

st.line_chart(trades_per_day)

# --- Trader Segmentation ---
st.subheader("Trader Activity Segmentation")

trade_counts = filtered_data.groupby("Account").size()

fig2, ax2 = plt.subplots()

sns.histplot(trade_counts, bins=30, ax=ax2)

ax2.set_title("Trades per Trader")

st.pyplot(fig2)

# Insights section
st.subheader("Key Insights")

st.markdown("""
• Greed sentiment tends to show higher trading activity.  
• Traders appear more active during optimistic market conditions.  
• Profit/loss variability increases when trade activity rises.
""")