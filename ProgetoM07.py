import random
import sys


# Essa função lê e trata de erros que podem ocorrer ao executar essa ação.
def ler_capiturarerros(ficheiro):
    existe = True

    try:
        with open(ficheiro, encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        existe = False
        conteudo = "O ficheiro não existe."

    except PermissionError:
        pasta, nome = ficheiro.split('\\')
        print(
            f'Erro: Não tens permissão para abrir o ficheiro {nome} da pasta {pasta}.')
        sys.exit(1)

    except UnicodeDecodeError:
        print(
            'Erro: O formato do texto não é suportado. Tenta guardar o ficheiro como UTF-8.')
        sys.exit(1)

    except Exception as erro:
        print(
            f'Erro: Ocorreu um erro inesperado ao processar o ficheiro.\nDetalhes técnicos: {erro}')
        sys.exit(1)

    return existe, conteudo


# Essa função cria novos ficheiros e retorna o conteúdo.
def criarficheiros(ficheiro):

    def escreverjogadores(dicionario, objeto_de_ficheiro):
        n = 0
        for chave in dicionario:
            n += 1
            if n == len(dicionario):
                objeto_de_ficheiro.write(
                    f'{chave}|{dicionario[chave]['nome']}|{dicionario[chave]['camisa']}|{dicionario[chave]['posição']}|{dicionario[chave]['idade']}|{dicionario[chave]['golos']}|{dicionario[chave]['cartões'][0]},{dicionario[chave]['cartões'][1]}|{dicionario[chave]['estado']}|{dicionario[chave]['jogos']}')
            else:
                objeto_de_ficheiro.write(
                    f'{chave}|{dicionario[chave]['nome']}|{dicionario[chave]['camisa']}|{dicionario[chave]['posição']}|{dicionario[chave]['idade']}|{dicionario[chave]['golos']}|{dicionario[chave]['cartões'][0]},{dicionario[chave]['cartões'][1]}|{dicionario[chave]['estado']}|{dicionario[chave]['jogos']}\n')

    def escrevertreinadores(dicionario, objeto_de_ficheiro):
        n = 0
        for t in dicionario:
            n += 1
            if n == len(dicionario):
                if dicionario[t]['estado'] == 'atual':
                    objeto_de_ficheiro.write(
                        f'{t}|{dicionario[t]['nome']}|{dicionario[t]['estado']}|{dicionario[t]['entrada']}|{dicionario[t]['jogos']}|{dicionario[t]['vitórias']}|{dicionario[t]['empates']}|{dicionario[t]['derrotas']}|{dicionario[t]['nacionalidade']}|{dicionario[t]['saída']}')
                else:
                    objeto_de_ficheiro.write(
                        f'{t}|{dicionario[t]['nome']}|{dicionario[t]['estado']}|{dicionario[t]['entrada']}|{dicionario[t]['jogos']}|{dicionario[t]['vitórias']}|{dicionario[t]['empates']}|{dicionario[t]['derrotas']}|{dicionario[t]['nacionalidade']}|{dicionario[t]['saída']}')
            else:
                if dicionario[t]['estado'] == 'atual':
                    objeto_de_ficheiro.write(
                        f'{t}|{dicionario[t]['nome']}|{dicionario[t]['estado']}|{dicionario[t]['entrada']}|{dicionario[t]['jogos']}|{dicionario[t]['vitórias']}|{dicionario[t]['empates']}|{dicionario[t]['derrotas']}|{dicionario[t]['nacionalidade']}|{dicionario[t]['saída']}\n')
                else:
                    objeto_de_ficheiro.write(
                        f'{t}|{dicionario[t]['nome']}|{dicionario[t]['estado']}|{dicionario[t]['entrada']}|{dicionario[t]['jogos']}|{dicionario[t]['vitórias']}|{dicionario[t]['empates']}|{dicionario[t]['derrotas']}|{dicionario[t]['nacionalidade']}|{dicionario[t]['saída']}\n')

    def escreverjogos(dicionario, objeto_de_ficheiro):
        n = 0
        for jogo in dicionario:
            n += 1
            if n == len(dicionario):
                objeto_de_ficheiro.write(f'{jogo}|{dicionario[jogo]['data']}|{dicionario[jogo]['hora']}|{dicionario[jogo]['adversário']}|{dicionario[jogo]['local']}|{dicionario[jogo]['golos'][0]},{dicionario[jogo]['golos'][1]}|{str(dicionario[jogo]['cartões A']).replace('[', '').replace(']', '')}|{str(dicionario[jogo]['cartões V']).replace('[', '').replace(']', '')}|{str(dicionario[jogo]['marcadores']).replace('[', '').replace(']', '')}')
            else:
                objeto_de_ficheiro.write(f'{jogo}|{dicionario[jogo]['data']}|{dicionario[jogo]['hora']}|{dicionario[jogo]['adversário']}|{dicionario[jogo]['local']}|{dicionario[jogo]['golos'][0]},{dicionario[jogo]['golos'][1]}|{str(dicionario[jogo]['cartões A']).replace('[', '').replace(']', '')}|{str(dicionario[jogo]['cartões V']).replace('[', '').replace(']', '')}|{str(dicionario[jogo]['marcadores']).replace('[', '').replace(']', '')}\n')

    def escreverestatisticas(dicionario, objeto_de_ficheiro):

        for dado in dicionario.items():
            if dado[0] == 'saldo de golos':
                objeto_de_ficheiro.write(f'{dado[1]}')
            else:
                objeto_de_ficheiro.write(f'{dado[1]}|')

    with open(ficheiro, 'x+', encoding='utf-8')as f:

        if ficheiro == 'jogadoresSaoPaulo.txt':
            jogadores1 = {
                '10001': {'nome': 'Lucas', 'camisa': '7', 'posição': 'M', 'idade': '31', 'golos': 2, 'cartões': [0, 0], 'estado': 'A', 'jogos': 3},
                '10002': {'nome': 'Calleri', 'camisa': '9', 'posição': 'A', 'idade': '30', 'golos': 3, 'cartões': [0, 0], 'estado': 'A', 'jogos': 3},
                '10003': {'nome': 'Luciano', 'camisa': '10', 'posição': 'A', 'idade': '30', 'golos': 1, 'cartões': [0, 0], 'estado': 'A', 'jogos': 3},
                '10004': {'nome': 'Pablo', 'camisa': '5', 'posição': 'M', 'idade': '22', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 2},
                '10005': {'nome': 'Rafael', 'camisa': '1', 'posição': 'G', 'idade': '34', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 3},
                '10006': {'nome': 'Beraldo', 'camisa': '35', 'posição': 'D', 'idade': '20', 'golos': 0, 'cartões': [1, 0], 'estado': 'I', 'jogos': 2},
                '10007': {'nome': 'Welington', 'camisa': '6', 'posição': 'D', 'idade': '23', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 3},
                '10008': {'nome': 'Alisson', 'camisa': '25', 'posição': 'M', 'idade': '30', 'golos': 0, 'cartões': [0, 1], 'estado': 'I', 'jogos': 2},
                '10009': {'nome': 'Rato', 'camisa': '27', 'posição': 'A', 'idade': '31', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 3},
                '10010': {'nome': 'Michel', 'camisa': '15', 'posição': 'M', 'idade': '27', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 1}
            }
            escreverjogadores(jogadores1, f)

        elif ficheiro == 'treinadoresSaoPaulo.txt':
            treinadores1 = {
                '30001': {'nome': 'Rogério Ceni', 'estado': 'antigo', 'entrada': '10/01/2025', 'jogos': 15, 'vitórias': 6, 'empates': 4, 'derrotas': 5, 'nacionalidade': 'Brasileira', 'saída': '15/04/2025'},
                '30002': {'nome': 'Dorival Júnior', 'estado': 'antigo', 'entrada': '20/04/2025', 'jogos': 20, 'vitórias': 10, 'empates': 5, 'derrotas': 5, 'nacionalidade': 'Brasileira', 'saída': '10/12/2025'},
                '30003': {'nome': 'Thiago Carpini', 'estado': 'atual', 'entrada': '15/01/2026', 'jogos': 3, 'vitórias': 2, 'empates': 1, 'derrotas': 0, 'nacionalidade': 'Brasileira', 'saída': '-'}
            }
            escrevertreinadores(treinadores1, f)

        elif ficheiro == 'jogosSaoPaulo.txt':
            jogos1 = {
                1: {'data': '10/4/2026', 'hora': '16:00', 'adversário': 'Corinthians', 'local': 'Morumbi', 'golos': [2, 0], 'cartões A': ['Pablo'], 'cartões V': [], 'marcadores': ['Lucas', 'Calleri']},
                2: {'data': '17/4/2026', 'hora': '20:00', 'adversário': 'Palmeiras', 'local': 'Allianz Parque', 'golos': [1, 1], 'cartões A': ['Beraldo'], 'cartões V': ['Alisson'], 'marcadores': ['Luciano']},
                3: {'data': '24/4/2026', 'hora': '18:30', 'adversário': 'Santos', 'local': 'Morumbi', 'golos': [3, 1], 'cartões A': ['Welington', 'Rato'], 'cartões V': [], 'marcadores': ['Lucas', 'Calleri', 'Calleri']}
            }
            escreverjogos(jogos1, f)

        elif ficheiro == 'estatisticasSaoPaulo.txt':
            estatisticas1 = {
                'pontos': 7,
                'vitórias': 2,
                'empates': 1,
                'derrotas': 0,
                'golos marcados': 6,
                'golos sofridos': 2,
                'saldo de golos': 4
            }
            escreverestatisticas(estatisticas1, f)

        elif ficheiro == 'jogadoresFlamengo.txt':
            jogadores2 = {
                '20001': {'nome': 'Pedro', 'camisa': '9', 'posição': 'A', 'idade': '26', 'golos': 3, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '20002': {'nome': 'Gabriel', 'camisa': '10', 'posição': 'A', 'idade': '27', 'golos': 1, 'cartões': [1, 0], 'estado': 'A', 'jogos': 4},
                '20003': {'nome': 'Bruno', 'camisa': '27', 'posição': 'A', 'idade': '28', 'golos': 1, 'cartões': [0, 0], 'estado': 'A', 'jogos': 3},
                '20004': {'nome': 'Arrascaeta', 'camisa': '14', 'posição': 'M', 'idade': '29', 'golos': 1, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '20005': {'nome': 'Rossi', 'camisa': '1', 'posição': 'G', 'idade': '28', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '20006': {'nome': 'Leo', 'camisa': '4', 'posição': 'D', 'idade': '28', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 4},
                '20007': {'nome': 'Ayrton', 'camisa': '6', 'posição': 'D', 'idade': '26', 'golos': 0, 'cartões': [0, 1], 'estado': 'I', 'jogos': 2},
                '20008': {'nome': 'Gerson', 'camisa': '20', 'posição': 'M', 'idade': '26', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 3},
                '20009': {'nome': 'Everton', 'camisa': '11', 'posição': 'A', 'idade': '28', 'golos': 0, 'cartões': [1, 0], 'estado': 'A', 'jogos': 4},
                '20010': {'nome': 'Pulgar', 'camisa': '5', 'posição': 'M', 'idade': '30', 'golos': 0, 'cartões': [1, 0], 'estado': 'I', 'jogos': 2}
            }
            escreverjogadores(jogadores2, f)

        elif ficheiro == 'treinadoresFlamengo.txt':
            treinadores2 = {
                '40001': {'nome': 'Jorge Sampaoli', 'estado': 'antigo', 'entrada': '10/05/2025', 'jogos': 15, 'vitórias': 7, 'empates': 4, 'derrotas': 4, 'nacionalidade': 'Argentina', 'saída': '25/09/2025'},
                '40002': {'nome': 'Vitor Pereira', 'estado': 'antigo', 'entrada': '01/01/2025', 'jogos': 18, 'vitórias': 10, 'empates': 2, 'derrotas': 6, 'nacionalidade': 'Portuguesa', 'saída': '05/04/2025'},
                '40003': {'nome': 'Tite', 'estado': 'atual', 'entrada': '05/10/2025', 'jogos': 4, 'vitórias': 2, 'empates': 1, 'derrotas': 1, 'nacionalidade': 'Brasileira', 'saída': '-'}
            }
            escrevertreinadores(treinadores2, f)

        elif ficheiro == 'jogosFlamengo.txt':
            jogos2 = {
                1: {'data': '14/05/2026', 'hora': '21:30', 'adversário': 'Vasco', 'local': 'Maracanã', 'golos': [1, 0], 'cartões A': ['Gerson'], 'cartões V': [], 'marcadores': ['Pedro']},
                2: {'data': '21/05/2026', 'hora': '16:00', 'adversário': 'Fluminense', 'local': 'Maracanã', 'golos': [2, 2], 'cartões A': ['Pulgar', 'Leo'], 'cartões V': ['Ayrton'], 'marcadores': ['Gabriel', 'Arrascaeta']},
                3: {'data': '28/5/2026', 'hora': '20:00', 'adversário': 'Botafogo', 'local': 'Engenhão', 'golos': [0, 1], 'cartões A': ['Everton'], 'cartões V': [], 'marcadores': []},
                4: {'data': '5/6/2026', 'hora': '18:30', 'adversário': 'Cruzeiro', 'local': 'Maracanã', 'golos': [3, 0], 'cartões A': ['Gabriel'], 'cartões V': [], 'marcadores': ['Pedro', 'Pedro', 'Bruno']}
            }
            escreverjogos(jogos2, f)

        elif ficheiro == 'estatisticasFlamengo.txt':
            estatisticas2 = {
                'pontos': 7,
                'vitórias': 2,
                'empates': 1,
                'derrotas': 1,
                'golos marcados': 6,
                'golos sofridos': 3,
                'saldo de golos': 3
            }
            escreverestatisticas(estatisticas2, f)

        elif ficheiro == 'jogadoresVasco.txt':
            jogadores3 = {
                '30001': {'nome': 'Suárez', 'camisa': '9', 'posição': 'A', 'idade': '37', 'golos': 4, 'cartões': [1, 0], 'estado': 'A', 'jogos': 4},
                '30002': {'nome': 'Villasanti', 'camisa': '20', 'posição': 'M', 'idade': '27', 'golos': 0, 'cartões': [2, 0], 'estado': 'A', 'jogos': 4},
                '30003': {'nome': 'Kannemann', 'camisa': '4', 'posição': 'D', 'idade': '33', 'golos': 0, 'cartões': [1, 1], 'estado': 'I', 'jogos': 3},
                '30004': {'nome': 'Cristaldo', 'camisa': '10', 'posição': 'M', 'idade': '27', 'golos': 1, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '30005': {'nome': 'Marchesín', 'camisa': '1', 'posição': 'G', 'idade': '36', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '30006': {'nome': 'Geromel', 'camisa': '3', 'posição': 'D', 'idade': '38', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 2},
                '30007': {'nome': 'Reinaldo', 'camisa': '6', 'posição': 'D', 'idade': '34', 'golos': 1, 'cartões': [1, 0], 'estado': 'A', 'jogos': 4},
                '30008': {'nome': 'Pepê', 'camisa': '23', 'posição': 'M', 'idade': '26', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4},
                '30009': {'nome': 'Pavón', 'camisa': '21', 'posição': 'A', 'idade': '28', 'golos': 0, 'cartões': [0, 0], 'estado': 'I', 'jogos': 1},
                '30010': {'nome': 'Diego', 'camisa': '19', 'posição': 'A', 'idade': '35', 'golos': 0, 'cartões': [0, 0], 'estado': 'A', 'jogos': 4}
            }
            escreverjogadores(jogadores3, f)

        elif ficheiro == 'treinadoresVasco.txt':
            treinadores3 = {
                '50001': {'nome': 'Tiago Nunes', 'estado': 'antigo', 'entrada': '01/02/2025', 'jogos': 10, 'vitórias': 3, 'empates': 3, 'derrotas': 4, 'nacionalidade': 'Brasileira', 'saída': '15/05/2025'},
                '50002': {'nome': 'Roger Machado', 'estado': 'antigo', 'entrada': '20/05/2025', 'jogos': 25, 'vitórias': 12, 'empates': 8, 'derrotas': 5, 'nacionalidade': 'Brasileira', 'saída': '01/12/2025'},
                '50003': {'nome': 'Renato Gaúcho', 'estado': 'atual', 'entrada': '10/01/2026', 'jogos': 4, 'vitórias': 3, 'empates': 0, 'derrotas': 1, 'nacionalidade': 'Brasileira', 'saída': '-'}
            }
            escrevertreinadores(treinadores3, f)

        elif ficheiro == 'jogosVasco.txt':
            jogos3 = {
                1: {'data': '20/04/2026', 'hora': '18:30', 'adversário': 'Internacional', 'local': 'Arena', 'golos': [2, 1], 'cartões A': ['Kannemann', 'Villasanti'], 'cartões V': [], 'marcadores': ['Suárez', 'Cristaldo']},
                2: {'data': '27/04/2026', 'hora': '21:00', 'adversário': 'Bahia', 'local': 'Fonte Nova', 'golos': [0, 1], 'cartões A': ['Reinaldo'], 'cartões V': ['Kannemann'], 'marcadores': []},
                3: {'data': '4/5/2026', 'hora': '16:00', 'adversário': 'Cuiabá', 'local': 'Arena', 'golos': [1, 0], 'cartões A': ['Villasanti'], 'cartões V': [], 'marcadores': ['Suárez']},
                4: {'data': '11/05/2026', 'hora': '19:00', 'adversário': 'Coritiba', 'local': 'Couto Pereira', 'golos': [3, 1], 'cartões A': ['Suárez'], 'cartões V': [], 'marcadores': ['Suárez', 'Suárez', 'Reinaldo']}
            }
            escreverjogos(jogos3, f)

        elif ficheiro == 'estatisticasVasco.txt':
            estatisticas3 = {
                'pontos': 9,
                'vitórias': 3,
                'empates': 0,
                'derrotas': 1,
                'golos marcados': 6,
                'golos sofridos': 3,
                'saldo de golos': 3
            }
            escreverestatisticas(estatisticas3, f)

    with open(ficheiro, 'r', encoding='utf-8')as f:
        conteudo = f.read()

    return conteudo


# Essa função transforma o conteúdo dos ficheiros em dicionários e retorna uma lista de dicionários.
def transformarjogadores():

    def transformar(conteudo):
        lista_jogadores = conteudo.split('\n')
        dicionario = {}
        for linha in lista_jogadores:
            linha = linha.strip()
            idjogador, nome, camisa, posicao, idade, golos, cartoes, estado, jogos = linha.split(
                '|')
            idade = int(idade)
            golos = int(golos)
            cA, cV = cartoes.split(',')
            cA = int(cA)
            cV = int(cV)
            jogos = int(jogos)
            dicionario[idjogador] = {'nome': nome, 'camisa': camisa, 'posição': posicao,
                                     'idade': idade, 'golos': golos, 'cartões': [cA, cV], 'estado': estado, 'jogos': jogos}

        return dicionario

    existe, conteudo_SaoPaulo = ler_capiturarerros('jogadoresSaoPaulo.txt')
    if existe == False:
        conteudo_SaoPaulo = criarficheiros('jogadoresSaoPaulo.txt')
    dicionario_SaoPaulo = transformar(conteudo_SaoPaulo)

    existe, conteudo_Flamengo = ler_capiturarerros('jogadoresFlamengo.txt')
    if existe == False:
        conteudo_Flamengo = criarficheiros('jogadoresFlamengo.txt')
    dicionario_Flamengo = transformar(conteudo_Flamengo)

    existe, conteudo_Vasco = ler_capiturarerros('jogadoresVasco.txt')
    if existe == False:
        conteudo_Vasco = criarficheiros('jogadoresVasco.txt')
    dicionario_Vasco = transformar(conteudo_Vasco)

    return [dicionario_SaoPaulo, dicionario_Flamengo, dicionario_Vasco]


def transformartreinadores():

    def transformar(conteudo):
        lista_treinadores = conteudo.split('\n')
        dicionario = {}
        for linha in lista_treinadores:
            idtreinador, nome, estado, entrada, jogos, vitorias, empates, derrotas, nacionalidade, saida = linha.strip().split('|')
            jogos = int(jogos)
            vitorias = int(vitorias)
            empates = int(empates)
            derrotas = int(derrotas)
            dicionario[idtreinador] = {'nome': nome, 'estado': estado, 'entrada': entrada, 'jogos': jogos,
                                       'vitórias': vitorias, 'empates': empates, 'derrotas': derrotas, 'nacionalidade': nacionalidade, 'saída': saida}

        return dicionario

    existe, conteudo_SaoPaulo = ler_capiturarerros('treinadoresSaoPaulo.txt')
    if existe == False:
        conteudo_SaoPaulo = criarficheiros('treinadoresSaoPaulo.txt')
    dicionario_SaoPaulo = transformar(conteudo_SaoPaulo)

    existe, conteudo_Flamengo = ler_capiturarerros('treinadoresFlamengo.txt')
    if existe == False:
        conteudo_Flamengo = criarficheiros('treinadoresFlamengo.txt')
    dicionario_Flamengo = transformar(conteudo_Flamengo)

    existe, conteudo_Vasco = ler_capiturarerros('treinadoresVasco.txt')
    if existe == False:
        conteudo_Vasco = criarficheiros('treinadoresVasco.txt')
    dicionario_Vasco = transformar(conteudo_Vasco)

    return [dicionario_SaoPaulo, dicionario_Flamengo, dicionario_Vasco]


def transformarjogos():

    def transformar(conteudo):
        lista_jogos = conteudo.split('\n')
        dicionario = {}
        for linha in lista_jogos:
            rodada, data, hora, adversario, local, golos, cartoesA, cartoesV, marcadores = linha.strip().split('|')
            gM, gS = golos.split(',')
            gM = int(gM)
            gS = int(gS)
            dicionario[int(rodada)] = {'data': data, 'hora': hora, 'adversário': adversario, 'local': local, 'golos': [
                gM, gS], 'cartões A': cartoesA.split(','), 'cartões V': cartoesV.split(','), 'marcadores': marcadores.split(',')}

        return dicionario

    existe, conteudo_SaoPaulo = ler_capiturarerros('jogosSaoPaulo.txt')
    if existe == False:
        conteudo_SaoPaulo = criarficheiros('jogosSaoPaulo.txt')
    dicionario_SaoPaulo = transformar(conteudo_SaoPaulo)

    existe, conteudo_Flamengo = ler_capiturarerros('jogosFlamengo.txt')
    if existe == False:
        conteudo_Flamengo = criarficheiros('jogosFlamengo.txt')
    dicionario_Flamengo = transformar(conteudo_Flamengo)

    existe, conteudo_Vasco = ler_capiturarerros('jogosVasco.txt')
    if existe == False:
        conteudo_Vasco = criarficheiros('jogosVasco.txt')
    dicionario_Vasco = transformar(conteudo_Vasco)

    return [dicionario_SaoPaulo, dicionario_Flamengo, dicionario_Vasco]


def tranformarestatisticas():
    def transformar(conteudo):
        lista_estatisticas = conteudo.split('\n')
        dicionario = {}
        for linha in lista_estatisticas:
            pontos, vitorias, empates, derrotas, golosM, golosS, saldo_golos = linha.strip().split('|')
            pontos = int(pontos)
            vitorias = int(vitorias)
            empates = int(empates)
            derrotas = int(derrotas)
            golosM = int(golosM)
            golosS = int(golosS)
            saldo_golos = int(saldo_golos)
            dicionario = {'pontos': pontos, 'vitórias': vitorias, 'empates': empates, 'derrotas': derrotas,
                          'golos marcados': golosM, 'golos sofridos': golosS, 'saldo de golos': saldo_golos}

        return dicionario

    existe, conteudo_SaoPaulo = ler_capiturarerros('estatisticasSaoPaulo.txt')
    if existe == False:
        conteudo_SaoPaulo = criarficheiros('estatisticasSaoPaulo.txt')
    dicionario_SaoPaulo = transformar(conteudo_SaoPaulo)

    existe, conteudo_Flamengo = ler_capiturarerros('estatisticasFlamengo.txt')
    if existe == False:
        conteudo_Flamengo = criarficheiros('estatisticasFlamengo.txt')
    dicionario_Flamengo = transformar(conteudo_Flamengo)

    existe, conteudo_Vasco = ler_capiturarerros('estatisticasVasco.txt')
    if existe == False:
        conteudo_Vasco = criarficheiros('estatisticasVasco.txt')
    dicionario_Vasco = transformar(conteudo_Vasco)

    return [dicionario_SaoPaulo, dicionario_Flamengo, dicionario_Vasco]


# Transformar os conteúdos dos ficheiros em dicionário.
jogadores = transformarjogadores()

treinadores = transformartreinadores()
jogos = transformarjogos()
estatisticas = tranformarestatisticas()

Gestao_campeonato = {
    'Jogadores': jogadores,

    'Histórico Treinadores': treinadores,

    'Jogos CB': jogos,

    'Estatísticas CB': estatisticas
}


# >>MANIPULANDO OS DICIONÁRIOS<<


# Esta função retorna uma lista de IDs cujo um determinado valor é semelhante entre eles
def verificar(clube_posicao, dicionario, chave, valor):
    ids = []
    for id in Gestao_campeonato[dicionario][clube_posicao]:
        if valor == Gestao_campeonato[dicionario][clube_posicao][id][chave]:
            ids.append(id)
    return ids


def escolher_jogador(lista, clube_posicao):
    opcoes = []
    for id in lista:
        print(
            f"{Gestao_campeonato['Jogadores'][clube_posicao][id]['nome']} - camisa: {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']}")
        opcoes.append(Gestao_campeonato['Jogadores']
                      [clube_posicao][id]['camisa'])

    n = input("\nEscolhe o jogador (nº da camisa): ").strip()

    while n not in opcoes:
        n = input(
            "\nO número introduzido não corresponde a nenhuma das opções apresentadas.\nTente novamente: ").strip()

    for id in Gestao_campeonato['Jogadores'][clube_posicao]:
        if Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa'] == n:
            return id


def mostrar_jogadores(id, clube_posicao):

    for c, v in Gestao_campeonato['Jogadores'][clube_posicao][id].items():
        if c == 'nome':
            pass
        elif c == 'cartões':
            print(f"Cartões amarelos: {v[0]} - Cartões vermelhos: {v[1]}")
        else:
            print(f"{c}: {v}")


def verificar_camisa(n, clube_posicao):
    for id in Gestao_campeonato['Jogadores'][clube_posicao]:
        if Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa'] == n:
            return id
    return None


def gerarID(dicionario, clube_posicao):
    id = str(random.randint(100, 100000000))
    while Gestao_campeonato[dicionario][clube_posicao].get(id) != None:
        id = str(random.randint(100, 100000000))
    return id


def validar_SN(pergunta):
    resposta = input(pergunta).strip().upper()
    while resposta not in 'SN':
        resposta = input(
            f"<< RESPOSTA INVÁLIDA. >>\n Tente novamente: ").strip().upper()
    return resposta


def mostrar_treinador(id, clube_posicao):
    for c, v in Gestao_campeonato['Histórico Treinadores'][clube_posicao][id].items():

        print(f"{c}: {v}")


def validardata(ultima_data_inserida, tipo):
    def pedirdata():
        erro = True
        while erro:
            try:
                dd = int(input('Dia: '))
                mm = int(input('Mês: '))
                aaaa = int(input('Ano: '))
                erro = False
            except ValueError:
                print("\nDADO INVÁLIDO!: Apenas algarismos são aceitos.")
        return dd, mm, aaaa

    dd, mm, aaaa = pedirdata()
    udd, umm, uaaaa = ultima_data_inserida.split('/')
    while dd < 1 or dd > 31 or dd > 29 and mm == 2 or mm < 1 or mm > 12 or mm < int(umm) and aaaa == int(uaaaa) or mm == int(umm) and dd < int(udd) or aaaa < int(uaaaa):

        if tipo == 'treinadores':
            print('\nDATA INVÁLIDA!! Verifique se:\n - Os dados foram corretamente introduzidos.\n - A data introduzida é maior que a data de saída do último treinador.\n')
        elif tipo == 'jogos':
            print('\nDATA INVÁLIDA!! Verifique se:\n - Os dados foram corretamente introduzidos.\n - A data introduzida é maior que a data do último jogo.\n')

        dd, mm, aaaa = pedirdata()

    data_validada = f"{dd}/{mm}/{aaaa}"
    return data_validada


def demitir_treinador(clube_posicao):
    for id in reversed(Gestao_campeonato['Histórico Treinadores'][clube_posicao]):
        if Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['estado'] == 'atual':
            Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['estado'] = 'antigo'
            Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['saída'] = validardata(
                Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['entrada'], 'treinadores')
            return f"\n{Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['nome']}, até então atual treinador, foi demitido.", Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['saída']


def mostrar_jogos(rodada, clube_posicao):
    for c, v in Gestao_campeonato['Jogos CB'][clube_posicao][rodada].items():
        if c == 'cartões A' or c == 'cartões V' or c == 'marcadores':
            print(f" {c}: ")
            for nome in v:
                print('  -', nome)
        elif c == 'golos':
            print(f" Resultado: {v[0]} - {v[1]}")
        else:
            print(f" {c}: {v}")


def nomes_cAV():
    nome = input('- Nome: ').strip().title()
    ids = []
    while nome != '':
        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)
        while len(nomes_iguais) == 0:
            nome = input(
                "\n⚠️   Nome não encontrado! Tente novamente: ").strip().title()
            nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)

        if len(nomes_iguais) > 1:
            print("⚠️   Mais de um jogador encontrado:")
            id = escolher_jogador(nomes_iguais, clube_posicao)
            ids.append(id)
        elif len(nomes_iguais) == 1:
            ids.append(nomes_iguais[0])
        nome = input('- Nome: ').strip().title()

    return ids


def nomes_marcadores(ngolos):
    ids = []
    for n in range(ngolos):
        nome = input('- Nome: ').strip().title()
        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)
        while len(nomes_iguais) == 0:
            nome = input(
                "\n⚠️   Nome não encontrado! Tente novamente: ").strip().title()
            nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)

        if len(nomes_iguais) > 1:
            print("⚠️   Mais de um jogador encontrado:")
            id = escolher_jogador(nomes_iguais, clube_posicao)
            ids.append(id)
        elif len(nomes_iguais) == 1:
            ids.append(nomes_iguais[0])
    return ids


def AtualizarJogadores_cartoes_marcadores(ids, tipo, clube_posicao):
    for id in Gestao_campeonato['Jogadores'][clube_posicao]:
        if id in ids:
            if tipo == 'A':
                Gestao_campeonato['Jogadores'][clube_posicao][id]['cartões'][0] += 1
            elif tipo == 'V':
                Gestao_campeonato['Jogadores'][clube_posicao][id]['cartões'][1] += 1
            elif tipo == 'M':
                Gestao_campeonato['Jogadores'][clube_posicao][id]['golos'] += 1


def procurarJogador(ids, clube_posicao):
    nomes = []
    for id in ids:
        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome',
                                 Gestao_campeonato['Jogadores'][clube_posicao][id]['nome'])
        if len(nomes_iguais) > 1:
            nomes.append(
                f"{Gestao_campeonato['Jogadores'][clube_posicao][id]['nome']} - camisa {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']}")
        elif len(nomes_iguais) == 1:
            nomes.append(
                f"{Gestao_campeonato['Jogadores'][clube_posicao][id]['nome']}")
    return nomes


def ConsultarJogadores(submenu, clube_posicao):

    if submenu == "1":
        lista = []
        for id in Gestao_campeonato['Jogadores'][clube_posicao]:
            if Gestao_campeonato['Jogadores'][clube_posicao][id]["estado"] == "A":
                lista.append(
                    f"{Gestao_campeonato['Jogadores'][clube_posicao][id]["nome"]} - Nº camisa: {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']}")

        lista.sort()
        for jogadorA in lista:
            print(jogadorA)

    if submenu == "2":
        set_golos = set()
        for id in Gestao_campeonato['Jogadores'][clube_posicao]:
            n_golos = Gestao_campeonato['Jogadores'][clube_posicao][id]['golos']
            if n_golos != 0:
                set_golos.add(n_golos)

        if len(set_golos) == 0:
            print("\nSEM GOLOS REGISTRADOS ATÉ AGORA.")
        else:
            n_max = max(set_golos)
            ids_jogadores = verificar(
                clube_posicao, "Jogadores", 'golos', n_max)
            for id in ids_jogadores:
                print(
                    f"Camisa {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']}: {Gestao_campeonato['Jogadores'][clube_posicao][id]['nome']} - {n_golos} golos.")

    elif submenu == "3":
        nome = input("\nNome do jogador: ").strip().title()

        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)

        if len(nomes_iguais) == 0:
            print("\n<< NÃO TEMOS JOGADORES COM ESSE NOME. >>")
        elif len(nomes_iguais) >= 2:
            print("\nMAIS DE UM JOGADOR ENCONTRADO:")
            id = escolher_jogador(nomes_iguais, clube_posicao)
            mostrar_jogadores(id, clube_posicao)
        else:
            mostrar_jogadores(nomes_iguais[0], clube_posicao)

    else:
        print("> COMANDO INVÁLIDO. <")


