

class Documents:
    def __init__(self, document):
        self.doc_original = document

        # Para obtener las dimensiones de la matriz
        self.doc_count, self.terms_count = len(self.doc_original), len(self.doc_original.columns)

        #Para obtener por la relacion documento-termino
        self.dic = {}

        #Para guardar todos los terminos
        self.terms = []

        self.keys = []

        self.__initialize()

        # Matriz de incidencia de documento-termino que representa la lista de todos los terminos distintos
        # y su presencia en cada documento (vector de incidencia)
        
        self.presence_matrix = []
        self.__initialize_presence_matrix()
    

    def __initialize(self):
        key = ""
        for r in range(self.doc_count):
            for c in range (self.terms_count):
                if c == 0:
                    key = self.doc_original.loc[r].iat[c]
                    self.keys.append(key)
                    self.dic.update({key: []})
                else:
                    self.dic[key].append(self.doc_original.loc[r].iat[c])

                    if self.doc_original.loc[r].iat[c] not in self.terms:
                        self.terms.append(self.doc_original.loc[r].iat[c])

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
        print("Introduzca la consulta")
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
    

def isOp(text):
    return text == '(' or text == "and" or text == "or" or text == "not" or text == ")"