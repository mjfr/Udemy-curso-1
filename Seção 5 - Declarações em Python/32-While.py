# O while é mais um laço de repetição que executa instruções desde que sua condição seja verdadeira.

# O formato geral é:
# while (condição):
#   Faz algo
# else:
#   Faz algo

# Devemos tomar cuidado para não fazer um 'while' que nunca tenha sua condição atingida, como por exemplo, esquecer de adicionar +1 ao valor do x (algo que faria uma repetição 'infinita')
x = 1
while x < 10:
    print('O valor de x é:', x)
    x += 1
else:
    print('O valor de x é:', x)

# While com operador de comparação em cadeia
y = 1
while (x < 10 and y < 20):
    print('O valor de x é:', x*y)
    x += 1
    y += 2
else:
    print('O valor de x é:', x*y)

lista = []
z = 0
# Devemos tomar muito cuidado com 'while True' pois while sempre será True. Para contornar isso, podemos inserir um 'break' que interromperá o loop
while True:
    lista += [z]
    z += 1
    if z > 10:
        break
lista

ate = 50
a = 1
# Também temos o 'continue' que permite a desconsideração de código dentro do loop sem que saia do loop (diferente do break)
while a < ate:
    a += 1
    if a % 2 == 1:
        continue
    if a % 2 == 0:
        print (a, 'é par')
