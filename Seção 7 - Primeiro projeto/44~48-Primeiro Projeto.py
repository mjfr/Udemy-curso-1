import os
# Um jogo da velha deve possuir:
# - Tabuleiro
#       Nove espaços em forma de #
#       Deve atualizar a cada jogada
# - 2 jogadores
#       Cada jogador terá sua vez
#       Cada jogador possui um símbolo (X / O)
#       O jogador deve poder escolher a posição para colocar o seu símbolo, dada a disponibilidade do tabuleiro

lista_tabuleiro_superior = ['__', '__', '__']
lista_tabuleiro_meio = ['__', '__', '__']
lista_tabuleiro_inferior = ['__', '__', '__']

# Define um tabuleiro:
def tabuleiro():
    tabuleiro.lista_tabuleiro_superior = lista_tabuleiro_superior
    tabuleiro.lista_tabuleiro_meio = lista_tabuleiro_meio
    tabuleiro.lista_tabuleiro_inferior = lista_tabuleiro_inferior
    return [tabuleiro.lista_tabuleiro_superior, tabuleiro.lista_tabuleiro_meio, tabuleiro.lista_tabuleiro_inferior]



# Definir os jogadores:
def gera_jogadores():
    '''
    Função para escolher qual jogador ficará com qual símbolo
    '''
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
    gera_jogadores.jogadores = dict_jogadores
    gera_jogadores.jogador1 = gera_jogadores.jogadores['Jogador 1']
    gera_jogadores.jogador2 = gera_jogadores.jogadores['Jogador 2']
    return dict_jogadores



# Verificar o tabuleiro:
def resposta_reinicio():
    def resposta_input():
        return str(input('Gostaria de reiniciar o jogo? (sim / nao)'))
    # Resposta para confirmar ou negar o reinício
    sim_nao = True
    while sim_nao:
        resp = resposta_input()
        if resp == 'sim':
            resposta_bool = True
            sim_nao = False
        elif resp == 'nao':
            resposta_bool = False
            sim_nao = False
            break
        else:
            print('Responda apenas com (sim / nao)')
    reiniciar(resposta_bool)



