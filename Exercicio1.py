with open("C:\\Users\\ESEN\\Desktop\\Problema03\\Exercício1.txt", 'r', encoding='utf-8') as f:
    lista = []
    for nome in f.readlines():
        nome = nome.strip('\n')
        lista.append(nome)
    lista = set(lista)
    lista = list(lista)
    lista.sort()
    print(lista)
