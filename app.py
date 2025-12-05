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

    # CLEAN column names BEFORE ANYTHING
    df.columns = [c.strip() for c in df.columns]

    st.success("✔ File loaded successfully!")
    st.write(df.head())

    # Detect columns automatically
    life_col = find_life_expectancy_column(df)
    country_col = None
    year_col = None

    # Try to find 'Country' and 'Year'
    for col in df.columns:
        col_clean = col.lower().replace(" ", "")
        if col_clean == "country":
            country_col = col
        if col_clean == "year":
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
    country = st.selectbox("🌍 Choose a country", sorted(df[country_col].unique()))

    # --- Filter data ---
    df_country = df[df[country_col] == country].sort_values(year_col)

    st.write(f"### 📈 Life Expectancy for **{country}**")
    st.write(df_country[[year_col, life_col]])

    # --- Plot ---
    fig, ax = plt.subplots()
    ax.plot(df_country[year_col], df_country[life_col], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life Expectancy")
    ax.set_title(f"Life Expectancy Trend - {country}")

    st.pyplot(fig)



