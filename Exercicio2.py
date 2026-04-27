with open('C:\\Users\\ESEN\\Desktop\\Ficheiros\\passatempos.txt', 'r', encoding='utf-8') as f:
    dicionario = {}
    nomes_pts = f.readlines()
    for nome_pt in nomes_pts:
        # Remover \ns
        if '\n' in nome_pt:
            nome_pt = nome_pt.rstrip('\n')
        # Descobrir o n de palavras e adcionar ao dicionário
        nome_pt = nome_pt.split(':')
        nome_pt[1] = nome_pt[1].strip().split(' ')
        dicionario[nome_pt[0]] = len(nome_pt[1])
    # Saída de dados
    for c, v in dicionario.items():
        print(f'{c}: {v}')
