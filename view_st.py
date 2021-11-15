import streamlit as st

st.title("Aqui va un titulo")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)