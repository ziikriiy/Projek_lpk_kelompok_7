import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('The first number is',angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('The second number is',angka_kedua)

operasi_matematika = angka_pertama*angka_kedua
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} = {operasi_matematika}")

operasi_matematika = angka_pertama+angka_kedua
st.write(f"angka pertama {angka_pertama} + angka kedua {angka_kedua} = {operasi_matematika}")

operasi_matematika = angka_pertama-angka_kedua
st.write(f"angka pertama {angka_pertama} - angka kedua {angka_kedua} = {operasi_matematika}")