def EditarJogadores(submenu, clube_posicao):
    def validarcamisa(camisa):
        retorno = verificar_camisa(camisa, clube_posicao)

        while retorno != None:
            camisa = input(
                f"{Gestao_campeonato['Jogadores'][clube_posicao][retorno]['nome']} veste essa camisa.\nInsira outro número: ").strip()
            retorno = verificar_camisa(camisa, clube_posicao)

        return camisa

    def adicionar_jogador(nome, clube_posicao):

        id = gerarID('Jogadores', clube_posicao)

        camisa = input("\nNº da camisa:").strip()
        camisa_valida = validarcamisa(camisa)

        posicao = input(
            "Posição (G-Goleiro D-Defesa A-Avançado M-Médio): ").strip().upper()
        while posicao not in "GDAM":
            posicao = input(
                ">> DADO INVÁLIDO <<\n(G-Goleiro D-Defesa A-Avançado M-Médio): ").strip().upper()

        estado = input("Estado (A-ativo ou I-inativo): ").strip().upper()
        while estado not in "AI":
            estado = input(
                ">> DADO INVÁLIDO <<\nEstado (A-ativo ou I-inativo): ").strip().upper()

        idade = int(input("Idade (>16 e <35): "))
        while idade < 16 or idade > 35:
            idade = int(input(">> IDADE INVÁLIDA <<\nIdade (>16 e <35): "))

        Gestao_campeonato['Jogadores'][clube_posicao][id] = {
            "nome": nome,
            "camisa": camisa_valida,
            "posição": posicao,
            "idade": idade,
            "golos": 0,
            "cartões": [0, 0],
            "estado": estado,
            "jogos": 0}

        print('\n\nJOGADOR ADICIONADO.')
        return id

    if submenu == "1":
        nome = input("\nNome do novo jogador: ").strip().title()

        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)
        mostrar = True
        if len(nomes_iguais) == 0:
            novo_id = adicionar_jogador(nome, clube_posicao)
        else:
            print("TEMOS JOGADOR(ES) COM ESSE NOME:")
            for id in nomes_iguais:
                print(
                    f"Nome: {Gestao_campeonato['Jogadores'][clube_posicao][id]['nome']} - camisa: {Gestao_campeonato["Jogadores"][clube_posicao][id]['camisa']}")

            r = validar_SN('\nDeseja continuar (S/N)? ')
            if r == 'S':
                novo_id = adicionar_jogador(nome, clube_posicao)

            else:
                mostrar = False
                print("Operação Interrompida.")

        if mostrar:
            if validar_SN("\nDeseja ver os dados atualizados desta secção? (S/N): ") == 'S':
                mostrar_jogadores(novo_id, clube_posicao)

    elif submenu == "2":
        nome = input("\nNome do jogador: ").strip().title()

        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)

        if len(nomes_iguais) == 0:
            print("\n< NOME NÃO ENCONTRADO. >")
        else:
            if len(nomes_iguais) >= 2:
                print(f"\nMais de um jogador encontrado:")
                id = escolher_jogador(nomes_iguais, clube_posicao)

                print(
                    f"\nCamisa: {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']} - {nome} foi removido.")
                del Gestao_campeonato['Jogadores'][clube_posicao][id]
            else:
                print(
                    f"\nCamisa: {Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]]['camisa']} - {nome} foi removido.")
                del Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]]

    elif submenu == "3":
        nome = input("\nNome do jogador: ").strip().title()
        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)
        if len(nomes_iguais) == 0:
            print("\n< NOME NÃO ENCONTRADO. >")
        else:
            n = 0
            if len(nomes_iguais) >= 2:
                print(f"\nMais de um jogador encontrado:")
                id = escolher_jogador(nomes_iguais, clube_posicao)

                camisa = input("Nº novo: ")
                camisa_valida = validarcamisa(camisa)

                print(
                    f"\n{nome} - camisa alterada de {Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa']} para {camisa_valida}.")
                Gestao_campeonato['Jogadores'][clube_posicao][id]['camisa'] = camisa_valida
            else:
                camisa = input("Nº novo: ")
                camisa_valida = validarcamisa(camisa)

                print(
                    f"\n{nome} - camisa alterada de {Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]]['camisa']} para {camisa_valida}.")
                Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]
                                                              ]['camisa'] = camisa_valida

    elif submenu == "4":
        nome = input("\nNome do jogador: ").strip().title()
        nomes_iguais = verificar(clube_posicao, 'Jogadores', 'nome', nome)

        if len(nomes_iguais) == 0:
            print("\n< NOME NÃO ENCONTRADO. >")

        elif len(nomes_iguais) >= 2:
            print(f"\nMais de um jogador encontrado:")
            id = escolher_jogador(nomes_iguais, clube_posicao)

            if Gestao_campeonato['Jogadores'][clube_posicao][id]['estado'] == "A":
                Gestao_campeonato['Jogadores'][clube_posicao][id]['estado'] = "I"
                print(f"{nome} passou de A para I.")
            else:
                Gestao_campeonato['Jogadores'][clube_posicao][id]['estado'] = "A"
                print(f"{nome} passou de I para A.")
        else:
            if Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]]['estado'] == "A":
                Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]
                                                              ]['estado'] = "I"
                print(f"{nome} passou de A para I.")
            else:
                Gestao_campeonato['Jogadores'][clube_posicao][nomes_iguais[0]
                                                              ]['estado'] = "A"
                print(f"{nome} passou de I para A.")

    else:
        print("> COMANDO INVÁLIDO. <")


