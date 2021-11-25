from random import choice
from os import system

# Um jogo de blackjack deve possuir:
# Um jogador vs um dealer (automático)
# O jogador pode:
#   Stand (Não pedir mais cartas)
#   Hit (Pedir mais cartas)
#   Double (Dobra a aposta para receber SOMENTE UMA carta adicional, opção só oferecida nas duas primeiras cartas)
#   Split (Se as primeiras duas cartas da mão do jogador forem de mesmo valor em pontos, ele pode divir em duas mãos. Cada carta se tornará a primeira carta de uma nova mão. Também DEVE fazer uma outra aposta de valor igual da primeira mão para a segunda mão)
#       O split pode ocorrer de duas a três vezes consecutivas
#   Surrender (Opção de render-se nas duas primeiras cartas. Se o jogador não gostar de suas cartas e quiser render-se ele perde 1/2 da aposta. Opção oferecida após o dealer verificar se há blackjack)
# O jogador deve poder escolher o seu valor de apostas
# É preciso acompanhar o dinheiro total do jogador
# É preciso alertar o jogador de vitórias e derrotas
# Não há cartas coringas
# O ás pode valor 1 ou 11 se estiver junto de uma carta J, Q ou K (deve favorecer o jogador ou computador)
# 10, J, Q e K valem 10
# O total de pontos é 21 (ao passar, perde-se o jogo)
# *Para o projeto é necessário usar POO




# def blackjack():
#     print('Bem vindo ao Blackjack versão texto!')
#     cartas = criar_cartas()
#     qtd_jogadores = quantidade_de_jogadores()
    
#     dealer_ascendente = choice(cartas)
#     carta_furo = choice(cartas)
#     var_dealer = Dealer([carta_furo, dealer_ascendente])
#     print('Carta do dealer virada para cima: {0}'.format(dealer_ascendente))
#     print('REMOVER PRINT NA FINALIZAÇÃO::: carta virada para baixo: {0}'.format(carta_furo))

#     informacao_jogadores = atribuir_nomes_aos_jogadores(qtd_jogadores)

#     var_dealer_list = [{'Cartas' : var_dealer.cartas}]
#     # print('\n\nmão do dealer ANTES: {0}\n\n\n'.format(var_dealer.cartas))
#     # atribuir_cartas(1, var_dealer_list, cartas, 1)
#     # print('\n\nmão do dealer DEPOIS: {0}\n\n\n'.format(var_dealer.cartas))

#     if qtd_jogadores == 1:
#         print('Apenas 1 jogador')
#         aposta = apostas(qtd_jogadores, informacao_jogadores)
#         valor_apostado = aposta
#         # Distribuindo as primeiras cartas
#         atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 2)
#         print('Sua mão é: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#         #if informacao_jogadores[qtd_jogadores-1]['Cartas'].count('Ás') == 1 and (informacao_jogadores[qtd_jogadores-1]['Cartas'].count(10) == 1 or informacao_jogadores[qtd_jogadores-1]['Cartas'].count('J') == 1 or informacao_jogadores[qtd_jogadores-1]['Cartas'].count('Q') == 1 or informacao_jogadores[qtd_jogadores-1]['Cartas'].count('K') == 1):
#         if verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas']) == 21:
#             print('Blackjack!')
#             pagar(qtd_jogadores, informacao_jogadores, informacao_jogadores[qtd_jogadores-1]['Saldo'] + aposta)
#             informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
#             #informacao_jogadores[qtd_jogadores-1]['Cartas'] = []
#     else:
#         print('WIP - Mais que 1 jogador - WIP')
    
#     while True:
#         jogada_escolhida = escuta_jogada(qtd_jogadores, informacao_jogadores, cartas)
#         if jogada_escolhida == 1:
#             print('Dealer revelou a carta furo: {0}'.format(carta_furo))
#             print('Mão do dealer: {0}'.format(var_dealer.cartas))
#             # if var_dealer.cartas.count('Ás') == 1 and (var_dealer.cartas.count(10) == 1 or var_dealer.cartas.count('J') == 1 or var_dealer.cartas.count('Q') == 1 or var_dealer.cartas.count('K') == 1):
#             while True:
#                 if verifica_soma(var_dealer_list['Cartas']) <= 17:
#                     atribuir_cartas(1, var_dealer_list, cartas, 1)
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 break

