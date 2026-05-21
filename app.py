import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="COVID Spatio-Temporal Indonesia",
    layout="wide"
)

# HEADER
st.title("Dashboard COVID-19 Indonesia")
st.write("Visualisasi data spasial dan temporal berbasis Streamlit")

# DESKRIPSI SINGKAT
st.markdown("""
Gunakan sidebar di sebelah kiri untuk berpindah halaman dan melakukan filter.
""")

# PEMISAH
st.divider()

# LAYOUT 2 KOLOM
col1, col2 = st.columns([1, 2])

# KOLOM KIRI
with col1:
    st.subheader("Fitur Aplikasi")

    st.markdown("""
    - Overview: menampilkan ringkasan data COVID-19  
    - Map: visualisasi persebaran kasus per provinsi  
    - Trends: analisis tren kasus dari waktu ke waktu  
    """)

    st.subheader("Sumber Data")
    st.markdown("""
    Dataset yang digunakan berasal dari:  
    [COVID-19 Indonesia Dataset (Kaggle)](https://www.kaggle.com/datasets/hendratno/covid19-indonesia?resource=download)
    """)

# KOLOM KANAN
with col2:
    st.subheader("Informasi Kelompok")

    st.write("Kelompok 2")

    anggota = pd.DataFrame({
        "Nama": [
            "Hanifah Larama Agasi",
            "Ahda Rindang Al-Amin",
            "Ahmad Muhaimin Kamil"
        ],
        "NIM": [
            "2311531002",
            "2311531003",
            "2311533013"
        ]
    })

    st.table(anggota)