def ConsultarTreinadores(submenu, clube_posicao):
    if submenu == '1':
        n_atuais = verificar(
            clube_posicao, 'Histórico Treinadores', 'estado', 'atual')
        if len(n_atuais) == 1:
            mostrar_treinador(n_atuais[0], clube_posicao)
        else:
            print("\n< NENHUM TREINADOR FOI CONTRATADO AINDA. >")
    elif submenu == "2":
        for id in Gestao_campeonato['Histórico Treinadores'][clube_posicao]:
            Edia, Emes, Eano = Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['entrada'].split(
                "/")
            if Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['estado'] != 'atual':
                Sdia, Smes, Sano = Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['saída'].split(
                    "/")
            if Eano == "2026" or Sano == "2026":
                for chave, valor in Gestao_campeonato['Histórico Treinadores'][clube_posicao][id].items():
                    if chave == 'nome':
                        print(f"\n> Nome: {valor} <")
                    if chave == 'saída' and valor == '-':
                        continue
                    print(f"{chave}: {valor}")


def EditarTreinadores(submenu, clube_posicao):
    if submenu == "1":
        if len(verificar(clube_posicao, 'Histórico Treinadores', 'estado', 'atual')) == 0:
            print("\n<< NÃO HÁ TREINADORES ATUAIS PARA DEMITIR. >>")
        else:
            print(demitir_treinador(clube_posicao)[0])
    elif submenu == '2':
        mostrar = True
        treinador_atual = None
        achou_atual = False
        for id in reversed(Gestao_campeonato['Histórico Treinadores'][clube_posicao]):
            if Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['estado'] == 'atual':
                achou_atual = True
                treinador_atual = Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['nome']

                print(
                    f"\nOPERAÇÃO IMPOSSÍVEL: {treinador_atual} ainda é o treinador.")

                r = validar_SN("\nDeseja demiti-lo para continuar (S/N)?\n: ")
                if r == "N":
                    mostrar = False
                    print(
                        f">> {Gestao_campeonato['Histórico Treinadores'][clube_posicao][id]['nome']} continua sendo o treinador do clube. <<")
                else:
                    pass
                break
        if mostrar == True:
            mensagem, dataSaida = demitir_treinador(clube_posicao)
            print(mensagem)
            nome = input("\nNome do novo treinador: ").strip().title()
            if nome == treinador_atual or nome != treinador_atual:
                id = gerarID('Histórico Treinadores', clube_posicao)
                if achou_atual == False:
                    for treinador in Gestao_campeonato['Histórico Treinadores'][clube_posicao]:
                        if Gestao_campeonato['Histórico Treinadores'][clube_posicao][treinador]['estado'] == 'antigo':
                            data = validardata(
                                Gestao_campeonato['Histórico Treinadores'][clube_posicao][treinador]['saída'], 'treinadores')
                else:
                    data = validardata(dataSaida, 'treinadores')

                Gestao_campeonato['Histórico Treinadores'][clube_posicao][id] = {
                    'nome': nome,
                    'estado': 'atual',
                    'entrada': data,
                    'jogos': 0,
                    'vitórias': 0,
                    'empates': 0,
                    'derrotas': 0,
                    'nacionalidade': input("Nacionalidade: ").strip().title(), }
                r = validar_SN(
                    "\nDeseja ver os dados atualizados desta secção? (S/N): ")
                if r == 'S':
                    mostrar_treinador(id, clube_posicao)


