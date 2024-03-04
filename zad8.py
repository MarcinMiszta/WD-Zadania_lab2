lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, '10', '11', '12', '13', '14', 'bb', 5, 6, 7, 8, 9, '11', '12', '13']
dic = {}
print(lista)
for i in lista:
    dic[i] = dic.get(i, 0) + 1
print(dic)
keys_delete = [key for key in dic if not isinstance(key, (int, float))]
for key in keys_delete:
    del dic[key]
print(dic)
