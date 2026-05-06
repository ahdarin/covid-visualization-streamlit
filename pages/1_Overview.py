import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/covid.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Location Level"] == "Province"]
    return df

df = load_data()

st.title("Overview")

# sidebar
st.sidebar.header("Filter")

provinces = st.sidebar.multiselect(
    "Pilih Provinsi",
    options=sorted(df["Location"].unique())
)

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(df["Date"].min(), df["Date"].max())
)

# VALIDASI INPUT
if not provinces:
    st.warning("Pilih minimal satu provinsi")
    st.stop()

if not isinstance(date_range, tuple) or len(date_range) < 2:
    st.warning("Pilih rentang tanggal lengkap")
    st.stop()

start_date, end_date = date_range

filtered = df[
    (df["Location"].isin(provinces)) &
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

if filtered.empty:
    st.warning("Data tidak ditemukan untuk kombinasi filter ini")
    st.stop()

# metrics aman
col1, col2, col3 = st.columns(3)

col1.metric("Total Cases", int(filtered["Total Cases"].max()))
col2.metric("Total Deaths", int(filtered["Total Deaths"].max()))
col3.metric("Total Recovered", int(filtered["Total Recovered"].max()))

st.subheader("Preview Data")
st.dataframe(filtered.head(50))