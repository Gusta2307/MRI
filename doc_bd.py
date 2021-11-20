from collections import Counter
import math
import json

class Documents:
    def __init__(self, document):
        self.doc_original = json.loads(document.read())['documents'][0]

        # Para obtener las dimensiones de la matriz
        self.doc_count = len(self.doc_original.keys())
        #self.terms_count = len(self.doc_original.columns)

        #Para obtener por la relacion documento-termino
        self.dic = {} 

        #Para guardar todos los terminos
        self.terms = []

        self.keys = []

        self.__initialize()
        
        #Tablas

        self.frec_i_j, self.presence_matrix = frec_ij(self.terms, self.dic)

        self.f_i_j = f_ij(self.frec_i_j)

        self.idf_i = idf_i(len(self.keys), self.terms, self.dic)

        self.w_i_j = w_ij(self.f_i_j, self.idf_i)

        # Matriz de incidencia de documento-termino que representa la lista de todos los terminos distintos
        # y su presencia en cada documento (vector de incidencia)
        
        # self.presence_matrix = []
        # self.__initialize_presence_matrix()
    

    def __initialize(self):
        for d in self.doc_original.keys():
            self.keys.append(d)
            list_term_ocurr = list(Counter(self.doc_original[d]).items())
            list_term_ocurr.sort(key = lambda x: x[0])
            self.dic.update({d: list_term_ocurr})
            for t,_ in list_term_ocurr:
                if t not in self.terms:
                    self.terms.append(t)

        self.terms.sort()
        
    def __initialize_presence_matrix(self):
        for d in range (self.doc_count):
            temp = []
            for t in range (len(self.terms)):

                temp.append(int(self.terms[t] in self.dic[self.keys[d]]))

            self.presence_matrix.append(temp) 
              
    def parser(self, text):
        token = []
        current = ""
        parent_open = 0
        for i in range(len(text)): 
            if text[i] == " " or text[i] == "(" or text[i] == ")":
                if len(current) > 0:
                    if isOp(current):
                        token.append({"text": current, "type": "op"})
                    else:
                        token.append({"text": current, "type": "terms"})
                
                current = ""
                if text[i] == "(":
                    parent_open += 1
                    token.append({"text": text[i], "type": "op"})
                elif text[i] == ")":
                    parent_open -= 1
                    token.append({"text": text[i], "type": "op"})
                    if parent_open < 0:
                        raise "Parentesis no balanceado"
            else:
                current+= text[i]
                    
        if len(current) > 0:
            token.append({"text": current, "type": "terms"})
        
        if parent_open < 0:
            raise "Parentesis no balanceado"

        print("RETORNADO POR EL PARSER ->", token)
        return token
            
    def metodo_booleano(self, query):
        result = []
        doc_ok = []
        token_list = self.parser(query) # Se parsea la consulta
        for d in range(self.doc_count): 
            expresion = "" #expresion final
            term = "" #termino actual
            for item in token_list: # se recorre lo q devuelve el parser
                if item['type'] == "op": # verifico si es un operador
                    if len(term) > 0: # si term es > 0 => estoy analizando un termino
                        value = -1
                        try: # hago esto xq sino el termino no esta da excepcion
                            value = self.terms.index(term) # indexof
                        except:
                            pass

                        expresion += f"{str(self.presence_matrix[d][value]) if value != -1 else str(0)} " # busco en la matriz el valor del termino en el documento d y se lo agrego a la expresion final
                        term = "" # restablezco term
                    expresion += f"{item['text']} " # le concateno el operador correspondiente a experesion
                else:
                    term += item['text'] if len(term) == 0  else f" {item['text']}" # concateno los terminos, si es que hay un termino de mas de una palabra, Ejemplo: "ice cream"
            
            if len(term) > 0: # verifico si tengo un termino sin analizar
                value = -1
                try:
                    value = self.terms.index(term)
                except:
                    pass

                expresion += f"{str(self.presence_matrix[d][value]) if value != -1 else str(0)} "

            evaluacion = int(eval(expresion)) # se evalua la expresion
            result.append(f"{self.keys[d]}: {expresion} ->  {evaluacion} " + ("OK!" if evaluacion else ""))
            if evaluacion:
                doc_ok.append(self.keys[d])
        return result, doc_ok

    def __str__(self) -> str:
        print(self.dic)
        print(self.terms)
        print(self.presence_matrix)
        return ""
    
    def metodo_vectorial(self, query):

        return 0


def frec_ij(terms, dic):
    result = []
    matriz = []
    for key in dic.keys():
        temp = []
        temp_row = []
        for term in terms:
            ocurr_temp = 0
            for t,o in dic[key]:
                if term == t:
                    ocurr_temp = o
                    break
            temp.append(ocurr_temp)
            temp_row.append(1 if ocurr_temp > 0 else 0)
        matriz.append(temp_row)
        result.append(temp)
    return result, matriz
                
def f_ij(frec):
    return [[i/max(item) for i in item] for item in frec]

def idf_i(N, terms, dic):
    result = []
    for term in terms:
        n = 0
        for key in dic.keys():
            for t,_ in dic[key]:
                if t == term:
                    n += 1
        result.append(truncate(math.log10(N/n),2))
    return result

def w_ij(f_ij, idf_i):
    result = []
    for i in range(len(f_ij)):
        temp = []
        for j in range(len(idf_i)):
            temp.append(f_ij[i][j]*idf_i[j])
        result.append(temp)
    return result




def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def isOp(text):
    return text == '(' or text == "and" or text == "or" or text == "not" or text == ")"