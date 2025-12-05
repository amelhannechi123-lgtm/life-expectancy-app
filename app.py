import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Life Expectancy Analysis App")

# --- Function to automatically detect life expectancy column ---
def find_life_expectancy_column(df):
    for col in df.columns:
        col_clean = col.lower().replace(" ", "").replace("_", "")
        if "lifeexpectancy" in col_clean:
            return col
    return None

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload Kaggle CSV here", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("✔ File loaded successfully!")
    st.write(df.head())

    # Normalize column names for internal use
    df.columns = [c.strip() for c in df.columns]

    # Detect columns automatically
    life_col = find_life_expectancy_column(df)
    country_col = None
    year_col = None

    # Try to find 'Country' column
    for col in df.columns:
        if col.lower().replace(" ", "") == "country":
            country_col = col
        if col.lower().replace(" ", "") == "year":
            year_col = col

    # --- Error handling ---
    if life_col is None:
        st.error("❌ 'Life expectancy' column not found.")
        st.write("Detected columns:", df.columns.tolist())
        st.stop()

    if country_col is None:
        st.error("❌ 'Country' column not found.")
        st.write("Detected columns:", df.columns.tolist())
        st.stop()

    if year_col is None:
        st.error("❌ 'Year' column not found.")
        st.write("Detected columns:", df.columns.tolist())
        st.stop()

    # --- UI selection ---
    country = st.selectbox("🌍 Choose a country", df[country_col].unique())


