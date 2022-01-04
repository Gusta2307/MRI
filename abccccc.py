import json

with open('cran.all.1400', 'r') as f:
    dic = {}
    
    data = f.read()
    data_split = data.split('.I')[1:]
    # data_split = data_split[1: len(data_split)]
    for doc in data_split:
        temp_dic = {}
        palabras =  doc.split("\n")
        index_id = palabras.index(".T")
        id = " ".join(palabras[0:index_id])
        index_t = palabras.index(".A") 
        titulo = " ".join(palabras[index_id + 1: index_t])
        temp_dic['titulo'] = titulo
        index_a = palabras.index(".B")
        autor = " ".join(palabras[index_t + 1: index_a])
        temp_dic['autor'] = autor
        index_b = palabras.index(".W")
        b = " ".join(palabras[index_a + 1: index_b])
        temp_dic['b'] = b
        texto = " ".join(palabras[index_b + 1:])

        temp_dic['texto'] = texto

        dic[id.strip()] = temp_dic


    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)

        # print("id", id)
        # print("T", titulo)
        # print("A", autor)
        # print("B", b)
        # print("texto", texto)
    # print(len(data_split))


