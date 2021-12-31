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

def parser(text):
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

from preprocesamiento import preprocesamiento_del_texto
import expansion_consulta


def preprocesamiento_expresion(token_list):
    palabras_relacionadas = dict()
    term_omitidos = set()
    for t in token_list:
        if t['type'] == 'terms':
            pre_result = list(preprocesamiento_del_texto(t['text']))
            if len(pre_result) > 0:
                t['text'] = pre_result[0]  
            else:
                term_omitidos.add(t['text'])
                t['text'] = ' '


            if t['text'] not in palabras_relacionadas.keys():
                palabras_relacionadas[t['text']] = expansion_consulta.palabras_relacionadas(t['text'])
    return palabras_relacionadas, token_list, term_omitidos
            


