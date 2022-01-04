import json
from doc_bd import Documents
from herramienta import *

text = open("Casos de Prueba/data.json")

doc = Documents(text)
query = "hi computer"
print(metodo_booleano(doc, query=query))
