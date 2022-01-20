from preprocesamiento import preprocesamiento_del_texto
import expansion_consulta

def parser_expresiones_logicas(text):
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

    return token
 
def isOp(text):
    return text == '(' or text == "and" or text == "or" or text == "not" or text == ")"

def preprocesamiento_expresion(token_list):
    palabras_relacionadas = dict()
    stop_words = set()
    raices = dict()
    for t in token_list:
        if t['type'] == 'terms':
            term, raiz = preprocesamiento_del_texto(t['text'])
            pre_result = list(term)
            if len(pre_result) > 0:
                t['text'] = pre_result[0]  
                if t['text'] not in palabras_relacionadas.keys():
                    palabras_relacionadas[t['text']] = expansion_consulta.palabras_relacionadas(t['text'])
                if t['text'] not in raices:
                    raices[t['text']] = list(raiz)[0]
            else:
                stop_words.add(t['text'])
                t['text'] = '#'
    return palabras_relacionadas, raices, token_list, stop_words
