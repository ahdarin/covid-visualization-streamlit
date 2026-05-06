import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/covid.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Location Level"] == "Province"]
    return df

df = load_data()

st.title("Map Visualization")

# sidebar
st.sidebar.header("Filter")

selected_date = st.sidebar.date_input(
    "Pilih Tanggal",
    value=df["Date"].max()
)

metric_option = st.sidebar.selectbox(
    "Pilih Variabel",
    ["Total Cases", "Total Deaths", "Total Recovered"]
)

# validasi
selected_date = pd.to_datetime(selected_date)

filtered = df[df["Date"] == selected_date]

if filtered.empty:
    st.warning("Tidak ada data pada tanggal ini")
    st.stop()

filtered = filtered.dropna(subset=["Latitude", "Longitude"])

# NORMALISASI ukuran titik (biar tidak terlalu besar/kecil)
size_col = filtered[metric_option]
size_scaled = (size_col - size_col.min()) / (size_col.max() - size_col.min() + 1e-9)
filtered["size"] = size_scaled * 40 + 5   # range ukuran 5–45

# PLOTLY MAP
fig = px.scatter_mapbox(
    filtered,
    lat="Latitude",
    lon="Longitude",
    size="size",
    color=metric_option,
    hover_name="Location",
    hover_data={
        "Total Cases": True,
        "Total Deaths": True,
        "Total Recovered": True,
        "Latitude": False,
        "Longitude": False,
        "size": False
    },
    color_continuous_scale="Reds",
    zoom=4,
    height=600
)

fig.update_layout(
    mapbox_style="carto-positron",
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.subheader(f"Peta {metric_option} pada {selected_date.date()}")

st.plotly_chart(fig, use_container_width=True)

# tabel bantu
st.subheader("Ranking Provinsi")

st.dataframe(
    filtered[[
        "Location",
        "Total Cases",
        "Total Deaths",
        "Total Recovered"
    ]].sort_values(metric_option, ascending=False)
)