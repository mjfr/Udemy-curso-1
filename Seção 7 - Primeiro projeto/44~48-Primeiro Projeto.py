# Um jogo da velha deve possuir:
# - Tabuleiro
#       Nove espaços em forma de #
#       Deve atualizar a cada jogada
# - 2 jogadores
#       Cada jogador terá sua vez
#       Cada jogador possui um símbolo (X / O)
#       O jogador deve poder escolher a posição para colocar o seu símbolo, dada a disponibilidade do tabuleiro

# Definir um tabuleiro:
lista_tabuleiro_superior = [x for x in range(1, 4)]
lista_tabuleiro_meio = [x for x in range(4, 7)]
lista_tabuleiro_inferior = [x for x in range(7, 10)]

def tabuleiro():
    #return ('', lista_tabuleiro_superior,'\n', lista_tabuleiro_meio, '\n', lista_tabuleiro_inferior)
    return  [lista_tabuleiro_superior, lista_tabuleiro_meio, lista_tabuleiro_inferior]
tabuleiro()

# Desenhar tabuleiro:
def desenhar_tabuleiro():
    tabuleiro()
    # Adicionar símbolo ao tabuleiro:
    def posicao_input():
        return str(input('Escolha a posição que marcará:'))
    condicional = True
    while condicional:
        posicao = posicao_input()
        if (posicao.isdigit() and 1 <= int(posicao) <= 9):
            condicional = False
        else:
            print('Escolha apenas os números inteiros que aparecem no tabuleiro! \nTente novamente.')
    print(posicao)
    if 1 <= int(posicao) <= 3:
        tabuleiro()[0][int(posicao)-1] = 'hey'
    # if 4 <= int(posicao) <= 6:
    #     print(tabuleiro()[0][int(posicao)])
    # if 7 <= int(posicao) <= 9:
    #     print(tabuleiro()[0][int(posicao)])

desenhar_tabuleiro()

# Definir os jogadores:
def gera_jogadores():
    '''
    Função para escolher qual jogador ficará com qual símbolo
    '''
    # Função interna para pegar o input do símbolo que o usuário escolheu
    #def jogador_input():
    #    return input('Escolha quem será o primeiro a jogar: (O / X)').upper()
    # Criação do dicionário para armazenar o jogador e seu símbolo
    dict_jogadores = {'Jogador 1' : '', 'Jogador 2' : ''}
    # Enquanto o jogador não escolher X ou O, ele não pode prosseguir.
    condicional = True
    while condicional:
        dict_jogadores['Jogador 1'] = input('Escolha quem será o primeiro a jogar: (O / X)').upper()
        if (dict_jogadores['Jogador 1'] == 'O' or dict_jogadores['Jogador 1'] == 'X'):
            condicional = False
        else:
            print('Você deve escolher entre (O / X). \nTente novamente.')
    # Bloco condicional para definir o símbolo do segundo jogador
    if dict_jogadores['Jogador 1'] == 'O':
        dict_jogadores['Jogador 2'] = 'X'
    else:
        dict_jogadores['Jogador 2'] = 'O'
    # Retorna um dicionário com as chaves sendo os jogadores e os valores seus símbolos
    return dict_jogadores

jogadores = gera_jogadores()


# Vez do jogador
def vez_do_jogador():
    vez = jogadores['Jogador 1']
    if 'X' == jogadores['Jogador 1']:
        print('Vez do jogador 1')
    else:
        print('Vez do jogador 2')
    # print('Vez do')

# Verificar o tabuleiro:
def verificar_tabuleiro():
    pass

# Jogar
def iniciar():
    pass