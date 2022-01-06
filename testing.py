import json
from doc_bd import Documents
from herramienta import *

text = open("Casos de Prueba/data.json")

doc = Documents(text)

querys = json.loads(open("query.json").read())

result = json.loads(open("result.json").read())

# print(len(querys.keys()))


for q in querys.keys():
    REL = set() # Conjunto de los documentos relevantes
    REC = set() # Conjunto de los documentos recuperados 
    RR = set()  # Conjunto de los documnentos relevantes recuperados 
    NN = set()  # Conjunto de los documentos no relevantes no recuperados

    # for d in result[q].keys():
    #     if result[q][d] != -1:
    #         REL.add(d)
    

    #print(querys[q]['texto']) 
    #print(doc)
    a, REC, b = metodo_booleano(doc, querys[q]['texto'], 0)
    # RR = REL & REC
    # NN = (set(result.keys()) - REL) - REC
    break

