import math
from tkinter.messagebox import NO
from itsdangerous import exc
from nltk.util import pr
from utils import *
from doc_bd import Documents
import preprocesamiento
import expansion_consulta

def metodo_booleano(doc, query):    
    doc_ok = set()
    palabras_relacionadas, raices, token_list, stop_words = preprocesamiento_expresion(parser_expresiones_logicas(query)) # Se parsea la consulta    
    for d in doc.doc_preprocesado.keys(): 
        expresion = "" #expresion final
        term = "" #termino actual
        for item in token_list: # se recorre lo q devuelve el parser
            if item['type'] == "op": # verifico si es un operador
                if len(term) > 0:
                    if term != '#': # si term es > 0 => estoy analizando un termino
                        # try:
                        expansion = expansion_consulta.contiene_palabra(palabras_relacionadas[term], doc.doc_preprocesado[d])
                        raiz = raices[term] in doc.raices_terminos[d]
                        expresion += f"{str(1)} " if (expansion or raiz) else f"{str(0)} "
                        # except:
                        #     return None, None, False
                        term = "" # restablezco term
                    else:
                        expresion += '0 '
                expresion += f"{item['text']} " # le concateno el operador correspondiente a expresion
            else:
                term += item['text'] if len(term) == 0 else f" {item['text']}" # concateno los terminos, si es que hay un termino de mas de una palabra, Ejemplo: "ice cream"
        
        if len(term) > 0: # verifico si tengo un termino sin analizar
            if term != '#':
                # try:
                expansion = expansion_consulta.contiene_palabra(palabras_relacionadas[term], doc.doc_preprocesado[d])
                raiz = raices[term] in doc.raices_terminos[d]
                expresion += f"{str(1)} " if (expansion or raiz) else f"{str(0)} "
                # except:
                #     return None, None, False
            else:
                expresion += '0 '
        
        if int(eval(expresion)): # se evalua la expresion
            doc_ok.add(d)
            
    return doc_ok, stop_words, True

