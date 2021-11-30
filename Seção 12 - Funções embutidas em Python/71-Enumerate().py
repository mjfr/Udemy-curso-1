# Permite que contemos elementos enquanto iteramos um objeto. Retorna uma tupla na forma de (contagem, elemento)
lista = ['a', '2', 'b', '5', 'z', '4le', 'y', 34, '62abc', '4']

# Como seria um enumerate sem o método
def enumerate_wannabe(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

list(enumerate_wannabe(lista))



list(enumerate(lista))

# Como o retorno é em tuplas, podemos fazer o tuple unpacking
for number, item in enumerate(lista, 0):
    print(number, ':', item)