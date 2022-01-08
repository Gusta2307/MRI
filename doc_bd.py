from collections import Counter
from utils import truncate
import json
import preprocesamiento
class Documents:
    def __init__(self, document):
        self.doc_original = json.loads(document.read())
        # print (self.doc_original)

        

        self.doc_preprocesado = {doc : preprocesamiento.preprocesamiento_del_texto(self.doc_original[doc]["texto"]) for doc in self.doc_original}


        # print(self.doc_preprocesado)


        #print(self.doc_preprocesado)
        # Para obtener las dimensiones de la matriz
        self.doc_count = len(self.doc_original.keys())
        #self.terms_count = len(self.doc_original.columns)

        ####CREO QUE ESTO YA NO HACE FALTA
        #Para obtener por la relacion documento-termino
        #self.dic = {} 
        
        #Para guardar todos los terminos
        self.terms = []

        #self.keys = []

        self.__initialize()

        #print("\nterms:", self.terms, '\n')
        # print("keys", self.keys)
        # print("dic", self.dic)
        
        #Tablas

       # self.frec_i_j = frec_ij(self.terms, self.dic)
#
        #self.f_i_j = f_ij(self.frec_i_j)
#
        #self.idf_i, self.n_i = idf_i(len(self.keys), self.terms, self.dic)
#
        #self.w_i_j = w_ij(self.f_i_j, self.idf_i) 


    def __initialize(self):
        for d in self.doc_original.keys():
            # self.keys.append(d)
            list_term_ocurr = list(Counter(self.doc_preprocesado[d]).items())
            list_term_ocurr.sort(key = lambda x: x[0])
            # self.dic.update({d: list_term_ocurr})
            for t,_ in list_term_ocurr:
                if t not in self.terms:
                    self.terms.append(t)

        self.terms.sort()

#def frec_ij(terms, dic):
#    result = []
#    for key in dic.keys():
#        temp = []
#        for term in terms:
#            ocurr_temp = 0
#            for t,o in dic[key]:
#                if term == t:
#                    ocurr_temp = o
#                    break
#            temp.append(ocurr_temp)
#        result.append(temp)
#    return result
#                
#def f_ij(frec):
#    return [[i/max(item) for i in item] for item in frec]
#
#def idf_i(N, terms, dic):
#    result = []
#    n_i = []
#    #print(terms)
#    for term in terms:
#        n = 0
#        for key in dic.keys():
#            for t,_ in dic[key]:
#                if t == term:
#                    n += 1
#                    
#        result.append(truncate(math.log10(N/n),4))
#        n_i.append(n)
#    return result, n_i
#
#def w_ij(f_ij, idf_i):
#    result = []
#    for i in range(len(f_ij)):
#        temp = []
#        for j in range(len(idf_i)):
#            temp.append(f_ij[i][j]*idf_i[j])
#        result.append(temp)
#    return result
#     