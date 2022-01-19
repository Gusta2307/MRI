import json
from doc_bd import Documents
from motor_de_busqueda import *
from datetime import datetime

text = open("Test Collections/cisi/cisi_data.json")
text_prep = open("Test Collections/cisi/cisi_data_prep.json")

doc = Documents(text)

# result = json.loads(open("Test Collections/cisi/result_CISI.json").read())

 
# def main():
#     print(metodo_booleano(doc, 'computer and the'))


# if __name__ == '__main__':
#     main()