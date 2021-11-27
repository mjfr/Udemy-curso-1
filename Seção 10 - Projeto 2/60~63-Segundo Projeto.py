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
            aposta = int(input('Caro jogador neste momento você possui [SALDO: {0}], faça sua aposta: '.format(informacao_jogadores[qtd_jogadores-1]['Saldo'])))
            if informacao_jogadores[qtd_jogadores-1]['Saldo'] - aposta >= 0:
                print('R$', aposta)
                informacao_jogadores[qtd_jogadores-1]['Saldo'] -= aposta
                break
        except ValueError:
            print('Digite um valor inteiro e válido.')
        else:
            print('SEM SALDO, NESTE CASO DIGITE 0 e depois 7 para sair do jogo. Então comece um novo jogo :)')
    return aposta


def atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, vezes = 1):
    for i in range(0, vezes):
        informacao_jogadores[qtd_jogadores-1]['Cartas'].append(choice(cartas))


# Função que retorna a jogada escolhida pelo jogador para ser usado na função dealer(qtd_jogadores).
def escuta_jogada(qtd_jogadores, informacao_jogadores):
    '''
    Função que recebe o jogador que está jogando no momento e retorna um int(input()) que será usado como decisão de jogada. Retorna int
    '''
    while True:
        try:
            jogada = int(input('Escolha de jogadas:\n{0}, qual jogada gostaria de realizar?\n1-)Stand\n2-)Hit\n3-)Double\n4-)Split\n5-)Surrender\n7-)Sair'.format(informacao_jogadores[qtd_jogadores-1]['Nome'])))
            if jogada > 0 and jogada <= 7:
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
        system('cls') # Remover depois
        print('WIP\nÉ uma jogada que o jogador que possui duas cartas iguais na mão inicial pode fazer.\nEle divide sua mão em dois, aposta para cada mão e no fim compara as duas mãos com a mesma mão do dealer') # Remover depois
        return 4

    elif jogada == 5:
        print('Insurance.')
        system('cls') # Remover depois
        print('WIP\nÉ uma jogada que é "nosciva" para não contadores de cartas. Geralmente favorece a casa') # Remover depois
        return 5

    elif jogada == 6:
        print('Surrender.')
        system('cls') # Remover depois
        print('WIP\nEm essência funciona mais para aplicações com persistência de dados ou na vida real.\nÉ uma escolha que o jogador para de jogar, porém matém metade do valor de sua aposta.\n Logo, não será implementado') # Remover depois
        return 6

    elif jogada == 7:
        system('cls')
        print('Saindo...')
        print('Obrigado por jogar!')
        return 7


# Dependendo do ponto de vista, é uma função 50% desnecessária uma vez que se eu colocasse verificações para uma carta
# que vale 1 (Ás), dependendo da ocasião, 1 poderia ser igual a 11 e as cartas J Q K poderiam simplesmente valer 10
# sem precisar de verificação para transformar a carta símbolo em número
def verifica_soma(cartas):
    soma = 0
    soma2 = 0
    for carta in range(len(cartas)):
        if cartas[carta] == 'J':
            cartas[carta] = 10
        elif cartas[carta] == "Q":
            cartas[carta] = 10
        elif cartas[carta] == 'K':
            cartas[carta] = 10

        if cartas[carta] == 'Ás':
            if soma == 10:
                cartas[carta] = 11
            elif soma < 10:
                cartas[carta] = 11
            elif soma > 10:
                cartas[carta] = 1
        soma += cartas[carta]
    for as_11 in range(len(cartas)):
        if (soma - 10) > 11 and cartas[as_11] == 11:
            cartas[as_11] = 1
        soma2 += cartas[as_11]
    return int(soma2)
        
            
def pagar(qtd_jogadores, informacao_jogadores, aposta, blackjack : bool, double = False):
    # Double False:
    if double == False:
        if blackjack:
            informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta) + (3/2)*int(aposta)
        else:
            informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta) * 2
    # Double True
    if double:
        if blackjack:
            informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta*2) + (3/2)*int(aposta*2)
        else:
            informacao_jogadores[qtd_jogadores-1]['Saldo'] += int(aposta*2) * 2



def acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas):
    # Bloco if, atribui cartas ao dealer e ao jogador caso ambos não possuam cartas ainda.
    if dealer[0]['Cartas'] == [] and informacao_jogadores[qtd_jogadores-1]['Cartas'] == []:
        print('Distribuindo cartas...')
        atribuir_cartas(1, dealer, cartas, 2)
        atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 2)
    else:
        print('Distribuindo outra mão')
        dealer[0]['Cartas'] = []
        informacao_jogadores[qtd_jogadores-1]['Cartas'] = []
        atribuir_cartas(1, dealer, cartas, 2)
        atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 2)


def verificar_blackjack(dealer, jogador):
    if verifica_soma(dealer[0]['Cartas']) == verifica_soma(jogador):
        print('Empate!')
        return None
    elif verifica_soma(dealer[0]['Cartas']) != 21 and verifica_soma(jogador) == 21:
        print('Blackjack para o jogador!')
        return 'Blackjack'
    elif verifica_soma(jogador) != 21 and verifica_soma(dealer[0]['Cartas']) == 21:
        print('Blackjack para o dealer!')
        return False
    elif verifica_soma(dealer[0]['Cartas']) > 21:
        print('Jogador vence porque o dealer tem uma mão que passa de 21!')
        return True
    elif verifica_soma(jogador) > 21:
        print('Dealer vence porque o jogador tem uma mão que passa de 21!')
        return False
    elif verifica_soma(dealer[0]['Cartas']) < 21 and verifica_soma(dealer[0]['Cartas']) > verifica_soma(jogador):
        print('Dealer vence por ter uma mão maior que a do jogador!')
        return False
    elif verifica_soma(jogador) < 21 and verifica_soma(jogador) > verifica_soma(dealer[0]['Cartas']):
        print('Jogador vence por ter uma mão maior que a do dealer!')
        return True


def acao_verificar_blackjack(vb, dealer, informacao_jogadores, qtd_jogadores, aposta, cartas, double = False):
        if vb == 'Blackjack':
            informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
            if double:
                pagar(qtd_jogadores, informacao_jogadores, aposta, True, True)
            else:
                pagar(qtd_jogadores, informacao_jogadores, aposta, True, False)
            print('Parabéns {0}, você ganhou e estes são seus seguintes status: {1}'.format(informacao_jogadores[qtd_jogadores-1]['Nome'], informacao_jogadores[qtd_jogadores-1]))
            acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
        elif vb == None:
            if double:               
                informacao_jogadores[qtd_jogadores-1]['Saldo'] += aposta*2
            else:
                informacao_jogadores[qtd_jogadores-1]['Saldo'] += aposta
            print('Como empatou, você recebe o valor de sua aposta de volta e uma nova mão será distribuida')
            acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
        elif vb == True:
            informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
            if double:
                pagar(qtd_jogadores, informacao_jogadores, aposta, False, True)
            else:
                pagar(qtd_jogadores, informacao_jogadores, aposta, False, False)
            print('Parabéns {0}, você ganhou e estes são seus seguintes status: {1}'.format(informacao_jogadores[qtd_jogadores-1]['Nome'], informacao_jogadores[qtd_jogadores-1]))
            acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
        else:
            informacao_jogadores[qtd_jogadores-1]['Derrotas'] += 1
            print('Que pena {0}! Você perdeu e estes são seus seguintes status: {1}'.format(informacao_jogadores[qtd_jogadores-1]['Nome'], informacao_jogadores[qtd_jogadores-1]))
            acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)

