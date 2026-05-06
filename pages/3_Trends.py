import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/covid.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Location Level"] == "Province"]
    return df

df = load_data()

st.title("Temporal Trends")

# sidebar
st.sidebar.header("Filter")

selected_province = st.sidebar.selectbox(
    "Pilih Provinsi",
    sorted(df["Location"].unique())
)

metric_option = st.sidebar.selectbox(
    "Pilih Variabel",
    ["New Cases", "Total Cases", "Total Deaths"]
)

filtered = df[df["Location"] == selected_province]

# sort tanggal
filtered = filtered.sort_values("Date")

st.subheader(f"Trend {metric_option} - {selected_province}")

chart_data = filtered.set_index("Date")[metric_option]

st.line_chart(chart_data)

# agregasi nasional
st.subheader("Trend Nasional (New Cases)")

national = df.groupby("Date")["New Cases"].sum().reset_index()
national = national.set_index("Date")

st.line_chart(national)