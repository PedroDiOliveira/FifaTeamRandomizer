import random
import json

###################################
##Caminhos para arquivos externos##
###################################
##Nao esquecer de colocar 2 barras entre casa caminho para o codigo nao dar erro de leitura

caminhoParticipantes = 'C:\\Users\\Pedro.doliveira\\Desktop\\fifinha\\input\\Participantes.txt'
caminhoClubes = 'C:\\Users\\Pedro.doliveira\\Desktop\\fifinha\\input\\Clubes.txt'
caminhoLogs = 'C:\\Users\\Pedro.doliveira\\Desktop\\fifinha\\saves\\logs.txt'


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
    # lista = [grupo1, grupo2, grupo3, grupo4]

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

    
    print(potes[0])
    print(potes[1])
    print(potes[2])
    print(potes[3])
        

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
            if verificaArquivoVazio(caminhoParticipantes):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Participantes.txt'.")
            else:
                nomes = recebeNomes()
                print(f'''Participantes:  {nomes}''')
                continue
        elif opcao == 2:##Abre o arquivo txt de clubes e mostra todos na tela
            if verificaArquivoVazio(caminhoClubes):
                print("O arquivo parece estar vazio parece estar vazio! Por favor informe os participantes no arquivo 'Clubes.txt'.")
            else:
                clubes = recebeClubes()
                print(f'''Participantes:  {clubes}''')
                continue
        elif opcao == 3:#Verifica se o arquivo de save esta vazio, caso esteja, ele sorteia e manda um novo save!
            if not verificaArquivoVazio(caminhoLogs):
                sobrepor = int(input("Parece que ja existe um save anterior! Deseja sobrepor o antigo save?(1-sim/2-nao)"))
                if sobrepor == 1:#caso ja tenha um save ele pergunta ao usuario se quer apagar o save antigo e sorteia novamente
                    resultados = sorteio()
                    with open(caminhoLogs, 'w') as arquivo:
                        arquivo.write('')
                    with open(caminhoLogs, 'w') as arquivo:
                        for jogador, timesorteio in resultados.items():
                            arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")       
                else:
                    continue
            else:
                resultados = sorteio()
                with open(caminhoLogs, 'w') as arquivo:
                    for jogador, timesorteio in resultados.items():
                        arquivo.write(f"Jogador: {jogador.ljust(12)}    Time: {timesorteio}\n")
        elif opcao == 4:
            with open(caminhoParticipantes, 'r') as arquivo:
                nomes = arquivo
                


    

menu()

#SeparaGrupos()
