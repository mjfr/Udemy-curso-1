# For é uma estrutura de controle de fluxo, um loop.
# Atua como iterador (objeto que percorre uma sequência de objetos)

# Formato geral:
# for (item) in (objeto):
#   Faz algo

lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)


for num in lista:
    print(num)

# Identificação de números pares e ímpares em laço for
for num in lista:
    if num % 2 == 0:
        print('É par')
    else:
        print('É impar')

# Somando todos os itens de uma lista usando laço for
sum_ = 0
for num in lista:
    sum_ += num
print(sum_)

# Printando caracteres separados de uma string usando laço for
lista_letra = 'Uma string usada no laço for'
for letra in lista_letra:
    print(letra)

# Iterando sobre tuplas usando laço for
tup = (1, 2, 3, 4, 5)
for t in tup:
    print(t)

# Peculiaridade de tuplas: Desembalamento de tuplas
tup2 = [(1, 2), (2, 3), (3, 4)]
# "Desembalado" a Tupla tup2 nas variáveis tup2_desembalado1 e tup2_desembalado2
(tup2_desembalado1, tup2_desembalado2) = tup2[0]

# "Desembalando" uma tupla utilizando um laço for
for (tup2_desembalado1, tup2_desembalado2) in tup2:
    print("1º desembalado:{0} & 2º desembalado:{1}".format(tup2_desembalado1, tup2_desembalado2))

# Iteração em dicionários:
dic = {'k1': 1, 'k2': 2, 'k3': 3}

# Retornando chaves utilizando laço for
for chave in dic:
    print(chave)

# Retornando tuplas das chaves e valores utilizando laço for
for valor in dic.items():
    print(valor)

# Retornando chave e valor utilizando laço for e desembalagem de tuplas
for (chave, valor) in dic.items():
    print(chave, ':', valor)