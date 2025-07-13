Nama,Simbol,Nomor Atom,Massa Atom,Golongan,Jenis
Hidrogen,H,1,1.008,1,Non-logam
Helium,He,2,4.0026,18,Gas Mulia
Litium,Li,3,6.94,1,Logam Alkali
Berilium,Be,4,9.0122,2,Logam Alkali Tanah
Bor,B,5,10.81,13,Metaloid

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Database Elemen Periodik", layout="centered")

st.title("🧪 Database Elemen Periodik Interaktif")

# Load data
df = pd.read_csv("elements.csv")

# Filter interaktif
nama = st.text_input("Cari berdasarkan nama atau simbol (contoh: H, O, Fe):")
golongan = st.selectbox("Pilih golongan", options=["Semua"] + sorted(df["Golongan"].astype(str).unique().tolist()))

# Filter data
filtered = df.copy()
if nama:
    filtered = filtered[
        filtered["Nama"].str.contains(nama, case=False) |
        filtered["Simbol"].str.contains(nama, case=False)
    ]
if golongan != "Semua":
    filtered = filtered[filtered["Golongan"].astype(str) == golongan]

# Tampilkan tabel
st.dataframe(filtered)

# Info tambahan
st.markdown("""
**Keterangan Kolom:**
- Simbol: Singkatan unsur (mis. H = Hidrogen)
- Golongan: Kolom pada tabel periodik
- Jenis: Logam, non-logam, gas mulia, dll.
""")
