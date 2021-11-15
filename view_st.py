from numpy import str_
import streamlit as st
from doc_bd import Documents
import pandas

st.title("Sistema de Recuperaci\'on de Informaci\'on")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
df = None
print(uploaded_file)
if uploaded_file != None:
    df = pandas.read_csv(uploaded_file)
    st.table(df)

metodo = st.selectbox("Elija el m\'etodo que desea utilizar:", ["Booleano", "Vectorial", "Probabilistico"])

query = st.text_input("Inserte la consulta.", "")
print("query", query)
if st.button("Submit") and uploaded_file != None and query != "":
    document = Documents(df)
    if metodo == "Booleano":
        result, doc_ok = document.metodo_booleano(query)
        print(result)
        st.subheader("Output:")
        str_result = "Evaluaci\'on de la consulta por documentos:\n\n"
        for item in result:
            str_result += str(item) + "\n"
        str_result += "\nDocumentos recuperados: \n"
        for item in doc_ok:
            str_result += str(item) + "\n"
        st.code(str_result)
    else:
        st.error("El metodo seleccionado aun no esta implementado.")