def verificar_tabuleiro():
    # 2 ifs para a primeira fileira (1, 2, 3)
    if tabuleiro()[0].count(gera_jogadores.jogadores['Jogador 1']) == 3 and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[0].count(gera_jogadores.jogadores['Jogador 2']) == 3 and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a segunda fileira (4, 5, 6)
    if tabuleiro()[1].count(gera_jogadores.jogadores['Jogador 1']) == 3 and tabuleiro()[1][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[1].count(gera_jogadores.jogadores['Jogador 2']) == 3 and tabuleiro()[1][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a terceira fileira (7, 8, 9)
    if tabuleiro()[2].count(gera_jogadores.jogadores['Jogador 1']) == 3 and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[2].count(gera_jogadores.jogadores['Jogador 2']) == 3 and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a primeira coluna (1, 4, 7)
    if tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[1][0] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[1][0] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a segunda coluna (2, 5, 8)
    if tabuleiro()[0][1] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[2][1] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[0][1] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[0][1] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[2][1] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[0][1] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a terceira coluna (3, 6, 9)
    if tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[1][2] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[2][2] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[1][2] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[2][2] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a primeira diagonal (1, 5, 9)
    if tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[2][2] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[2][2] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[0][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    # 2 ifs para a segunda diagonal (7, 5, 3)
    if tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 1'] and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 1']:
        print('Parabéns Jogador 1, você ganhou')
        resposta_reinicio()
    if tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[1][1] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[0][2] == gera_jogadores.jogadores['Jogador 2'] and tabuleiro()[2][0] == gera_jogadores.jogadores['Jogador 2']:
        print('Parabéns Jogador 2, você ganhou')
        resposta_reinicio()
    if (tabuleiro()[0].count(gera_jogadores.jogadores['Jogador 2']) + tabuleiro()[0].count(gera_jogadores.jogadores['Jogador 1']) == 3) and (tabuleiro()[1].count(gera_jogadores.jogadores['Jogador 2']) + tabuleiro()[1].count(gera_jogadores.jogadores['Jogador 1']) == 3) and (tabuleiro()[2].count(gera_jogadores.jogadores['Jogador 2']) + tabuleiro()[2].count(gera_jogadores.jogadores['Jogador 1']) == 3):
        print('Booooo!!!!! Deu velha!')
        resposta_reinicio()



# Desenhar tabuleiro:
def desenhar_tabuleiro(vez):
    print('', tabuleiro.lista_tabuleiro_superior, '\n', tabuleiro.lista_tabuleiro_meio, '\n', tabuleiro.lista_tabuleiro_inferior)
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
    condicional2 = True
    while condicional2:
        if 1 <= int(posicao) <= 3:
            if tabuleiro.lista_tabuleiro_superior[int(posicao)-1] != 'X' and tabuleiro.lista_tabuleiro_superior[int(posicao)-1] != 'O':
                tabuleiro.lista_tabuleiro_superior[int(posicao)-1] = vez
                condicional2 = False
                # return tabuleiro.lista_tabuleiro_superior, tabuleiro.lista_tabuleiro_meio, tabuleiro.lista_tabuleiro_inferior
            else:
                print('Você escolheu uma posição invalida ou ocupada.')
                posicao = posicao_input()
        elif 4 <= int(posicao) <= 6:
            if tabuleiro.lista_tabuleiro_meio[int(posicao)-4] != 'X' and tabuleiro.lista_tabuleiro_meio[int(posicao)-4] != 'O':
                tabuleiro.lista_tabuleiro_meio[int(posicao)-4] = vez
                condicional2 = False
                # return tabuleiro.lista_tabuleiro_superior, tabuleiro.lista_tabuleiro_meio, tabuleiro.lista_tabuleiro_inferior
            else:
                print('Você escolheu uma posição invalida ou ocupada.')
                posicao = posicao_input()
        elif 7 <= int(posicao) <= 9:
            if tabuleiro.lista_tabuleiro_inferior[int(posicao)-7] != 'X' and tabuleiro.lista_tabuleiro_inferior[int(posicao)-7] != 'O':
                tabuleiro.lista_tabuleiro_inferior[int(posicao)-7] = vez
                condicional2 = False
                # return tabuleiro.lista_tabuleiro_superior, tabuleiro.lista_tabuleiro_meio, tabuleiro.lista_tabuleiro_inferior
            else:
                print('Você escolheu uma posição invalida ou ocupada.')
                posicao = posicao_input()
    print('', tabuleiro.lista_tabuleiro_superior, '\n', tabuleiro.lista_tabuleiro_meio, '\n', tabuleiro.lista_tabuleiro_inferior)



# Jogar
def iniciar():
    gera_jogadores()
    for i in range(0, 9):
        if i%2==0:
            vez = gera_jogadores.jogador1
            verificar_tabuleiro()
            desenhar_tabuleiro(vez)
            os.system('cls')
        else:
            vez = gera_jogadores.jogador2
            verificar_tabuleiro()
            desenhar_tabuleiro(vez)
            os.system('cls')
            


def reiniciar(decisao : bool):
    if decisao == False:
        print('Obrigado por jogar!')
        quit()
    else:
        print('\n Jogo passado \n', '', tabuleiro.lista_tabuleiro_superior, '\n', tabuleiro.lista_tabuleiro_meio, '\n', tabuleiro.lista_tabuleiro_inferior)
        global lista_tabuleiro_superior
        global lista_tabuleiro_meio
        global lista_tabuleiro_inferior
        lista_tabuleiro_superior = ['__', '__', '__']
        lista_tabuleiro_meio = ['__', '__', '__']
        lista_tabuleiro_inferior = ['__', '__', '__']
        iniciar()
        
iniciar()