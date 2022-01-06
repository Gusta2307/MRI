from preprocesamiento import preprocesamiento_del_texto
import expansion_consulta
import math

def calc_w_in_q(a, q, N, n_i):
    result = []
    q_max = max(q)
    for i in range(len(q)):
        if q[i] != 0:
            result.append((a+(1-a)*q[i]/q_max)*math.log10(N/q[i]))
        else:
            result.append(0)
    return result

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

    #print("RETORNADO POR EL PARSER ->", token, '\n')
    return token
 
def isOp(text):
    return text == '(' or text == "and" or text == "or" or text == "not" or text == ")"

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def print_M(M):
    for r in M:
        print(r)

def preprocesamiento_expresion(token_list):
    palabras_relacionadas = dict()
    term_omitidos = set()
    for t in token_list:
        if t['type'] == 'terms':
            pre_result = list(preprocesamiento_del_texto(t['text']))
            if len(pre_result) > 0:
                t['text'] = pre_result[0]  
                if t['text'] not in palabras_relacionadas.keys():
                    palabras_relacionadas[t['text']] = expansion_consulta.palabras_relacionadas(t['text'])
            else:
                term_omitidos.add(t['text'])
                t['text'] = ' '
    return palabras_relacionadas, token_list, term_omitidos
            
def preprocesamiento_frase(texto):
    split_text = [item.strip() for item in texto.split(' ') if item != '']
    term_omitidos = set()
    palabras_relacionadas = dict()
    token_list = []
    for i in range(len(split_text)):
        pre_result = list(preprocesamiento_del_texto(split_text[i]))
        if len(pre_result) > 0 and len(pre_result[0]) > 0:
            token_list.append({"text": pre_result[0], "type": "terms"})
            if i + 1 < len(split_text):
                token_list.append({"text": 'and', "type": "op"})
            if pre_result[0] not in palabras_relacionadas.keys():
                palabras_relacionadas[pre_result[0]] = expansion_consulta.palabras_relacionadas(pre_result[0])
        else:
            term_omitidos.add(split_text[i])
    
    if token_list[-1]['type'] == 'op':
        token_list.pop()
    
    # print(token_list)
    # print(term_omitidos)
    # print(palabras_relacionadas)

    return palabras_relacionadas, token_list, term_omitidos




