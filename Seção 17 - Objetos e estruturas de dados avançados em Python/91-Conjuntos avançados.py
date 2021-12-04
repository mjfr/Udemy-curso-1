# Conjuntos são estruturas de dados que excluem elementos iguais dentro do mesmo.

s = set()

# Método de adição em sets
s.add(1)
s.add(2)

# Método para limpar o set
s.clear()

# Também podemos construir sets utilizando chaves.
s2 = {1, 2, 3, 3, 4, 2}

# Podemos copiar o set utilizando o método .copy()
sc = s2.copy()

# Podemos ver a diferença entre sets
s2.difference(s) # Há a diferença que o s2 possui 3 e 4
s.difference(s2) # Não há diferenças pois s2 possui 1 e 2 que estão presentes em s


# Podemos aplicar o método .difference_update() e fazer com que um set seja apenas a diferença de outro
ss1 = {1, 2, 3}
ss2 = {1, 4, 5}

ss1.difference_update(ss2)
ss1 # O 1 ficou de fora pois ele também está presente no ss2, porém, como 2 e 3 não estão presentes em ss2, eles permancem

# Também podemos descartar itens específicos de um set como:
ss1.discard(3)
ss1

# O método .intersection() nos retorna a interseção entre os dois sets
ss1 = {1, 2, 3}
ss2 = {1, 4, 5}

ss1.intersection(ss2)

# Assim como o difference_update(), podemos utilizar o .intersection_update() para transformar os valores do set apenas em suas interseções
ss1.intersection_update(ss2)
ss1

# O método .union() nos retorna a união entre os dois sets
ss1 = {1, 2, 3}
ss2 = {1, 4, 5}

ss1.union(ss2)