def ConsultarJogos(submenu, clube_posicao):
    if submenu == "1":
        rodada = int(input("\nNº da Rodada: "))
        while rodada < 1 or rodada > 38:
            rodada = int(input("\n<< Nº INVÁLIDO. >>\nTente novamente: "))
        if Gestao_campeonato['Jogos CB'][clube_posicao].get(rodada) == None:
            print(
                "\nNÃO EXISTEM DADOS SOBRE ESSA RODADA - Ela ainda não foi desputada pelo clube.")
        else:
            mostrar_jogos(rodada, clube_posicao)

    elif submenu == '2':
        rodada = int(input("\nNº da Rodada: "))
        while rodada < 1 or rodada > 38:
            rodada = int(input("\nDADO INVÁLIDO.\nTente novamente: "))
        if Gestao_campeonato['Jogos CB'][clube_posicao].get(rodada) == None:
            print("\n<< AINDA NÃO EXISTEM DADOS SOBRE O JOGO DESTA RODADA. >>")
        else:
            print(
                f"\nNº golos da partida: {Gestao_campeonato['Jogos CB'][rodada]['golos'][0]}")
            for nome in Gestao_campeonato['Jogos CB'][rodada]['marcadores']:
                print(f"- {nome}")
            if Gestao_campeonato['Jogos CB'][rodada]['marcadores'][0] == '':
                print("\n< NÃO HOUVERAM MARCADORES NESTA PARTIDA. >")

    elif submenu == '3':
        rodadas = 38-len(Gestao_campeonato['Jogos CB'])
        if rodadas == 0:
            print("\nO CAMPEONATO ACABOU.")
        else:
            print(f"\nFaltam {rodadas} rodadas.")
    else:
        print(f"\n> COMANDO INVÁLIDO. <")


