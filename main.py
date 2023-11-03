import random
import json
import os
import time

###################################
##Caminhos para arquivos externos##
###################################
##Nao esquecer de colocar 2 barras entre casa caminho para o codigo nao dar erro de leitura

caminhoParticipantes = 'C:\\Users\\pedro\\fifa\\FifaTeamRandomizer\\input\\Participantes.txt'
caminhoClubes = 'C:\\Users\\pedro\\fifa\\FifaTeamRandomizer\\input\\Clubes.txt'
caminhoLogs = 'C:\\Users\\pedro\\fifa\\FifaTeamRandomizer\\saves\\logs.txt'
caminhoConfrontos = 'C:\\Users\\pedro\\fifa\\FifaTeamRandomizer\\saves\\confrontos.txt'


##########################################
##Funcao que retorna os nomes dos Clubes##
##########################################

def recebeClubes():

    with open(caminhoClubes, 'r') as arquivo_times:
        linhas = arquivo_times.read().splitlines()

    times = []
    for linha in linhas:
        linha = linha.strip() 
        palavras = linha.split()
        times.extend(palavras)

    return times

#################################################
##Funcao que retorna os nomes dos participantes##
#################################################

def recebeNomes():

    with open(caminhoParticipantes, 'r') as arquivo_nomes:
        linhas = arquivo_nomes.read().splitlines()

    nomes = []
    for linha in linhas:
        linha = linha.strip()  
        palavras = linha.split()
        nomes.extend(palavras)

    return nomes


#####################################################################################
##Funcao que sorteia os jogadores e cria um dicionario para armazenar os resultados##
#####################################################################################

def sorteio():
    resultadosJogador = {}
    times = recebeClubes()
    jogadores = recebeNomes()
    
    for jogador in jogadores:#TODO
        for i in range(len(jogadores)):
            timesorteio = random.choice(times)
            times.remove(timesorteio)
            resultadosJogador[jogador] = timesorteio
            print(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}")
            break
            
    return resultadosJogador

#########################################################
##Funcao que pega o dicionario e salva em um aquivo txt##
#########################################################

def salvaResultados(jogadores, times):#TODO
    with open(caminhoLogs, 'w') as arquivo:
        print(X)    

################################################
##Funcao que verifica se um arquivo esta vazio##
################################################

