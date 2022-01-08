import json
from doc_bd import Documents
from herramienta import *

text = open("Test Collections/adi/adi_data.json")

doc = Documents(text)

querys = json.loads(open("Test Collections/adi/adi_query_bln.json").read())

result = json.loads(open("Test Collections/adi/result_ADI.json").read())

# print(len(querys.keys()))

def precision(RR, RI):
    try:
        return len(RR)/len(RR | RI)
    except :
        print ("NO DEVOLVIO DOCUMENTOS")
        return 0

def recobrado(RR, NR):
    try:
        return len(RR)/ len(RR | NR)
    except:
        return 0

def fallout(RI, NI):
    try:
        return len(RI)/len(RI | NI)
    except:
        return 0

pre = 0
re = 0
fall = 0
for q in querys.keys():
    REL = set() # Conjunto de los documentos relevantes
    #REC = set() # Conjunto de los documentos recuperados 
    #RR = set()  # Conjunto de los documnentos relevantes recuperados 
    #NN = set()  # Conjunto de los documentos no relevantes no recuperados
    if q in result:
        for d in result[q].keys():
            if result[q][d] != -1:
                REL.add(d)
    

        #print(querys[q]['texto']) 
        #print(doc)
        print("\n---------------------------------------------------")
        print(q)

        a, REC, b = metodo_booleano(doc, querys[q]['texto'], 1)
        print("REC", REC)
        print("REL", REL)
        RR = REL & REC
        RI = REC - RR
        NR = REL - RR
        NI = set(doc.doc_preprocesado.keys()) - (REL | REC)
        print(f"RR: {RR}\nRI: {RI}\nNR: {NR}\nNI: {NI}\n" )
        p =  precision(RR, RI)
        r =  recobrado(RR, NR)
        f = fallout(RI, NI)
        pre += p
        re += r
        fall += f
        print("precision", p)
        print("recobrado", r) 
        print('fallout', f)
        # break

print("\nPrecision promedio", pre/len(querys.keys()))
print("recobrado promedio", re/len(querys.keys()))
print("Fallout promedio", fall/len(querys.keys()))
