import streamlit as st
from doc_bd import Documents
from herramienta import metodo_booleano

def get_info(document):
    info = ""
    for k in document.keys:
        info += f"{k}: "
        for i in range(len(document.doc_original[k])):
            if i + 1 < len(document.doc_original[k]):
                info += f"{document.doc_original[k][i]}, "
            else:
                info += f"{document.doc_original[k][i]}"
        info += "\n"

    return info

st.title("Sistema de Recuperacion de Informacion")
# uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
df = open("./ej_pdf.json")
document = Documents(df)


# info_document = get_info(document)
# st.code(info_document)

st.subheader("Terminos indexados")

str_terms = ''
temp_index = 0
for terms in document.terms:
    str_terms += str(terms).ljust(25)
    temp_index += 1
    if temp_index == 3:
        str_terms += '\n'
        temp_index = 0

st.text(str_terms)

metodo = st.selectbox("Elija el metodo que desea utilizar:", ["Booleano", "Vectorial", "Probabilistico"])

query = st.text_input("Inserte la consulta.", "")

str_result = ""
if st.button("Submit") and query != "":
    if metodo == "Booleano":
        result, doc_ok, term_omitidos = metodo_booleano(document, query)
        st.subheader("Output:")
        str_result = "Evaluacion de la consulta por documentos:\n\n"
        for item in result:
            str_result += str(item) + "\n"
        st.code(str_result)
        str_result = ''
        if doc_ok:
            str_result += "\nDocumentos recuperados: \n"
            for item in doc_ok:
                str_result += str(item) + "\n"
            st.success(str_result)
        else:
            st.error("No se recupero ningun documento")
        str_term =''
        if term_omitidos:
            str_term += f"Esta consulta contiene los siguientes terminos que pueden ser considerados irrelevantes, lo cual puede afectar el resultaddo de la busqueda de manera desfavorable \n"
            for term in term_omitidos:
                str_term += '- ' + str(term) + "\n"
            st.warning(str_term)
    elif metodo == "Vectorial":
        result = document.metodo_vectorial(query)
        str_result += "\nDocumentos recuperados: \n"
        for item in result:
            str_result += str(item) + "\n"
        st.code(str_result)
    else:
        st.error("El metodo seleccionado aun no esta implementado.")




