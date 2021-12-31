from nltk.util import pr
import spacy
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer

nlp = spacy.load('en_core_web_sm')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def tokenizacion(texto):
    doc = nlp(texto) # Crea un objeto de spacy tipo nlp
    tokens = [t.orth_ for t in doc] # Crea una lista con las palabras del texto
    return tokens

def limpieza_del_texto(tokens):
    doc = nlp(tokens)
    lexical_tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
    return lexical_tokens

def normalizacion(tokens):
    filtered_sentence = [w.lower() for w in tokens if not w.lower() in stop_words]
    return filtered_sentence

def lematizacion(tokens):
    doc = nlp(tokens)
    lemas = [lemmatizer.lemmatize(str(tok), pos='v') for tok in doc]
    return lemas

def convertir_en_raices(tokens):
    stems = [stemmer.stem(token) for token in tokens]
    return stems
    
def preprocesamiento_del_texto(texto):
    tokens = tokenizacion(texto)
    
    tokens = limpieza_del_texto(" ".join(tokens))
    
    tokens = normalizacion(tokens)
    
    tokens = lematizacion(" ".join(tokens))

    return set(tokens)