def EditarJogos(submenu, clube_posicao):
    if submenu == '1':
        rodada = len(Gestao_campeonato['Jogos CB'])+1
        print(f"\n{rodada}º RODADA - Insira os dados do jogo: ")

        data_validada = validardata(
            Gestao_campeonato['Jogos CB'][clube_posicao][rodada-1]['data'], 'jogos')

        erro = True
        while erro:
            try:
                gM, gS = input(
                    "\nResultado (golos clube-golos adversário): ").strip().split('-')
                golos = (int(gM), int(gS))
                erro = False
            except ValueError:
                print("\nDADOS INVÁLIDOS! Certifique-se de que:\n - O formato índicado foi respeitado (golos clube-golos adversário).\n - Apenas algarismos foram introduzidos.")

        print("\n> CARTÕES AMARELOS - Nome(s) do(s) jogadores (ENTER para parar):")
        cartoesA = nomes_cAV()
        AtualizarJogadores_cartoes_marcadores(cartoesA, 'A', clube_posicao)
        cAnomes = procurarJogador(cartoesA, clube_posicao)
        print("\n> CARTÕES VERMELHOS - Nome(s) do(s) jogadores (ENTER para parar):")
        cartoesV = nomes_cAV()
        AtualizarJogadores_cartoes_marcadores(cartoesA, 'V', clube_posicao)
        cVnomes = procurarJogador(cartoesV, clube_posicao)

        print("\n> MARCADORES: ")
        gM = int(gM)
        gS = int(gS)
        marcadores = nomes_marcadores(gM)
        AtualizarJogadores_cartoes_marcadores(marcadores, 'M', clube_posicao)
        marcadoresnomes = procurarJogador(marcadores, clube_posicao)

        erro = True
        while erro:
            try:
                hh, mm = input("\nHorário do jogo (HH:MM):").strip().split(':')
                hh = int(hh)
                mm = int(mm)
                while hh < 16 or hh > 23 or mm < 0 or mm >= 60:
                    hh, mm = input(
                        'HH e/ou MM inválidos! Tente novamente (HH:MM): ').strip().split(':')
                    hh = int(hh)
                    mm = int(mm)
                hora = f"{hh}:{mm}"
                erro = False
            except ValueError:
                print("DADO INVÁLIDO! Certifique-se de que:\n - A hora foi inserida no formato (HH:MM).\n - Apenas algarismos foram introduzidos.")

        Gestao_campeonato['Jogos CB'][clube_posicao][rodada] = {
            'data': data_validada,
            'hora': hora,
            'adversário': input("Nome do clube adversário: ").capitalize(),
            'local': input("Local: ").capitalize(),
            'golos': golos,
            'cartões A': cAnomes,
            'cartões V': cVnomes,
            'marcadores': marcadoresnomes
        }
        for id in Gestao_campeonato['Jogadores'][clube_posicao]:
            if Gestao_campeonato['Jogadores'][clube_posicao][id]["estado"] == "A":
                Gestao_campeonato['Jogadores'][clube_posicao][id]['jogos'] += 1

        if golos[0] > golos[1]:
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['pontos'] += 3
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['vitórias'] += 1
        elif golos[0] == golos[1]:
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['pontos'] += 1
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['empates'] += 1
        else:
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['derrotas'] += 1
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['golos marcados'] += golos[0]
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['golos sofridos'] += golos[1]
            Gestao_campeonato['Estatísticas CB'][clube_posicao]['saldo de golos'] = Gestao_campeonato['Estatísticas CB'][
                clube_posicao]['golos marcados'] - Gestao_campeonato['Estatísticas CB'][clube_posicao]['golos sofridos']

        if validar_SN("\nDeseja ver os dados atualizados desta secção? (S/N): ") == 'S':
            print(f"| RODADA: {rodada} |")
            mostrar_jogos(rodada, clube_posicao)
            mostrarestatisticas(clube_posicao)

    else:
        pass


