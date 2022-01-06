import json

with open('cran.qry', 'r') as f:
    dic = {}
    data = f.read()
    data_split = data.split('.I')[1:]
    # data_split = data_split[1: len(data_split)]
    for doc in data_split:
        temp_dic = {}
        palabras =  doc.split("\n")
        index_id = palabras.index(".W")
        id = "".join(str(int(''.join(palabras[0:index_id]).strip())))
        texto = " ".join(palabras[index_id + 1:])
        temp_dic['texto'] = texto
        dic[id.strip()] = temp_dic


    
    with open('query.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)

        # print("id", id)
        # print("T", titulo)
        # print("A", autor)
        # print("B", b)
        # print("texto", texto)
    # print(len(data_split))




