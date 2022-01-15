from collections import Counter
from utils import truncate
import json
import preprocesamiento
class Documents:
    def __init__(self, original, preprocesado=None):
        self.doc_original = json.loads(original.read())
        
        if preprocesado is None:
            self.doc_preprocesado = {str(doc) : list(preprocesamiento.preprocesamiento_del_texto(self.doc_original[doc]["texto"])) for doc in self.doc_original}
        else:
            self.doc_preprocesado = json.loads(preprocesado.read())
        
        self.doc_count = len(self.doc_original.keys())

        self.terms = []

        self.__initialize()

    def __initialize(self):
        for d in self.doc_original.keys():
            list_term_ocurr = list(Counter(self.doc_preprocesado[d]).items())
            list_term_ocurr.sort(key = lambda x: x[0])
            for t,_ in list_term_ocurr:
                if t not in self.terms:
                    self.terms.append(t)

        self.terms.sort()