def mostrarestatisticas(clube_posicao):
    print("| Estatísticas do clube: |")
    for c, v in Gestao_campeonato['Estatísticas CB'][clube_posicao].items():
        print(f" {c}: {v}")


def validar_int(pergunta):
    erro=True
    while erro:
        try:
            valor=int(input(pergunta))
            erro=False
        except ValueError:
            print(f'❗ DADO INVÁLIDO ❗')
    return valor

def validar_float(pergunta):
    erro=True
    while erro:
        try:
            valor=float(input(pergunta))
            erro=False
        except ValueError:
            print(f'❗ DADO INVÁLIDO ❗\n tente novamente: ')
    return valor

def calcularaproveitamentos():
    aproveitamentos=[]
    ids=[]
    for id_treinador in Gestao_campeonato['Histórico Treinadores'][clube_posicao]:
        try:
            aproveitamento=(Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['vitórias']*3)+(Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['empates']*1)
            n_max_pontos=Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['jogos']*3
            aproveitamento=aproveitamento/n_max_pontos*100
            aproveitamentos.append(round(aproveitamento,1))
            ids.append(id_treinador)
        except ZeroDivisionError:
            aproveitamentos.append(0)
    
    return aproveitamentos,ids

# PRGRAMA PRINCIPAL.
opcao = input(
    "1- Consultar informações\n2- Editar informações\n3- Pesquisas avançadas\n0- Sair\n: ").strip().upper()
