import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Life Expectancy Analysis App")

uploaded_file = st.file_uploader("Upload Kaggle CSV here", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File loaded successfully!")
    st.write(df.head())

    # Choose country
    if "Country" in df.columns:
        country = st.selectbox("Choose a country", df["Country"].unique())

        df_country = df[df["Country"] == country]

        if "Life expectancy" in df.columns:
            plt.plot(df_country["Year"], df_country["Life expectancy"])
            plt.xlabel("Year")
            plt.ylabel("Life Expectancy")
            plt.title(f"Life Expectancy Evolution — {country}")
            st.pyplot(plt)
        else:
            st.warning("'Life expectancy' column not found in dataset.")
    else:
        st.warning("'Country' column not found in dataset.")
