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

            with open('Test Collections/cisi/cisi_data_prep.json', 'w', encoding='utf-8') as f:
                json.dump(self.doc_preprocesado, f, ensure_ascii=False, indent=4)
            with open('Test Collections/cisi/cisi_data_prep_raiz.json', 'w', encoding='utf-8') as f:
                json.dump(self.raices_terminos, f, ensure_ascii=False, indent=4)
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
