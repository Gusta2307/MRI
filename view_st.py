import streamlit as st

import pandas

st.title("Aqui va un titulo")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)

metodo = st.selectbox("Elija el metodo que desea utilizar", ["Booleno", "Vectorial", "Probabilistico"])