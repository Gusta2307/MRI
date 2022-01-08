from nltk.corpus import wordnet
from nltk.util import pr


from preprocesamiento import preprocesamiento_del_texto


def palabras_relacionadas(palabra):
    syns = wordnet.synsets(palabra) 
    palabras = set([palabra])
    for i in syns: 
        for l in i.lemmas():
            if '-' in l.name(): 
                continue
            palabras = palabras | preprocesamiento_del_texto(l.name().replace("_", " "))
    return palabras

def contiene_palabra(relacionadas, texto):
    # relacionadas = palabras_relacionadas(palabra) 
    # relacionadas.add(palabra)
    # print(f"palabras -> {palabra} -> {texto}", palabras_relacionadas(palabra))
    # print("relacionadas", relacionadas)

    
    # for p in relacionadas:
    if relacionadas in texto:
            return 1
    
    return 0
    