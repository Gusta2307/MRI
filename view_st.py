import streamlit as st
from doc_bd import Documents
from herramienta import metodo_booleano

# def get_info(document):
#     info = ""
#     for k in document.keys:
#         info += f"{k}: "
#         for i in range(len(document.doc_original[k])):
#             if i + 1 < len(document.doc_original[k]):
#                 info += f"{document.doc_original[k][i]}, "
#             else:
#                 info += f"{document.doc_original[k][i]}"
#         info += "\n"

#     return info

st.title("Sistema de Recuperación de Información")
# uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)

coleccion = st.selectbox("Elija la coleccion de documentos a utilizar:", ["ADI", "CISI"])

if coleccion == "ADI":
    df = open("Test Collections/adi/adi_data.json")
else:
    df = open("Test Collections/cisi/cisi_data.json")

document = Documents(df)

col1, col2, col3, col4 = st.columns(4)
col_list = [col1,col2, col3, col4]

st.subheader("Términos indexados")



str_terms = """"""
temp_index = 0
# for terms in document.terms:
index_term = 0
index_cols = 0

with st.expander("Ver términos", expanded=False):
    while index_term < len(document.terms):
        str_terms += str(document.terms[index_term]).ljust(19)
        # with col_list[index_cols]:
        #     st.write(str_terms)
        index_term += 1
        # index_cols = (index_cols + 1) % len(col_list)
        temp_index += 1
        if temp_index == 4:
            # print(len(str_terms))
            str_terms += '\n'
            temp_index = 0
    st.text(str_terms)

query = st.text_input("Inserte la consulta.", "")

str_result = ""
if st.button("Submit") and query != "":
    result, doc_ok, term_omitidos = metodo_booleano(document, query)
    st.subheader("Output:")
    # str_result = "Evaluación de la consulta por documentos:\n\n"
    # for item in result:
    #     str_result += str(item) + "\n"
    # st.code(str_result)
    # str_result = ''
    if doc_ok:
        str_result += "Documentos recuperados: "
        for item in doc_ok:
            str_result += str(item) + " "
        st.success(str_result)
        list_rec = st.selectbox("Escoge el documento a ", doc_ok)
    else:
        st.error("No se recupero ningún documento")
    str_term =''
    if term_omitidos:
        str_term += f"Esta consulta contiene los siguientes términos que pueden ser considerados irrelevantes, lo cual puede afectar el resultado de la búsqueda de manera desfavorable \n"
        for term in term_omitidos:
            str_term += '- ' + str(term) + "\n"
        st.warning(str_term)




