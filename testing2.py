import json
from doc_bd import Documents
from herramienta import *

text = open("Test Collections/cisi/cisi_data.json")

doc = Documents(text)

with open('Test Collections/cisi/cisi_data_prep.json', 'w', encoding='utf-8') as f:
    json.dump(doc.doc_preprocesado, f, ensure_ascii=False, indent=4)