while opcao not in '1230':
    opcao = input("!DADO INVÁLIDO!  Tente novamente: ").strip().upper()

clube = input("\n\nESCOLHA O CLUBE:\n1-São Paulo\n2-Flamengo\n3-Vasco\n: ")

while clube not in "123":
    clube = input("\n\nCOMANDO INVÁLIDO\nTente novamente: ")

clube_posicao = int(clube)-1


if opcao == '1':
    menuC = input("\n\nConsultar informações sobre:\n 1- Jogadores\n 2- Treinadores\n 3- Jogos (CB 2026)\n 4- Estatísticas (CB 2026)\n 0- Sair\n : ").strip()
    while menuC not in '12340':
        menuC = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()

    if menuC == '1':
        submenu = input(
            "\n\n1- Lista de jogadores ativos\n2- Melhor(es) marcador(es)\n3- Dados de um jogador\n: ").strip()
        while submenu not in '123':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        ConsultarJogadores(submenu, clube_posicao)

    elif menuC == '2':
        submenu = input(
            "\n1- Dados do treinador atual\n2- Histórico de treinadores (2026)\n: ").strip()
        while submenu not in '12':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        ConsultarTreinadores(submenu, clube_posicao)

    elif menuC == '3':
        submenu = input(
            "\n1- Dados de um determinado jogo\n2- Marcadores de golos de um determinado jogo\n3- Quantas rodadas faltam para o fim do CB\n: ").strip()
        while submenu not in '123':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        ConsultarJogos(submenu, clube_posicao)

    elif menuC == '4':
        submenu = input("\n1- Ver as estatísticas de um determinado clube.\n0- Sair")
        while submenu not in '10':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        if submenu=='1':
            mostrarestatisticas(clube_posicao)
        else:
            pass
    elif menuC == '0':
        pass

elif opcao == '2':
    menuE = input(
        "\n\nEditar informações sobre:\n 1- Jogadores\n 2- Treinadores\n 3- Jogos (CB 2026)\n 0- Sair\n : ").strip()

    while menuE not in '1230':
        menuE = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()

    if menuE == '1':
        submenu = input(
            "\n1- Adicionar jogador\n2- Remover jogador\n3- Editar o nº da camisa\n4- Editar estado\n:").strip()
        while submenu not in '1234':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        EditarJogadores(submenu, clube_posicao)

    elif menuE == '2':
        submenu = input(
            "\n1- Demitir Treinador\n2- Contratar Treinador\n: ").strip()
        while submenu not in '12':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        EditarTreinadores(submenu, clube_posicao)

    elif menuE == '3':
        submenu = input(
            "\n1- Adicionar novo resultado de jogo\n0- Sair\n: ").strip()
        while submenu not in '10':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        EditarJogos(submenu, clube_posicao)

    elif menuE == '0':
        pass
    else:
        print("COMANDO INVÁLIDO.")

