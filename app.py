import streamlit as st

st.title("Kalkulator Biaya Kos Per Bulan 💰")
st.write("Hitung kira-kira sebulan lu habis berapa di kos!")

# 1. FUNGSI BUATAN SENDIRI
def hitung_total(sewa, makan_harian, listrik, harga_paket, pakai_wifi):
    makan_bulanan = makan_harian * 30
    biaya_wifi = 100000 if pakai_wifi else 0
    total = sewa + makan_bulanan + listrik + harga_paket + biaya_wifi
    return total, makan_bulanan, biaya_wifi

# DATA PAKET PAKAI DICT
daftar_paket = {
    "Hemat (Kuota 10GB)": 50000,
    "Normal (Kuota 30GB)": 100000,
    "Sultan (Unlimited)": 200000
}

# 2. 4 WIDGET INPUT
sewa = st.number_input("1. Sewa kos per bulan (Rp)", min_value=0, value=800000, step=50000)
makan_harian = st.slider("2. Budget makan per hari (Rp)", 10000, 100000, 30000)
listrik = st.number_input("3. Biaya listrik / token per bulan (Rp)", min_value=0, value=100000, step=10000)
pilihan_paket = st.selectbox("4. Pilih paket internet", list(daftar_paket.keys()))
pakai_wifi = st.checkbox("Tambah WiFi kos (+ Rp 100.000)")

# AMBIL HARGA PAKET DARI DICT
harga_paket = daftar_paket[pilihan_paket]

if st.button("Hitung Total!"):
    total, makan_bulanan, biaya_wifi = hitung_total(sewa, makan_harian, listrik, harga_paket, pakai_wifi)

    # 3. LOGIKA IF/ELSE
    if total < 1500000:
        kategori = "HEMAT BANGET! 🤑"
        saran = "Pertahankan! Masih bisa nabung banyak."
    elif total < 2500000:
        kategori = "NORMAL 🙂"
        saran = "Masih wajar untuk anak kos."
    else:
        kategori = "BOROS! 😭"
        saran = "Coba kurangin jajan / makan di luar."

    # 4. OUTPUT METRIC + GRAFIK
    st.metric("Total Biaya Per Bulan", f"Rp {total:,}")
    st.write(f"**Kategori:** {kategori}")
    st.write(saran)

    # DATA BUAT GRAFIK PAKAI DICT
    rincian = {
        "Sewa": sewa,
        "Makan": makan_bulanan,
        "Listrik": listrik,
        "Paket": harga_paket,
        "WiFi": biaya_wifi
    }
    st.write("### Rincian Biaya")
    st.bar_chart(rincian)