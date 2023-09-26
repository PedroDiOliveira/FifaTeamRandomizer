import random

##########################################
##Funcao que retorna os nomes dos Clubes##
##########################################

def recebeClubes():
    # Passo 1: Leitura do arquivo de texto
    with open('C:\\Users\\pedro\\FIFA\\texto\\Clubes.txt', 'r') as arquivo_times:
        linhas = arquivo_times.read().splitlines()

    # Passo 2: Processamento das linhas e criação da lista de times
    times = []
    for linha in linhas:
        linha = linha.strip()  # Remove espaços em branco no início e no final da linha
        palavras = linha.split()
        times.extend(palavras)

    return times

#################################################
##Funcao que retorna os nomes dos participantes##
#################################################

def recebeNomes():
    # Passo 1: Leitura do arquivo de texto
    with open('C:\\Users\\pedro\\FIFA\\texto\\Participantes.txt', 'r') as arquivo_nomes:
        linhas = arquivo_nomes.read().splitlines()

    # Passo 2: Processamento das linhas e criação da lista de times
    nomes = []
    for linha in linhas:
        linha = linha.strip()  # Remove espaços em branco no início e no final da linha
        palavras = linha.split()
        nomes.extend(palavras)

    return nomes

times = recebeClubes()
jogadores = recebeNomes()

for jogador in jogadores:
    for i in range(len(jogadores)):
        timesorteio = random.choice(times)
        times.remove(timesorteio)
        print(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}")
        break