def verificaArquivoVazio(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        return not conteudo
    
###############################################
##Funcao para lidar com a separacao dos potes##
###############################################

def separaPotes():
    nomes = recebeNomes()

    pote1 = []
    pote2 = []
    pote3 = []
    pote4 = []

    potes = [
        pote1,
        pote2,
        pote3,
        pote4
    ]

    if len(nomes) < 16:
        print('Nao ha nomes para preencher corretamente os potes.')
        return

    x = 0
    for i in range(4):
       #1 sorteio
       potes[i].append(nomes[x])
    
       #2 sorteio
       potes[i].append(nomes[x + 1])

       #3 sorteio
       potes[i].append(nomes[x + 2])
    
       #4 sorteio
       potes[i].append(nomes[x + 3])

       x = x + 4
    #print(f" Pote 1: {pote1} \n Pote 2: {pote2} \n Pote 3: {pote3} \n Pote 4: {pote4}")

    return pote1, pote2, pote3, pote4

###############################
##Funcao que separa os grupos##
###############################

def SeparaGrupos():
    i = 0
    p1,p2,p3,p4 = separaPotes()
    grupo1 = []
    grupo2 = []
    grupo3 = []
    grupo4 = []

    potes = [
        grupo1,
        grupo2,
        grupo3,
        grupo4,
    ]    
    x = 3

    for i in range(4):
       #1 sorteio
       indexAleatorio = random.randint(0,x)
       potes[i].append(p1[indexAleatorio])
       p1.remove(p1[indexAleatorio])

       #2 sorteio
       indexAleatorio = random.randint(0,x)
       potes[i].append(p2[indexAleatorio])
       p2.remove(p2[indexAleatorio])

       #3 sorteio
       indexAleatorio = random.randint(0,x)
       potes[i].append(p3[indexAleatorio])
       p3.remove(p3[indexAleatorio])

       #4 sorteio
       indexAleatorio = random.randint(0,x)
       potes[i].append(p4[indexAleatorio])
       p4.remove(p4[indexAleatorio])    

       x -= 1

    
    print(f"Grupo 1 -> {potes[0]}")
    print(f"Grupo 2 -> {potes[1]}")
    print(f"Grupo 3 -> {potes[2]}")
    print(f"Grupo 4 -> {potes[3]}")

    return potes[0], potes[1], potes[2], potes[3]

#######################################
##Funcao que cria uma tela de loading##
#######################################

def animacao():
    os.system("cls")
    for i in range(1, 11):  
        print("Loading [" + "=" * i + " " * (10 - i) + "] " + str(i * 10) + "%")
        time.sleep(0.3)
        os.system('cls')

####################################
##Funcao que sorteia os confrontos##
####################################

def sorteio_confrontos():
    potes = SeparaGrupos()
    confrontos_potes = []

    # Gerar uma lista de todos os confrontos possíveis por pote
    for pote in potes:
        confrontos_pote = [(jogador1, jogador2) for i, jogador1 in enumerate(pote) for jogador2 in pote[i+1:] if jogador1 != jogador2]
        confrontos_potes.append(confrontos_pote)

    # Embaralhar a lista de confrontos dentro de cada pote
    for confrontos_pote in confrontos_potes:
        random.shuffle(confrontos_pote)

    # Imprimir os confrontos organizados por pote
    with open(caminhoConfrontos, 'w') as arquivo:
        for i, pote in enumerate(potes, start=1):
            arquivo.write(f"Pote {i}:\n")
            for confronto in confrontos_potes[i - 1]:
                jogador1, jogador2 = confronto
                arquivo.write(f"{jogador1} x {jogador2}\n")
            arquivo.write("\n")



########################################
##Funcao do menu principal de execucao##
########################################

def menu():
    sair = False
    os.system('cls')
    
    while not sair:
        print('''
          |-------------------------------------------------------------|
          |                                                             |
          |  Bem vindo la setima edicao do campeonato de Fifa do Betas  |
          |                                                             |
          |-------------------------------------------------------------|

          1- Mostrar participantes
          2- Mostrar times
          3- Sortear times
          4- Sortear Confrontos  
          5- Sair do programa                                                     
          ''')
        print("")
        opcao = int(input("Digite uma opcao: "))
        if opcao == 1:#Abre o arquivo txt de participantes e mostra todos na tela
            if verificaArquivoVazio(caminhoParticipantes):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Participantes.txt'.")
            else:
                nomes = recebeNomes()
                print(f'''Participantes:  {nomes}''')
                time.sleep(2)
                continue
        elif opcao == 2:##Abre o arquivo txt de clubes e mostra todos na tela
            if verificaArquivoVazio(caminhoClubes):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Clubes.txt'.")
            else:
                clubes = recebeClubes()
                print(f'''Participantes:  {clubes}''')
                time.sleep(2)
                continue
        elif opcao == 3:#Verifica se o arquivo de save esta vazio, caso esteja, ele sorteia e manda um novo save!
            if not verificaArquivoVazio(caminhoLogs):
                sobrepor = int(input("Parece que ja existe um save anterior! Deseja sobrepor o antigo save?(1-sim/2-nao)"))
                if sobrepor == 1:#caso ja tenha um save ele pergunta ao usuario se quer apagar o save antigo e sorteia novamente
                    animacao()
                    resultados = sorteio()
                    with open(caminhoLogs, 'w') as arquivo:
                        arquivo.write('')
                    with open(caminhoLogs, 'w') as arquivo:
                        for jogador, timesorteio in resultados.items():
                            arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")       
                else:
                    continue
            else:
                animacao()
                resultados = sorteio()
                with open(caminhoLogs, 'w') as arquivo:
                    for jogador, timesorteio in resultados.items():
                        arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")
        elif opcao == 4:
            if verificaArquivoVazio(caminhoConfrontos):
                sorteio_confrontos()
            else:
                sobrepor = int(input("Parece que ja existe um save anterior! Deseja sobrepor o antigo save?(1-sim/2-nao)"))
                if sobrepor == 1:#caso ja tenha um save ele pergunta ao usuario se quer apagar o save antigo e sorteia novamente
                    animacao()
                    with open(caminhoLogs, 'w') as arquivo:
                        arquivo.write('')
                    sorteio_confrontos()       
                else:
                    continue

        elif opcao == 5:
            print("Saindo do programa!")
            sair = True

################################
##Funcao principal de execucao##
################################

menu()