#             if verifica_soma(var_dealer.cartas) == verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas']):
#                 informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(valor_apostado)
#                 system('cls')
#                 print('\nEmpate!')
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 print('Sua mão: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#             elif verifica_soma(var_dealer.cartas) == 21:
#                 system('cls')
#                 print('\nBlackjack para o dealer!')
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 print('Sua mão: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#                 informacao_jogadores[qtd_jogadores-1]['Derrotas'] += 1
#             elif verifica_soma(var_dealer.cartas) > 21:
#                 system('cls')
#                 print('\nA mão do dealer passou de 21!')
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 print('Sua mão: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#                 informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
#                 pagar(qtd_jogadores, informacao_jogadores, int(valor_apostado))
#             elif verifica_soma(var_dealer.cartas) > verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas']):
#                 system('cls')
#                 print('\nA mão do dealer ficou maior que a sua!')
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 print('Sua mão: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#                 informacao_jogadores[qtd_jogadores-1]['Derrotas'] += 1
#             elif verifica_soma(var_dealer.cartas) < verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas']) and verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas'] <= 21):
#                 system('cls')
#                 print('\nA sua mão ficou maior que a do dealer!')
#                 print('Mão do dealer: {0}'.format(var_dealer.cartas))
#                 print('Sua mão: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
#                 informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
#                 pagar(qtd_jogadores, informacao_jogadores, valor_apostado)

#                 #break
#         elif jogada_escolhida == 2:
#             atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 1)
#             print('\nA carta do dealer virada para cima é: {0}'.format(carta_furo))
#             print('\nSua mão agora é: ', informacao_jogadores[qtd_jogadores-1]['Cartas'])
#             print('\nEscolha 1 para pedir mais uma carta ou 0 para parar de pedir.')
#             while True:
#                 try:
#                     hit = input('1 - Pedir mais uma carta\n0 - Parar de pedir cartas')
#                 except ValueError:
#                     print('ERRO: Escolha apenas entre 1 e 0')
#                 if hit == 1:
#                     atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 1)
#                     print('\nSua mão agora é: ', informacao_jogadores[qtd_jogadores-1]['Cartas'])
#                 else:
#                     break
#         elif jogada_escolhida == 3:
#             if aposta > informacao_jogadores[qtd_jogadores-1]['Saldo']:
#                 print('Ignorando double. Razão: Saldo insuficiente')
#             else:
#                 informacao_jogadores[qtd_jogadores-1]['Saldo'] -= aposta
#                 valor_apostado = aposta * 2
#                 atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 1)
#                 break
#         elif jogada_escolhida == 6:
#             break

#     # Pega o próximo jogador

#     print(informacao_jogadores)

#     #dealer(qtd_jogadores, informacao_jogadores, cartas)
# blackjack()



# Classe para a criação dos jogadores
class Jogador(object):
    def __init__(self, nome, posicao = 1, saldo=100, vitorias=0, derrotas=0):
        self.nome = nome
        self.posicao = posicao
        self.saldo = saldo
        self.vitorias = vitorias
        self.derrotas = derrotas
    
    # Função para retornar retornar o nome em formato de string ao invés de endereço de memória (usado para o dictionary)
    def __repr__(self):
        return '{0}'.format(self.nome)


class Dealer(Jogador):
    def __init__(self, cartas):
        self.nome = 'Dealer'
        self.cartas = cartas
    
    # Função para retornar retornar o nome em formato de string ao invés de endereço de memória (usado para o dictionary)
    def __repr__(self):
        return '{0}'.format(self.nome)


# Função de criação das cartas
def criar_cartas():
    '''
    Função que cria o baralho de cartas e retorna  8 baralhos idênticos. Retorna list
    '''
    cartas = [i for i in range(2, 11)]
    cartas.insert(0, 'Ás')
    cartas.append('J')
    cartas.append('Q')
    cartas.append('K')
    return cartas*8


# Função que recebe e verifica a quantidade de jogadores (tratando erro se necessário)
def quantidade_de_jogadores():
    '''
    Função que pede por um input int que retornará a quantidade de jogadores que participarão da partida. Retorna int
    '''
    while True:
        try:
            qtd_jogadores = int(input('Quantas pessoas jogarão? (Escolha um número de 1 a 7)'))
            if qtd_jogadores > 0 and qtd_jogadores <= 7:
                break
            else:
                print('O limite de 7 jogadores deve ser respeitado. Escolha a quantidade de jogadores de 1 a 7.')
        except ValueError:
            print('ERRO: Digite apenas quantos jogadores irão jogar.')
    return qtd_jogadores


# Função que atribui um nome ou apelido ao jogador, justamente criando instâncias da classe Jogador. Armazena o jogador em um dictionary e os jogadores em uma lista.
def atribuir_nomes_aos_jogadores(numero_de_jogadores):
    '''
    Função que recebe como atributo a quantidade de jogadores que participarão do jogo e os separam em dictonaries com valores que possibilitam uma fácil identificação como nome/apelido e sua posição no jogo. Retorna list
    '''
    jogadores = []
    for numero in range(1, numero_de_jogadores+1):
        jogador = {'Nome' : str, 'Posicao' : numero, 'Saldo' : 20000, 'Vitorias' : 0, 'Derrotas' : 0, 'Cartas' : []}
        jogador['Nome'] = Jogador(nome = input('Jogador {0}, digite seu nome ou apelido: '.format(numero)))
        jogadores.append(jogador)
    return jogadores

    
def atribuir_dealer():
    dealer_list = []
    dealer = {'Nome' : 'Dealer', 'Cartas' : []}
    dealer_list.append(dealer)
    return dealer_list


def apostas(qtd_jogadores, informacao_jogadores):
    while True:
        try:
            aposta = int(input('Caro jogador, faça sua aposta: '))
            if informacao_jogadores[qtd_jogadores-1]['Saldo'] - aposta >= 0:
                print('R$', aposta)
                informacao_jogadores[qtd_jogadores-1]['Saldo'] -= aposta
                break
        except ValueError:
            print('Digite um valor inteiro e válido.')
        else:
            print('SEM SALDO')
    return aposta


def atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, vezes = 1):
    for i in range(0, vezes):
        informacao_jogadores[qtd_jogadores-1]['Cartas'].append(choice(cartas))


# Função que retorna a jogada escolhida pelo jogador para ser usado na função dealer(qtd_jogadores).
def escuta_jogada(qtd_jogadores, informacao_jogadores, cartas):
    '''
    Função que recebe o jogador que está jogando no momento e retorna um int(input()) que será usado como decisão de jogada. Retorna int
    '''
    while True:
        try:
            jogada = int(input('Escolha de jogadas:\n{0}, qual jogada gostaria de realizar?\n1-)Stand\n2-)Hit\n3-)Double\n4-)Split\n5-)Surrender\n6-)Sair'.format(informacao_jogadores[qtd_jogadores-1]['Nome'])))
            if jogada > 0 and jogada <= 6:
                break
            else:
                print('Existem 5 opções numeradas de 1 a 5. Para escolher a jogada, escolha uma entre elas.')
        except ValueError:
            print('ERRO: Use o teclado numérico para escolher apenas uma das jogadas citadas.')

    if jogada == 1:
        print('Stand.')
        return 1

    elif jogada == 2:
        print('Hit.')
        return 2

    elif jogada == 3:
        print('Double.')
        return 3

    elif jogada == 4:
        print('Split.')
        return 4

    elif jogada == 5:
        print('Surrender.')
        return 5

    elif jogada == 6:
        system('cls')
        print('Saindo...')
        print('Obrigado por jogar!')
        return 6


def verifica_soma(cartas):
    soma = 0
    soma2 = 0
    for carta in range(len(cartas)):
        if cartas[carta] == 'J':
            cartas[carta] = 10
            #print(cartas)
        elif cartas[carta] == "Q":
            cartas[carta] = 10
            #print(cartas)
        elif cartas[carta] == 'K':
            cartas[carta] = 10
            #print(cartas)

        if cartas[carta] == 'Ás':
            if soma == 10:
                cartas[carta] = 11
            elif soma < 10:
                cartas[carta] = 11
            elif soma > 10:
                cartas[carta] = 1
        soma += cartas[carta]    
    #print(cartas) # Retirar depois
    for as_11 in range(len(cartas)):
        if (soma - 10) > 11 and cartas[as_11] == 11:
            cartas[as_11] = 1
        soma2 += cartas[as_11]
    #print(cartas) # Retirar depois
    return int(soma2)
        
            
def pagar(qtd_jogadores, informacao_jogadores, aposta, blackjack : bool):
    if blackjack:
        informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta) + (3/2)*int(aposta)
    else:
        informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta) * 2



def acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas):
    # Bloco if, atribui cartas ao dealer e ao jogador caso ambos não possuam cartas ainda.
    if dealer[0]['Cartas'] == [] and informacao_jogadores[qtd_jogadores-1]['Cartas'] == []:
        print('Distribuindo cartas...')
        atribuir_cartas(1, dealer, cartas, 2)
        print('CARTAS DO DEALER:\nCartas iniciais: {2}\nCarta virada para cima: {0}\nCarta virada para baixo: {1}'.format(dealer[0]['Cartas'][0], dealer[0]['Cartas'][1], dealer[0]['Cartas'])) # Retirar depois
        atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 2)
        print('CARTAS DO JOGADOR:\nCartas iniciais: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas'])) # Retirar depois
    else:
        print('Tem item DEALER: {0}\nJOGADOR: {1}'.format(dealer, informacao_jogadores[qtd_jogadores-1]['Cartas'])) # Retirar depois


