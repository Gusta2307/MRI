import json

with open('Test Collections/cisi/CISI.REL', 'r') as f:
    dic = {}
    data = f.read()
    data_split = data.split('\n')[1:]
    # data_split = data_split[1: len(data_split)]
    temp_dic = {}
    for doc in data_split:
        
        line = [item.strip() for item in doc.split(" ") if item != ''] 
        print(line)
        if not int(line[0]) in dic.keys():
            dic[int(line[0])] = {}
        
        dic[int(line[0])][int(line[1])] =  int(line[2])





        #index_id = palabras.index(".W")
        #id = "".join(str(int(''.join(palabras[0:index_id]).strip())))
        #texto = " ".join(palabras[index_id + 1:])
        #dic['texto'] = texto
        # dic[id.strip()] = dic


    
    with open('Test Collections/cisi/result_ CISI.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)

        # print("id", id)
        # print("T", titulo)
        # print("A", autor)
        # print("B", b)
        # print("texto", texto)
    # print(len(data_split))





