import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Page title
st.title("📈 NSE Stock Price Viewer")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Stock_NSE.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Stock selection dropdown
stock_list = df["stock"].unique()
selected_stock = st.selectbox("Select Stock", stock_list)

# Filter data based on stock
filtered_df = df[df["stock"] == selected_stock]

# Date range selection
min_date = filtered_df["Date"].min()
max_date = filtered_df["Date"].max()

start_date, end_date = st.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter by date
mask = (filtered_df["Date"] >= pd.to_datetime(start_date)) & \
       (filtered_df["Date"] <= pd.to_datetime(end_date))

filtered_df = filtered_df.loc[mask]

# Plot
st.subheader(f"{selected_stock} Closing Price")

fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=filtered_df, x="Date", y="Close", ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)
