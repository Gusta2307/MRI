import json
from doc_bd import Documents
from motor_de_busqueda import *

text = open("Test Collections/cisi/cisi_data.json")

doc = Documents(text)

with open('Test Collections/cisi/cisi_data_prep_raiz.json', 'w', encoding='utf-8') as f:
    json.dump(doc.raices_terminos, f, ensure_ascii=False, indent=4)