def verificar_blackjack(dealer, jogador):
    if verifica_soma(dealer[0]['Cartas']) == verifica_soma(jogador):
        print('Empate!')
    elif verifica_soma(dealer[0]['Cartas']) != 21 and verifica_soma(jogador) == 21:
        print('Blackjack para o jogador!')
    elif verifica_soma(jogador) != 21 and verifica_soma(dealer[0]['Cartas']) == 21:
        print('Blackjack para o dealer!')
    elif verifica_soma(dealer[0]['Cartas']) > 21:
        print('Jogador vence porque o dealer tem uma mão que passa de 21!')
    elif verifica_soma(jogador) > 21:
        print('Dealer vence porque o jogador tem uma mão que passa de 21!')
    elif verifica_soma(dealer[0]['Cartas']) < 21 and verifica_soma(dealer[0]['Cartas']) > verifica_soma(jogador):
        print('Dealer vence por ter uma mão maior que a do jogador!')
    elif verifica_soma(jogador) < 21 and verifica_soma(jogador) > verifica_soma(dealer[0]['Cartas']):
        print('Jogador vence por ter uma mão maior que a do dealer!')


def iniciar():
    print('Bem vindo ao Blackjack versão texto!')
    # Retorna uma lista com 8 baralhos de cartas
    cartas = criar_cartas() 
    qtd_jogadores = quantidade_de_jogadores()
    informacao_jogadores = atribuir_nomes_aos_jogadores(qtd_jogadores)
    print(informacao_jogadores) # Retirar depois
    dealer = atribuir_dealer()
    print(dealer) # Retirar depois
    aposta = apostas(qtd_jogadores, informacao_jogadores)
    acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
    print(informacao_jogadores) # Retirar depois
    verificar_blackjack(dealer, informacao_jogadores[qtd_jogadores-1]['Cartas'])
    pagar(qtd_jogadores, informacao_jogadores, aposta, True)
    print(informacao_jogadores) # Retirar depois

iniciar()



