# O filter() permite que filtremos todos os elementos de um iterável que retornaram positivo.
lista = [1, 4, 5, 12, 19, 21, 22, 23]

# Como seria um filter sem o método
lst = []
for i in lista:
    if i % 2 == 0:
        lst += [i]
print(lst)

# Faz a mesma coisa que o bloco de código acima
# Foi convertido em lista, assim como o map pois retorna endereço de memória caso contrário
list(filter(lambda x: x%2 == 0, lista))