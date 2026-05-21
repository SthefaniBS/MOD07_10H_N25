# LER FICHEIROS
import os
import sys


def capiturar_erros(ficheiro):
    try:
        with open(ficheiro, encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        with open(ficheiro, 'x+', encoding='utf-8') as f:
            if ficheiro == 'livros.txt':
                dicionario_livros = {
                    "9789720049575": {
                        "título": "Os Maias",
                        "género": "Romance",
                        "autor": "Eça de Queirós",
                        "disponível": True
                    },

                    "9789896600825": {
                        "título": "Ensaio sobre a Cegueira",
                        "género": "Ficção",
                        "autor": "José Saramago",
                        "disponível": False
                    },

                    "9789722333344": {
                        "título": "A Cidade e as Serras",
                        "género": "Romance",
                        "autor": "Eça de Queirós",
                        "disponível": True
                    },

                    "9789896412084": {
                        "título": "Memorial do Convento",
                        "género": "Romance Histórico",
                        "autor": "José Saramago",
                        "disponível": True
                    },

                    "9789723829495": {
                        "título": "O Alquimista",
                        "género": "Ficção",
                        "autor": "Paulo Coelho",
                        "disponível": False
                    },

                    "9789897732341": {
                        "título": "Harry Potter e a Pedra Filosofal",
                        "género": "Fantasia",
                        "autor": "J.K. Rowling",
                        "disponível": True
                    }
                }
                n = 0
                for isbn in dicionario_livros:
                    n += 1
                    if n == len(dicionario_livros):
                        f.write(
                            f"{isbn};{dicionario_livros[isbn]['título']};{dicionario_livros[isbn]['género']};{dicionario_livros[isbn]['autor']};{dicionario_livros[isbn]['disponível']}")
                    else:
                        f.write(
                            f"{isbn};{dicionario_livros[isbn]['título']};{dicionario_livros[isbn]['género']};{dicionario_livros[isbn]['autor']};{dicionario_livros[isbn]['disponível']}\n")

            elif ficheiro == 'alunos.txt':
                dicionario_alunos = {
                    "10001": {"nome": "Ana Silva", "estado": "A"},
                    "10002": {"nome": "Bruno Costa", "estado": "I"},
                    "10003": {"nome": "Carla Pereira", "estado": "A"},
                    "10004": {"nome": "Diogo Fernandes", "estado": "A"},
                    "10005": {"nome": "Eva Almeida", "estado": "I"},
                    "10006": {"nome": "Fábio Rocha", "estado": "A"}
                }
                n = 0
                for numero in dicionario_alunos:
                    n += 1
                    if n == len(dicionario_alunos):
                        f.write(
                            f"{numero};{dicionario_alunos[numero]['nome']};{dicionario_alunos[numero]['estado']}")
                    else:
                        f.write(
                            f"{numero};{dicionario_alunos[numero]['nome']};{dicionario_alunos[numero]['estado']}\n")

        with open(ficheiro, encoding='utf-8') as f:
            conteudo = f.read()
    except PermissionError:
        print(f'A permissão para abrir o ficheiro {ficheiro} foi negada.')
        sys.exit(1)
    return conteudo


def lerlivros():
    livros = capiturar_erros('livros.txt')
    lista_livros = livros.split('\n')
    dicionario_livros = {}
    for linha in lista_livros:
        isbn, titulo, genero, autor, disponivel = linha.strip().split(';')
        disponivel = (disponivel == 'True')
        dicionario_livros[isbn] = {
            'título': titulo, 'género': genero, 'autor': autor, 'disponível': disponivel}
    return dicionario_livros


def leralunos():
    alunos = capiturar_erros('alunos.txt')
    lista_alunos = alunos.split('\n')
    dicionario_alunos = {}
    for linha in lista_alunos:
        numero, nome, estado = linha.strip().split(';')
        dicionario_alunos[numero] = {'nome': nome, 'estado': estado}
    return dicionario_alunos


def lerrequisicoes():
    requisicoes = capiturar_erros('requisicoes.txt')
    lista_requisicoes = requisicoes.split('\n')
    return lista_requisicoes

# Essas funções são usadas no programa principal


def validaraluno(n):
    if n not in dicionario_alunos:
        return "Número não encontrado."
    else:
        if dicionario_alunos[n]['estado'] == 'I':
            return 'Este aluno está inativo na escola.'
        else:
            return 'tudo ok'


def encontrarmax_elemento_repeticoes(conjunto, lista):
    max_nrepeticoes = 0
    max_elemento = []
    for elemento in conjunto:
        repeticoes = lista.count(elemento)
        if repeticoes > max_nrepeticoes or repeticoes == max_nrepeticoes:
            max_nrepeticoes = repeticoes
            max_elemento.append(elemento)
    return max_elemento, max_nrepeticoes


# PROGRAMA PRINCIPAL
dicionario_livros = lerlivros()
dicionario_alunos = leralunos()
lista_requisicoes = lerrequisicoes()
z = 0
menu = input("1- Listar livros disponíveis\n2- Requisitar livro\n3- Devolver livro\n4- Livro mais requisitado do mês\n5-Aluno que mais requisitou no ano\n6-Género mais requisitado\n: ")

if menu == '1':

    print('|\tLIVROS DISPONÍVEIS\t|\n')
    for chave in dicionario_livros:
        if dicionario_livros[chave]['disponível'] == True:
            print(
                f"ISBN: {chave}\nTítulo: {dicionario_livros[chave]['título']}\nGénero: {dicionario_livros[chave]['género']}\nAutor: {dicionario_livros[chave]['autor']}\n\n")


if menu == '2':
    z = 5
    nAluno = input("Número do aluno: ")

    if validaraluno(nAluno) == 'tudo ok':
        isbn = input("ISBN do livro: ").strip()
        if isbn not in dicionario_livros:
            print("ISBN não encontrado: Não temos esse livro.")
        else:
            requisicao_data = input(
                "Data da requisição (dd/mm/aaaa): ").strip()

            for chave in dicionario_livros:
                if chave == isbn and dicionario_livros[chave]['disponível'] == False:
                    print("Livro indisponível para requisição.")
                elif chave == isbn and dicionario_livros[chave]['disponível'] == True:
                    lista_requisicoes.append(
                        f"{nAluno};{isbn};{requisicao_data};{dicionario_livros[chave]['género']}")
                    dicionario_livros[chave]['disponível'] = False
    else:
        print(validaraluno(nAluno))


elif menu == '3':
    nAluno = input('Número do aluno: ')

    if validaraluno(nAluno) == 'tudo ok':
        nAlunos = set()
        isbn = input("ISBN do livro: ").strip()
        if isbn not in dicionario_livros:
            print("ISBN não encontrado: Não temos esse livro.")
        else:
            requisicao_data = input(
                "Data da requisição (dd/mm/aaaa): ").strip()

            for linha in lista_requisicoes:
                numero, isbn_req, data, genero = linha.split(';')
                nAlunos.add(numero)

            if nAluno not in nAlunos:
                print('OPERAÇÃO INVÁLIDA: ISBN não encontrado.')
            else:
                dicionario_livros[isbn]['disponível'] = True

    else:
        print(validaraluno(nAluno))

elif menu == '4':

    if len(lista_requisicoes) == 1 and lista_requisicoes[0] == '':
        print('Nenhum livro foi requisitado ainda.')
    else:
        livros_mes = []
        for linha in lista_requisicoes:
            numero, isbn, data, genero = linha.split(';')
            data = data.split('/')
            if data[1] == '05' or data[1] == '5':
                livros_mes.append(isbn)

        set_livros_mes = set(livros_mes)
        # Esta função vai encontrar o livro mais requisitado do mês
        max_livro, total_req = encontrarmax_elemento_repeticoes(
            set_livros_mes, livros_mes)

        print(
            f'O livro mais requisitado do mês foi {max_livro} com {total_req} requisições.')

elif menu == '5':
    if len(lista_requisicoes) == 1 and lista_requisicoes[0] == '':
        print('Nenhum livro foi requisitado ainda.')
    else:
        nalunos = []
        for linha in lista_requisicoes:
            numero, isbn, data, genero = linha.split(';')
            data = data.split('/')
            if data[2] == '2026' or data[2] == '2026':
                nalunos.append(numero)

        set_nalunos = set(nalunos)
        # Esta função vai encontrar o aluno que mais requisitou livros.
        aluno, total_req = encontrarmax_elemento_repeticoes(
            set_nalunos, nalunos)

        print(f'{aluno} requisitou um total de {total_req} livros.')

elif menu == '6':
    if len(lista_requisicoes) == 1 and lista_requisicoes[0] == '':
        print('Nenhum livro foi requisitado ainda.')
    else:
        generos = []
        for linha in lista_requisicoes:
            numero, isbn, data, genero = linha.split(';')
            generos.append(genero)

        set_generos = set(generos)
        genero, total_rep = encontrarmax_elemento_repeticoes(
            set_generos, generos)

        print(f'{genero} com {total_rep} requisições.')

# ATUALIZAR OS FICHEIROS
if menu != '1':  # Porque quando o menu é 1 eu apenas mostro o conteúdo do ficheiro livros.txt
    with open('livros.txt', 'w', encoding='utf-8') as livros:
        for isbn in dicionario_livros:
            livros.write(
                f"{isbn};{dicionario_livros[isbn]['título']};{dicionario_livros[isbn]['género']};{dicionario_livros[isbn]['autor']};{dicionario_livros[isbn]['disponível']}\n")

    with open('requisicoes.txt', 'w', encoding='utf-8') as requisicoes:
        for linha in lista_requisicoes:
            requisicoes.write(linha)
