import random
import json

##########################################
##Funcao que retorna os nomes dos Clubes##
##########################################

def recebeClubes():

    with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\input\\Clubes.txt', 'r') as arquivo_times:
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

    with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\input\\Participantes.txt', 'r') as arquivo_nomes:
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
    with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\saves\\logs.txt', 'w') as arquivo:
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
    pote1.append(nomes[0])
    pote1.append(nomes[1])
    pote1.append(nomes[2])
    pote1.append(nomes[3])
    pote2.append(nomes[4])
    pote2.append(nomes[5])
    pote2.append(nomes[6])
    pote2.append(nomes[7])
    pote3.append(nomes[8])
    pote3.append(nomes[9])
    pote3.append(nomes[10])
    pote3.append(nomes[11])
    pote4.append(nomes[12])
    pote4.append(nomes[13])
    pote4.append(nomes[14])
    pote4.append(nomes[15])

    print(f" Pote 1: {pote1} \n Pote 2: {pote2} \n Pote 3: {pote3} \n Pote 4: {pote4}")
    



########################################
##Funcao do menu principal de execucao##
########################################

def menu():
    sair = False
    print('''
          |-------------------------------------------------------|
          |                                                       |
          |  Bem vindo a x edicao do campeonato de Fifa do Betas  |
          |                                                       |
          |-------------------------------------------------------|

          1- Mostrar participantes
          2- Mostrar times
          3- Sortear times
          4- Sortear Confrontos  
          5- Players Log               
          6- Confrontos Log
          7- Menu De Exclusao
          8- Fechar programa                                                     
          ''')
    
    while not sair:
        print("")
        opcao = int(input("Digite uma opcao: "))
        if opcao == 1:#Abre o arquivo txt de participantes e mostra todos na tela
            if verificaArquivoVazio('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\input\\Participantes.txt'):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Participantes.txt'.")
            else:
                nomes = recebeNomes()
                print(f'''Participantes:  {nomes}''')
                continue
        elif opcao == 2:##Abre o arquivo txt de clubes e mostra todos na tela
            if verificaArquivoVazio('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\input\\Clubes.txt'):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Clubes.txt'.")
            else:
                clubes = recebeClubes()
                print(f'''Participantes:  {clubes}''')
                continue
        elif opcao == 3:#Verifica se o arquivo de save esta vazio, caso esteja, ele sorteia e manda um novo save!
            if not verificaArquivoVazio('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\saves\\logs.txt'):
                sobrepor = int(input("Parece que ja existe um save anterior! Deseja sobrepor o antigo save?(1-sim/2-nao)"))
                if sobrepor == 1:#caso ja tenha um save ele pergunta ao usuario se quer apagar o save antigo e sorteia novamente
                    resultados = sorteio()
                    with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\saves\\logs.txt', 'w') as arquivo:
                        arquivo.write('')
                    with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\saves\\logs.txt', 'w') as arquivo:
                        for jogador, timesorteio in resultados.items():
                            arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")       
                else:
                    continue
            else:
                resultados = sorteio()
                with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\saves\\logs.txt', 'w') as arquivo:
                    for jogador, timesorteio in resultados.items():
                        arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")
        elif opcao == 4:
            with open('C:\\Users\\pedro\\FIFA\\FifaTeamRandomizer\\input\\Participantes.txt', 'r') as arquivo:
                nomes = arquivo


    

#menu()

separaPotes()