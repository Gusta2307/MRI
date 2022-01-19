import streamlit as st
from doc_bd import Documents
from motor_de_busqueda import metodo_booleano


st.title("Sistema de Recuperación de Información")

coleccion = st.selectbox(
    "Elija la coleccion de documentos a utilizar:", ["ADI", "CISI"])

if coleccion == "ADI":
    df = open("Test Collections/adi/adi_data.json")
    df_pre = open("Test Collections/adi/adi_data_prep.json")
    df_pre_raiz = open("Test Collections/adi/adi_data_prep_raiz.json")
else:
    df = open("Test Collections/cisi/cisi_data.json")
    df_pre = open("Test Collections/cisi/cisi_data_prep.json")
    df_pre_raiz = open("Test Collections/cisi/cisi_data_prep_raiz.json")

document = Documents(df, df_pre)

col1, col2, col3, col4 = st.columns(4)
col_list = [col1, col2, col3, col4]

st.subheader("Términos indexados")

str_terms = """"""
temp_index = 0
index_term = 0
index_cols = 0

with st.expander("Ver términos", expanded=False):
    while index_term < len(document.terms):
        str_terms += str(document.terms[index_term]).ljust(19)
        index_term += 1
        temp_index += 1
        if temp_index == 4:
            str_terms += '\n'
            temp_index = 0
    st.text(str_terms)

query = st.text_input("Inserte la consulta.", "")

str_result = ""
if st.button("Submit") and query != "":
    doc_ok, term_omitidos, ok = metodo_booleano(document, query)
    st.subheader("Output:")

    if not ok:
        st.warning('Consulta mal formulada.')
    else:
        if doc_ok:
            str_result += "Fueron recuperados algunos documentos"
            title_doc = {}
            for item in doc_ok:
                title_doc[document.doc_original[item]['titulo']] = item
            st.success(str_result)
            for item in range(len(doc_ok)):
                with st.expander(list(title_doc.keys())[item].capitalize()):
                    info_text = f"Autor: {document.doc_original[list(doc_ok)[item]]['autor']}\n\n {document.doc_original[list(doc_ok)[item]]['texto'].capitalize()}"
                    st.text_area(" ", info_text, height=150, disabled=True)
        else:
            st.error("No se recuperó ningún documento")
        str_term = ''
        if term_omitidos:
            str_term += f"Esta consulta contiene los siguientes términos que pueden ser considerados irrelevantes, lo cual puede afectar el resultado de la búsqueda de manera desfavorable \n"
            for term in term_omitidos:
                str_term += '- ' + str(term) + "\n"
            st.warning(str_term)
