from random import choice

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

# class Dealer(Jogador):
#     def __init__(self, nome='Dealer', posicao=1, vitorias=0, derrotas=0):
#         self.nome = nome
#         self.vitorias = vitorias
#         self.derrotas = derrotas
        
#     def __repr__(self):
#         return '{0}'.format(self.nome)


# Função de criação das cartas
def criar_cartas():
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
    Função que recebe como atributo a quantidade de jogadores que participarão do jogo e os separam em dictonaries com valores que possibilitam uma fácil identificação como nome/apelido e sua posição no jogo. Retorna lista
    '''
    jogadores = []
    for numero in range(1, numero_de_jogadores+1):
        jogador = {'Nome' : str, 'Posicao' : numero, 'Saldo': 100, 'Vitorias' : 0, 'Derrotas' : 0, 'Cartas' : []}
        jogador['Nome'] = Jogador(nome = input('Jogador {0}, digite seu nome ou apelido: '.format(numero)))
        jogadores.append(jogador)
    return jogadores

# Função que retorna a jogada escolhida pelo jogador para ser usado na função dealer(qtd_jogadores).
def escuta_jogada(jogador):
    '''
    Função que recebe o jogador que está jogando no momento e retorna um int(input()) que será usado como decisão de jogada. Retorna int
    '''
    while True:
        try:
            jogada = int(input('Escolha de jogadas:\n{0}, qual jogada gostaria de realizar?\n1-)Stand\n2-)Hit\n3-)Double\n4-)Split\n5-)Surrender\n'.format(jogador)))
            if jogada > 0 and jogada <= 5:
                break
            else:
                print('Existem 5 opções numeradas de 1 a 5. Para escolher a jogada, escolha uma entre elas.')
        except ValueError:
            print('ERRO: Use o teclado numérico para escolher apenas uma das jogadas citadas.')
    return jogada
    
def atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, vezes):
    for i in range(0, vezes):
        informacao_jogadores[qtd_jogadores-1]['Cartas'].append(choice(cartas))
    #return informacao_jogadores[qtd_jogadores-1]['Cartas']

# Função que fará a lógica do Dealer.
def dealer(qtd_jogadores, informacao_jogadores, cartas = criar_cartas()):
    print('\nDealer em ação...\n')
    dealer_ascendente = choice(cartas)
    carta_furo = choice(cartas)
    aposta = 0
    print('Carta do dealer virada para cima: {0}'.format(dealer_ascendente))
    print('REMOVER PRINT NA FINALIZAÇÃO::: carta virada para baixo: {0}'.format(carta_furo))
    # Verificação do modo de funcionamento do dealer (um ou múltiplos jogadores)
    if qtd_jogadores == 1:
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
        print('Apenas 1 jogador')
        # Distribuindo as primeiras cartas
        atribuir_cartas(qtd_jogadores, informacao_jogadores, cartas, 2)
        if informacao_jogadores[qtd_jogadores-1]['Cartas'].count('Ás') == 1 and (informacao_jogadores[qtd_jogadores-1]['Cartas'].count('J') == 1 or informacao_jogadores[qtd_jogadores-1]['Cartas'].count('Q') == 1 or informacao_jogadores[qtd_jogadores-1]['Cartas'].count('K') == 1):
            print('Blackjack!')
            informacao_jogadores[qtd_jogadores-1]['Vitorias'] += 1
        # for i in informacao_jogadores[qtd_jogadores-1]['Cartas']:

    # Pega o próximo jogador
    else:
        print('Mais que 1 jogador')

    # Distribuição de cartas iniciais: 2 para cada jogador, viradas para cima. 2 para o dealer sendo uma para cima e outra para baixo.
    #escuta_jogada()
    return print(qtd_jogadores, '\n\n', informacao_jogadores)

    

def blackjack():
    print('Bem vindo ao Blackjack versão texto!')
    qtd_jogadores = quantidade_de_jogadores()
    informacao_jogadores = atribuir_nomes_aos_jogadores(qtd_jogadores)
    dealer(qtd_jogadores, informacao_jogadores)
blackjack()

