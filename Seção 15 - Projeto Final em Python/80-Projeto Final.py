# Projeto final, foram passadas 100 ideias sobre o que fazer como projeto final.
# Este projeto é progressivo, a medida em que novos conhecimentos forem agregados e um lampejo de inspiração surgir, deve prosseguir.
# Inicialmente, penso em fazer um código sobre cada tema, embora é provável que não faça todos os temas.

'''
WIP - Início 02/12/2021
'''

# 1 Números
# Encontre o PI de "n" casas decimais. ** - Insira um número e faça com que o programa gere o PI até "n' casas decimais. Mantenha um limite para o quão longe o programa irá.

from math import pi
def casas_pi():
    '''
    Função que pergunta ao usuário quantas casas decimais ele quer que apareçam no Pi. Retorna uma string contendo Pi com X casas decimais
    '''
    while True:
        try:
            casas_decimais = input('Quantas casas decimais você quer que apareçam no Pi? ')
            resultado = 'Pi é: {:1.{casas}f}'.format(pi, casas = casas_decimais)
            break
        except ValueError:
            print('Você deve inserir somente números positivos e inteiros')
    return print(resultado)

casas_pi()


# 2 Algoritmos Clássicos
# Conjectura Collatz ** - Comece com um número *n> 1*. Encontre o número de etapas necessárias para chegar a 1 usando o seguinte processo: Se *n* for par, divida por 2. Se *n* for ímpar, multiplique por 3 e adicione 1.

def conjectura_collatz():
    while True:
        try:
            numero = int(input('Conjectura de Collatz. \nDigite um número maior que 1 e o mesmo será reduzido até 1. \nNúmero: '))
            break
        except ValueError:
            print('Digite apenas números inteiros, positivos e maiores que 1')
    while numero > 1:
        if numero % 2 == 0:
            print('{0} ÷ 2'.format(numero))
            numero /= 2
        elif numero % 2 != 0:
            print('({0} x 3) + 1'.format(numero))
            numero = (numero*3) + 1
    return 'O resultado é: {0}'.format(numero)

conjectura_collatz()


# 3 Grafos
# Caminho Euleriano ** - Crie um programa que terá como entrada um grafo e produza um caminho Euleriano ou um ciclo Euleriano, ou declare que isto não é possível. Um Caminho Euleriano inicia em um nó e percorre todas as arestas de um gráfico em cada nó e termina em outro nó. Um ciclo Euleriano é um caminho euleriano que inicia e termina no mesmo nó.

def caminho_euleriano():
    pass

# 4 Texto

