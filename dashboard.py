import streamlit as st
import pandas as pd
from data_cleaning import load_data, data_cleaning, create_columns

@st.cache_data
def get_data():
    df = load_data()
    df = data_cleaning(df)
    df = create_columns(df)

    return df

df = get_data()

st.title("Superstore Sales Dashboard")

st.sidebar.title("Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))

filtered_data = df[df["Year"] == selected_year]

monthly = filtered_data.groupby("Month")[["Sales", "Profit"]].sum().reset_index()

st.subheader(f"Monthly Sales & Profit in {selected_year}")
st.line_chart(monthly.set_index('Month'))

category_sales = filtered_data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

st.subheader(f"Sales by Category in {selected_year}")
st.bar_chart(category_sales)

metric = st.sidebar.selectbox("Select A Metric To Sort The Subcategories By", options =["Sales", "Quantity", "Profit", "Profit Margin"])
if metric == "Profit Margin":
    best_sub_categories = filtered_data.groupby("Sub-Category")[metric].mean().sort_values(ascending=False).head(10)
else:
    best_sub_categories = filtered_data.groupby("Sub-Category")[metric].sum().sort_values(ascending=False).head(10)

st.subheader(f"Top 10 Sub-Categories by {metric} in {selected_year}")
st.dataframe(best_sub_categories)