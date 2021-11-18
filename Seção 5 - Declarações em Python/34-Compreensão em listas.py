# Formas de criar uma lista:
# 1 - A forma mais imprática
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 2 - Uma forma melhor que a primeira, porém mais extensa
y = []
for i in range (0, 20):
    y += [i]
y

# 3 - Compreensão em lista, uma forma mais prática:
# Dizemos ao Python que queremos criar uma lista cujo valor da lista sempre será a primeira variável. 
z = [j for j in range(0, 20)]
z

# Também podemos realizar operações com os valores da lista
a = [k*2 + 10 for k in range(0, 20)]
a

# Também podemos criar listas com condições
# Método longo:
x1 = []
for i1 in range(0, 20):
    if i1 % 2 == 0:
        x1 += [i1]
x1

# Método com compreensão de lista
y1 = [j1 for j1 in range(0, 20) if j1 % 2 == 0]
y1

# Também podemos utilizar compreensão de listas com strings
lista = [letra for letra in 'word']
lista

# Conversão de temperaturas de Celsius para Fahrenheit utilizando compreensão em listas
celsius = [0, 10, 15, 20, 30, 50, 100]
fahrenheit = [(temperatura * (9/5) + 32) for temperatura in celsius]
fahrenheit