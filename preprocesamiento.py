from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import spacy
import nltk
import string
import gensim 

nltk.download('stopwords')
nltk.download('wordnet')

nlp = spacy.load('en_core_web_sm')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = (set(stopwords.words('english')) | set(gensim.parsing.preprocessing.STOPWORDS)) - set(['computer', 'system', 'call', 'amount']) 

def tokenizacion(texto):
    p = string.punctuation
    result = ""
    for i in texto:
        result += i if not i in p else " "
    doc = nlp(result)
    tokens = [t.orth_ for t in doc]
    return tokens

def limpieza_del_texto_y_normalizacion(tokens):
    doc = nlp(tokens)
    lexical_tokens = [t.orth_.lower() for t in doc if not t.is_punct and not t.orth_.lower() in stop_words and (len(t.orth_.lower()) > 1 or t.orth_.isnumeric())]
    return lexical_tokens

def lematizacion(tokens):
    doc = nlp(tokens)
    lemas = [lemmatizer.lemmatize(str(tok), pos='v') for tok in doc]
    return lemas

def convertir_en_raices(tokens):
    stems = [stemmer.stem(token) for token in tokens]
    return stems

def preprocesamiento_del_texto(texto):
    tokens = tokenizacion(texto)
    tokens = limpieza_del_texto_y_normalizacion(" ".join(tokens))
    tokens = lematizacion(" ".join(tokens))
    term = [item for item in tokens if not item.isspace()]
    return set(term), set(convertir_en_raices(term))

