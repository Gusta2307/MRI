import json
import preprocesamiento
class Documents:
    def __init__(self, original, preprocesado=None, raices = None):
        self.doc_original = json.loads(original.read())
        self.doc_preprocesado = {}
        self.raices_terminos = {}
        
        if preprocesado is None or raices is None:
            for d in self.doc_original:
                term, raiz = preprocesamiento.preprocesamiento_del_texto(self.doc_original[d]["texto"])
                self.doc_preprocesado[d] = list(term)
                self.raices_terminos[d] = list(raiz)
        else:
            self.doc_preprocesado = json.loads(preprocesado.read())
            self.raices_terminos = json.loads(raices.read())
        
        self.doc_count = len(self.doc_original.keys())

        self.terms = []

        self.__initialize()

    def __initialize(self):
        for d in self.doc_preprocesado.keys():
            for t in self.doc_preprocesado[d]:
                if t not in self.terms:
                    self.terms.append(t)

        self.terms.sort()