elif opcao=='3':
    menuP = input("\n\nPesquisas avançadas sobre:\n 1- Jogadores\n 2- Treinadores\n 3- Jogos (CB 2026)\n 0- Sair\n : ")
    while menuP not in '1230':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
    if menuP=='1':
        submenu=input("\n1- Jogadores com mais de X golos em posição específica\n2- Jogadores ativos com mais de X golos em menos de X jogos\n3- Jogadores mais eficientes: golos por jogo e poucos cartões.\n0- Sair\n: ").strip()
        while submenu not in '1230':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        if submenu=='1':
            
            quantidademin_golos=validar_int("Insira a quantidade mínima de golos desejada: ")

            posicao=input("Posição desejada (G/D/M/A): ").strip().upper()
            while posicao not in 'GDMA':
                posicao=input("❗ DADO INVÁLIDO ❗\n Posição desejada (G/D/M/A): ").strip().upper()

            lista1=[]
            for id_jogador in Gestao_campeonato['Jogadores'][clube_posicao]:
                if Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['posição']==posicao and  Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['golos'] < quantidademin_golos:
                    lista1.append(id_jogador)
                    print(f"> Camisa {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['camisa']}: {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['nome']}\n - Posição: {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['posição']}\n - Golos: {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['golos']}.")
            
            if len(lista1)==0:
                print(f"\n😞   Nenhum jogador na posição {posicao} se encontra com um valor de golos igual ou superior à {quantidademin_golos}.")

        elif submenu=='2':
            quantidademin_golos=validar_int('Insira a quantidade mínima de golos desejada: ')
            quantidademax_jogos=validar_int('Insira a quantidade maxima de jogos desejada: ')

            lista2=[]
            for id_jogador in Gestao_campeonato['Jogadores'][clube_posicao]:
                if Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['jogos']<=quantidademax_jogos and Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['golos'] >= quantidademin_golos:
                    lista2.append(id_jogador)
                    print(f"> Camisa {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['camisa']}: {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['nome']}\n - {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['golos']} golos em {Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['jogos']} jogos.")

            if len(lista2)==0:
                print(f"\n😞   Nenhum jogador que tenha jogado no máximo {quantidademax_jogos} jogos marcou um valor de golos igual ou superior à {quantidademin_golos}")
        
        elif submenu=='3':
            print("\n  ⚠️  OBS: Estão a se considerados jogadores que jogaram no mínimo 1 jogo. ⚠️")
            eficiencia_golos_jogos=[]
            eficiencia_cartoes_jogos=[]
            ids_mais_de_1_jogo=[]
            for id_jogador in Gestao_campeonato['Jogadores'][clube_posicao]:
                if Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['jogos']!=0:
                    ids_mais_de_1_jogo.append(id_jogador)
                    eficiencia_golos_jogos.append(round(Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['golos']/Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['jogos'],2))
                    eficiencia_cartoes_jogos.append(round((Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['cartões'][0]+Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['cartões'][1])/Gestao_campeonato['Jogadores'][clube_posicao][id_jogador]['jogos'],2))
            
            if len(ids_mais_de_1_jogo) ==0:
                print("\n😞  Nenhum jogador jogou no mínimo 1 jogo.")
            else:
                eficiencias=[]
                ids=[]
                for i in range(len(eficiencia_golos_jogos)):
                    try:
                        eficiencias.append(eficiencia_golos_jogos[i]/eficiencia_cartoes_jogos[i])
                        ids.append(ids_mais_de_1_jogo[i])
                    except ZeroDivisionError:
                        continue
                n_max_eficiencia=max(eficiencias)
                for i in range(len(eficiencias)):
                    if eficiencias[i]==n_max_eficiencia:
                        print(f"> Camisa {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['camisa']} - {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['nome']} é o jogador mais eficiente do clube:\n - jogos: {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['jogos']}\n - golos: {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['golos']}\n - cartões amarelos: {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['cartões'][0]}\n - cartões vermelhos: {Gestao_campeonato['Jogadores'][clube_posicao][ids[i]]['cartões'][1]}\n")
        else:
            pass
    elif menuP=='2':
        submenu=input("\n1- Treinadores com mais de X vitórias e menos de X derrotas\n2- Treinador com maior aproveitamento geral\n3- Treinadores com aproveitamento acima de X%\n0- Sair\n: ").strip()
        while submenu not in '1230':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        if submenu=='1':
            vitorias_min=validar_int('Nº mínimo de vitórias: ')
            derrotas_max=validar_int('Nº máximo de derrotas: ')

            lista3=[]
            for id_treinador in Gestao_campeonato['Histórico Treinadores'][clube_posicao]:
                if Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['vitórias']>=vitorias_min and Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['derrotas'] <= derrotas_max:
                    lista3.append(id_treinador)
                    print(f"> Camisa {Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['camisa']} - {Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['nome']}: {Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['vitórias']} vitórias e {Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_treinador]['derrotas']} derrotas.")

            if len(lista3) ==0:
                print("\n😞  Nenhum treinador atual/antigo foi encontrado com as características desejadas.")

        elif submenu=='2':
                
            aproveitamentos,ids=calcularaproveitamentos()
                    
                
            if len(ids)==0:
                print("\nTodos os treinadores tiveram um aproveitamento de 0%.")
            else:
                melhores=[]
                n_aproveitamento_max=max(aproveitamentos)
                for i in range(len(aproveitamentos)):
                    if aproveitamentos[i]==n_aproveitamento_max:
                        melhores.append(ids[i])
                    
                for id_melhor in melhores:
                    print(f"\n{Gestao_campeonato['Histórico Treinadores'][clube_posicao][id_melhor]['nome']} - aproveitamento: {n_aproveitamento_max}%")
            
        elif submenu=='3':
            aproveitamento_min=validar_float('Insira a percentagem mínima de aproveitamento: ')
            aproveitamentos,ids=calcularaproveitamentos()
            if len(ids)==0:
                print("\nTodos os treinadores tiveram um aproveitamento de 0%.")
            else:
                a=[]
                ids_a=[]
                for i in range(len(aproveitamentos)):
                    if aproveitamentos[i]>=aproveitamento_min:
                        a.append(aproveitamentos[i])
                        ids_a.append(ids[i])
                    
                if len(a)==0:
                    print("😞  Nenhum treinador possui aproveitamento igual ou superior ao solicitado.")
                else:
                    for i in range(len(ids_a)):
                        print(f"{Gestao_campeonato['Histórico Treinadores'][clube_posicao][ids_a[i]]['nome']} - {a[i]}% de aproveitamento.")
        else:
            pass
    elif menuP=='3':
        submenu=input("\n1- Jogos em que o clube marcou pelo menos X golos e sofreu no máximo Y\n2- Mostrar jogos em que o clube venceu por mais de X golos\n3- O desempenho do clube contra um adversário específico, apresentando a percentagem de vitórias, empates e derrotas\n0- Sair\n: ").strip()
        while submenu not in '1230':
            submenu = input("\n\n! COMANDO INVÁLIDO !    Tente novamente: ").strip()
        if submenu=='1':
            n_golos_clube=validar_int('Nº mínimo de golos para o clube: ')
            n_golos_adversario=validar_int('Nº máximo de golos para o adversário: ')

            lista4=[]
            for rodada in Gestao_campeonato['Jogos CB'][clube_posicao]:
                if Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][0]>=n_golos_clube and Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][1] <=n_golos_adversario:
                    lista4.append(rodada)
                    print(f"\n-- {rodada}º rodada --")
                    print(f"golos marcados {Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][0]} - golos sofridos {Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][1]}")
            
            if len(lista4)==0:
                print("Até agora nenhum jogo desputado foi encontrado com essas características.")

        elif submenu=='2':
            n_golos=validar_int('Nº mínimo de golos: ')
            rodadas=[]
            for rodada in Gestao_campeonato['Jogos CB'][clube_posicao]:
                if Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][0]>Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][1] and Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][0]>=n_golos:
                    rodadas.append(rodada)
                    print(f'{rodada}º rodada - {Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][0]} golos marcados e {Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'][1]} golos sofridos.')
                
            if len(rodadas)==0:
                print("Nenhum jogo foi encontrado com essas características.")
        
        elif submenu=='3':
            #o desempenho do clube contra um adversário específico, apresentando a percentagem de vitórias, empates e derrotas
            adversario=input("Nome do adversário: ").strip().title()
            resultados=[]
            for rodada in Gestao_campeonato['Jogos CB'][clube_posicao]:
                if Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['adversário'] ==adversario:
                    resultados.append(Gestao_campeonato['Jogos CB'][clube_posicao][rodada]['golos'])
            
            if len(resultados)==0:
                print(f"Não foram encontrados jogos com o {adversario}.")
            else:
                v=0
                e=0
                d=0
                for resultado in resultados:
                    golosM=resultado[0]
                    golosS=resultado[1]
                    if golosM>golosS:
                        v+=1
                    elif golosM==golosS:
                        e+=1
                    else:
                        d+=1
                try:
                    percentagemV=v*100/len(resultados)
                except ZeroDivisionError:
                    percentagemV=0
                try:
                    percentagemE=e*100/len(resultados)
                except ZeroDivisionError:
                    percentagemE=0
                try:
                    percentagemD=d*100/len(resultados)
                except ZeroDivisionError:
                    percentagemD=0
                
                print(f"Total jogos: {len(resultados)} >  {round(percentagemV,1)}% vitórias - {round(percentagemE,1)}% empates - {round(percentagemD,1)}% derrotas.")
        
        else:
            pass
else:
    print("COMANDO INVÁLIDO")

#Atualizar Ficheiros
