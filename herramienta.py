import math
from utils import *
from doc_bd import Documents
import preprocesamiento
import expansion_consulta

def metodo_booleano(doc, query):
    result = []
    doc_ok = []
    palabras_relacionadas, token_list, term_omitidios = preprocesamiento_expresion(parser(query)) # Se parsea la consulta    

    for d in doc.doc_preprocesado.keys(): 
        expresion = "" #expresion final
        term = "" #termino actual
        for item in token_list: # se recorre lo q devuelve el parser
            if item['type'] == "op": # verifico si es un operador
                if len(term) > 0: # si term es > 0 => estoy analizando un termino
                    expresion += f"{str(expansion_consulta.contiene_palabra(palabras_relacionadas[term], doc.doc_preprocesado[d]))} " # busco en la matriz el valor del termino en el documento d y se lo agrego a la expresion final
                    term = "" # restablezco term
                expresion += f"{item['text']} " # le concateno el operador correspondiente a expresion
            else:
                term += item['text'] if len(term) == 0 else f" {item['text']}" # concateno los terminos, si es que hay un termino de mas de una palabra, Ejemplo: "ice cream"
        
        if len(term) > 0: # verifico si tengo un termino sin analizar
            expresion += f"{str(expansion_consulta.contiene_palabra(palabras_relacionadas[term], doc.doc_preprocesado[d]))} "

        evaluacion = int(eval(expresion)) # se evalua la expresion
        result.append(f"{d}: {expresion} ->  {evaluacion} " + ("OK!" if evaluacion else ""))
        if evaluacion:
            doc_ok.append(d)
    return result, doc_ok, term_omitidios

def metodo_vectorial(doc, query):
    a = 0.5

    query = query.replace('[', '')
    query = query.replace(']', '')
    query = query.split(',')

    q = []
    for i in query:
        q.append(int(i))

    w_iq = calc_w_in_q(a, q, doc.doc_count, doc.n_i)

    print(w_iq)

    sum_w_i_j = []
    for j in range(doc.doc_count):
        temp_sum = 0
        n = 0
        d1 = 0
        d2 = 0
        for i in range(len(doc.terms)):
            n += doc.w_i_j[j][i]*w_iq[i]
            d1 += math.pow(doc.w_i_j[j][i],2)
            d2 += math.pow(w_iq[i], 2)

        temp_sum = n/(math.sqrt(d1)*math.sqrt(d2))
            
        sum_w_i_j.append((temp_sum, doc.keys[j]))

    sum_w_i_j.sort(key= lambda x: x[0], reverse=True)

    print(sum_w_i_j)

    result = []
    q1 = []
    for q0,d in sum_w_i_j:
        result.append(d)
        q1.append(q0)

    return result, q1

def rocchio(doc, rel, q):
    alpha = 1
    beta = 0.75
    gamma = 0.15

    prom_r = [0 for _ in range(len(doc.terms))]
    prom_nr = [0 for _ in range(len(doc.terms))]

    for i in range(len(rel)):
        for j in range(len(doc.terms)):
            if rel[i]:
                prom_r[j] += doc.w_i_j[i][j]
            else:
                prom_nr[j] += doc.w_i_j[i][j]

    prom_r = [prom_r[i]/rel.count(1) for i in range(len(prom_r))]
    prom_nr = [prom_nr[i]/rel.count(0) for i in range(len(prom_nr))]

    result = []

    for i in range(len(doc.terms)):
        result.append(alpha*q[i] + beta*prom_r[i] - gamma*prom_nr[i])

    d_q = list(zip(doc.keys, result))

    d_q.sort(key= lambda x: x[1], reverse=True)

    result = []
    q1 = []
    for d,q0 in d_q:
        result.append(d)
        q1.append(q0)

    return result, q1

