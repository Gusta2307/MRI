from functools import partial
import math

from nltk.util import pr
from utils import *
from doc_bd import Documents
import preprocesamiento
import expansion_consulta

def metodo_booleano(doc, query, parse):    
    result = []
    doc_ok = set()
    palabras_relacionadas, token_list, term_omitidios = preprocesamiento_expresion(parser_expresiones_logicas(query)) if parse else preprocesamiento_frase(query) # Se parsea la consulta    
    for d in doc.doc_preprocesado.keys(): 
        expresion = "" #expresion final
        term = "" #termino actual
        for item in token_list: # se recorre lo q devuelve el parser
            if item['type'] == "op": # verifico si es un operador
                if len(term) > 0: # si term es > 0 => estoy analizando un termino
                    expresion += f"{str(expansion_consulta.contiene_palabra(term, doc.doc_preprocesado[d]))} " # busco en la matriz el valor del termino en el documento d y se lo agrego a la expresion final
                    term = "" # restablezco term
                expresion += f"{item['text']} " # le concateno el operador correspondiente a expresion
            else:
                term += item['text'] if len(term) == 0 else f" {item['text']}" # concateno los terminos, si es que hay un termino de mas de una palabra, Ejemplo: "ice cream"
        
        if len(term) > 0: # verifico si tengo un termino sin analizar
            expresion += f"{str(expansion_consulta.contiene_palabra(term, doc.doc_preprocesado[d]))} "

        evaluacion = int(eval(expresion)) # se evalua la expresion
        result.append(f"{d}: {expresion} ->  {evaluacion} " + ("OK!" if evaluacion else ""))
        
        # print("#"*60)

        # print("Document", doc.doc_preprocesado[d])
        # print("Palabras Rel", palabras_relacionadas)
        # print("Terminos Omitidos", term_omitidios)
        # print("Query", query)
        # print(expresion)

        # print("#"*60)

        if evaluacion:
            doc_ok.add(d)
            
    return result, doc_ok, term_omitidios

