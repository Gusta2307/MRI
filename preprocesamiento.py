from nltk.util import pr
import spacy
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from spacy.tokens.token import Token


nlp = spacy.load('en_core_web_sm')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def tokenizacion(texto):
    doc = nlp(texto) # Crea un objeto de spacy tipo nlp
    tokens = [t.orth_ for t in doc] # Crea una lista con las palabras del texto
    return tokens

def limpieza_del_texto_y_normalizacion(tokens):
    doc = nlp(tokens)
    lexical_tokens = [t.orth_.lower() for t in doc if not t.is_punct | t.is_stop]
    return lexical_tokens

def lematizacion(tokens):
    doc = nlp(tokens)
    lemas = [lemmatizer.lemmatize(str(tok), pos='v') for tok in doc]
    return lemas

# def convertir_en_raices(tokens):
#     stems = [stemmer.stem(token) for token in tokens]
#     return stems
    
def preprocesamiento_del_texto(texto):
    tokens = tokenizacion(texto)
    print("TOKENIZACION", tokens)
    tokens = limpieza_del_texto_y_normalizacion(" ".join(tokens))
    print("LIMPIEZA", tokens, end='\n\n')
    tokens = lematizacion(" ".join(tokens))
    print('LEMATIZACION', tokens, end='\n\n')
    return set(tokens)
