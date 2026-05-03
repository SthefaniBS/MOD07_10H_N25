with open("C:\\Users\\ESEN\\Desktop\\Ficheiros\\notas.txt", 'a+', encoding='latin-1') as f:
    nome = input("Nome do aluno: ").strip().title()
    while nome != 'Fim':
        try:
            nota = int(input("Nota do aluno: "))
        except ValueError:
            print('O dado inserido é inválido.')
        f.write(f"{nome}: {nota}\n")
        nome = input("Nome do aluno: ").strip().title()
    f.seek(0)
    notas = []
    nomes = []
    linhas = f.readlines()
    for nn in linhas:
        aluno = nn.split(':')
        aluno[1] = int(aluno[1])
        notas.append(aluno[1])
        nomes.append(aluno[0])
    media = sum(notas)/len(notas)
    print(f"{round(media, 2)}")
    NotaMax = max(notas)
    print("ALUNO(S) COM A NOTA MAIS ALTA:")
    for i in range(len(notas)):
        if notas[i] == NotaMax:
            print(f"{nomes[i]}")
