# O zip() condensa dois iteráveis juntos e devolve uma tupla com a agregação dos dois iteráveis
x = [1, 2, 3]
y = [4, 5, 6]

# Como seria um zip sem o método
def zip_wannabe(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

list(zip_wannabe(x, y))

# Junta as duas listas em uma tupla
list(zip(x, y))



# Encontrando os maiores valores comparando as listas
a = [1, 2, 3, 7, 1, 9, 10]
b = [4, 5, 6, 1, 4, 2, 1]
list(zip(a, b))

# Neste caso, i é uma tupla
for i in zip(a, b):
    print(max(i))



# O zip() pode ser utilizado com iteráveis de comprimentos diferentes, porém devemos ter em mente os valores que podem não aparecer
j = [1, 2, 3, 54]
k = [1, 2]

# Neste caso o zip() irá seguir o comprimento do MENOR iterador
list(zip(j, k))

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
# Neste caso, o zip juntará apenas as chaves
list(zip(d1, d2))
# Aqui ele juntará os valores
list(zip(d1.values(), d2.values()))