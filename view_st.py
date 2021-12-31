import streamlit as st
from doc_bd import Documents

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
df = open("./ej_pdf1.json")
document = Documents(df)


info_document = get_info(document)
st.code(info_document)


metodo = st.selectbox("Elija el metodo que desea utilizar:", ["Booleano", "Vectorial", "Probabilistico"])

st.text(document.terms)
query = st.text_input("Inserte la consulta.", "")

str_result = ""
if st.button("Submit") and query != "":
    if metodo == "Booleano":
        result, doc_ok = document.metodo_booleano(query)
        st.subheader("Output:")
        str_result = "Evaluacion de la consulta por documentos:\n\n"
        for item in result:
            str_result += str(item) + "\n"
        str_result += "\nDocumentos recuperados: \n"
        for item in doc_ok:
            str_result += str(item) + "\n"
        st.code(str_result)
    elif metodo == "Vectorial":
        result = document.metodo_vectorial(query)
        str_result += "\nDocumentos recuperados: \n"
        for item in result:
            str_result += str(item) + "\n"
        st.code(str_result)
    else:
        st.error("El metodo seleccionado aun no esta implementado.")