def iniciar():
    print('Bem vindo ao Blackjack versão texto!')
    cartas = criar_cartas() 
    qtd_jogadores = quantidade_de_jogadores()
    informacao_jogadores = atribuir_nomes_aos_jogadores(qtd_jogadores)
    dealer = atribuir_dealer()
    acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
    while True:
        aposta = apostas(qtd_jogadores, informacao_jogadores)
        print('{0}, essa é a sua mão: {1}\n{0}, essa é a carta do dealer que está virada para cima: {2}'.format(informacao_jogadores[qtd_jogadores-1]['Nome'], informacao_jogadores[qtd_jogadores-1]['Cartas'], dealer[0]['Cartas'][0]))
        jogada = escuta_jogada(qtd_jogadores, informacao_jogadores)
        # Caso 7, sair! O jogador não quer mais jogar, logo, fecha o programa
        if jogada == 7:
            break
        # Caso 1, stand! O jogador não recebe mais cartas enquanto o dealer revela a sua e se necessário compra mais cartas.
        if jogada == 1:
            if verifica_soma(dealer[0]['Cartas']) < 17:
                while verifica_soma(dealer[0]['Cartas']) < 17:
                    atribuir_cartas(1, dealer, cartas, 1)
            system('cls')
            print('O dealer revelou a segunda carta: [{0}, {1}]'.format(dealer[0]['Cartas'][0], dealer[0]['Cartas'][1]))
            print('A mão do dealer ficou: {0}\nA mão do jogador ficou: {1}'.format(dealer[0]['Cartas'], informacao_jogadores[qtd_jogadores-1]['Cartas']))
            vb = verificar_blackjack(dealer, informacao_jogadores[qtd_jogadores-1]['Cartas'])

            acao_verificar_blackjack(vb, dealer, informacao_jogadores, qtd_jogadores, aposta, cartas)

        # Caso 2, hit! O jogador pegará mais cartas
        if jogada == 2:
            parar = 0
            while parar == 0:
                if verifica_soma(informacao_jogadores[qtd_jogadores-1]['Cartas']) > 21:
                    print('Não pode comprar mais cartas, perdeu por passar de 21')
                    informacao_jogadores[qtd_jogadores-1]['Derrotas'] += 1
                    acoes_dealer(qtd_jogadores, dealer, informacao_jogadores, cartas)
                    break
                else:
                    print('A sua mão é: {0}'.format(informacao_jogadores[qtd_jogadores-1]['Cartas']))
                    try:
                        parar = int(input('Digite 1 para parar ou 0 para pedir mais uma carta: '))
                        if parar == 0:
                            atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 1)
                    except ValueError:
                        print('ERRO: Use o teclado numérico para escolher apenas entre 0 e 1.')

            if parar == 1:
                if verifica_soma(dealer[0]['Cartas']) < 17:
                    while verifica_soma(dealer[0]['Cartas']) < 17:
                        atribuir_cartas(1, dealer, cartas, 1)

            system('cls')
            print('O dealer revelou a segunda carta: [{0}, {1}]'.format(dealer[0]['Cartas'][0], dealer[0]['Cartas'][1]))
            print('A mão do dealer ficou: {0}\nA mão do jogador ficou: {1}'.format(dealer[0]['Cartas'], informacao_jogadores[qtd_jogadores-1]['Cartas']))
            vb = verificar_blackjack(dealer, informacao_jogadores[qtd_jogadores-1]['Cartas'])
            acao_verificar_blackjack(vb, dealer, informacao_jogadores, qtd_jogadores, aposta, cartas)

        if jogada == 3:
            if informacao_jogadores[qtd_jogadores-1]['Saldo'] - aposta >= 0:
                informacao_jogadores[qtd_jogadores-1]['Saldo'] -= aposta
                atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 1)
                if verifica_soma(dealer[0]['Cartas']) < 17:
                    while verifica_soma(dealer[0]['Cartas']) < 17:
                        atribuir_cartas(1, dealer, cartas, 1)
            else:
                print('Saldo insuficiente para um double.')
            
            system('cls')
            print('O dealer revelou a segunda carta: [{0}, {1}]'.format(dealer[0]['Cartas'][0], dealer[0]['Cartas'][1]))
            print('A mão do dealer ficou: {0}\nA mão do jogador ficou: {1}'.format(dealer[0]['Cartas'], informacao_jogadores[qtd_jogadores-1]['Cartas']))
            vb = verificar_blackjack(dealer, informacao_jogadores[qtd_jogadores-1]['Cartas'])
            acao_verificar_blackjack(vb, dealer, informacao_jogadores, qtd_jogadores, aposta, cartas, True)

iniciar()