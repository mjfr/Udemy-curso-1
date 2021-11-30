# map() é um método que recebe dois argumentos, uma função e um iterável e tenta aplicar a função em todos os iteráveis

temp = [9, 0, 22, 30, 90, 120]

def fahrenheit(T):
    return (9/5) * T + 32
    
# Como seria o map sem o método
lista_temp = []
for t in temp:
    lista_temp.append(fahrenheit(t))
print(lista_temp)

# Mesma funcionalidade do trecho de código acima utilizando map(). Não chamamos a função '()', apenas apontamos para qual função que deverá ser usada
# Neste caso, no Python 3, diferente do 2 que já retornaria os valores calculados, devemos colocar em uma lista para evitar receber apenas o endereço de memória do map que fizemos
list(map(fahrenheit, temp))

# Também podemos utilizar uma função lambda, logo não precisariamos criar uma função como na linha 4

list(map(lambda t: (9/5) * t + 32, temp))