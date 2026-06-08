import streamlit as st
import joblib

st.title(" Sistem Sortir Kopi Otomstid v3")
st.write(" Selamat datang di panel kendali  AI pabrik, silahkan sesuaikan sensor dibawah untuk menyortir kualitas biji kopi secara instan. ")
st.markdown("---")

@st.cache_resource
def muat_otak_ai():
    return joblib.load("otak_kopi_pipeline.joblib")

otak_ai = muat_otak_ai()

st.subheader(" Input Parameter Sensor Biji Kopi")

input_ukuran = st.slider("Ukuran Biji Kopi (mm)", min_value = 1.0, max_value = 15.0, value = 7.0, step = 0.1 )
input_gelap = st.slider("Tingkat Kegelapan Warna (1-10)", min_value = 1.0, max_value = 10.0, value = 5.0, step = 0.1)

st.markdown("---")

st.subheader(" Hasil Keputusan Mesin AI")

data_baru = [[input_ukuran, input_gelap]]

kode_tebakan = otak_ai.predict(data_baru)[0]

if kode_tebakan == 0:
    st.success("### KUALITAS: PREMIUM (0)")
    st.write("Biji kopi memenuhi standar ekspor internasional. Masukkan ke Gudang A. ")

elif kode_tebakan == 1 :
    st.warning("### KUALITAS: STANDAR (1)")
    st.write("Biji kopi memenuhi standar pasar lokal. Masukkan ke Gudang B.")

else:
    st.error("### KUALIITAS: CACAT/REJECT (2)")
    st.write("Biji kopi tidak layak konsumsi atau  gosong. Buang ke pembuangan limbah. ")