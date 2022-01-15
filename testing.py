import json
from doc_bd import Documents
from herramienta import *
from datetime import datetime

text = open("Test Collections/cisi/cisi_data.json")
text_prep = open("Test Collections/cisi/cisi_data_prep.json")
print("A")
doc = Documents(text, text_prep)
print("B")
querys = json.loads(open("Test Collections/adi/adi_query_bln.json").read())

result = json.loads(open("Test Collections/cisi/result_CISI.json").read())

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

pre = 0
re = 0
index = 0
cant_rr = 0
time = 0
for q in querys.keys():
    REL = set() # Conjunto de los documentos relevantes
    #REC = set() # Conjunto de los documentos recuperados 
    #RR = set()  # Conjunto de los documnentos relevantes recuperados 
    #NN = set()  # Conjunto de los documentos no relevantes no recuperados
    if q in result:
        index += 1
        REL = set(result[q].keys())
        # for d in result[q].keys():
        #     if result[q][d] != -1:
        #         REL.add(d)
    

        #print(querys[q]['texto']) 
        #print(doc)
        print("\n---------------------------------------------------")
        print(q)

        current_time = datetime.now()
        a, REC, b = metodo_booleano(doc, querys[q]['texto'])
        current_time = datetime.now() - current_time
        time += current_time.seconds
        # print("REC", len(REC))
        # print("REL", len(REL))
        RR = REL & REC
        cant_rr += len(RR)
        RI = REC - RR
        NR = REL - RR
        print(f"Time", current_time.seconds)
        print("RR", len(RR))
        print("RI", len(RI))
        print("NR", len(NR))
        NI = set(doc.doc_preprocesado.keys()) - (REL | REC)
        print("NI", len(NI))
        # print(f"RR: {RR}\nRI: {RI}\n" )
        p =  precision(RR, RI)
        r =  recobrado(RR, NR)
        pre += p
        re += r

        print("precision", p)
        print("recobrado", r) 
        # break

print("\nPrecision promedio", pre/index)
print("recobrado promedio", re/index)
print("RR promedio", cant_rr/index)
print("Time", time/index)

print(index,  len(querys.keys()))


# Precision promedio 0.11975553817133362
# recobrado promedio 0.5114872777323042
# Fallout promedio 0.21334758764532316

# Precision promedio 0.11970802470918601
# recobrado promedio 0.5043444205894471
# Fallout promedio 0.21200953176181275