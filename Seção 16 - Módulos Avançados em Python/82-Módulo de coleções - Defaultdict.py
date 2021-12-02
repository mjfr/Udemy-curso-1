# A diferença dele para um dicionário comum é que o defaultdict não retorna erro caso não exista uma chave

from collections import defaultdict
d = {}
d['one'] = 1
d['two']  # Retorna um erro pois o valor não existe

d2 = defaultdict(object) 
d2['one'] = 1 # Retornará a chave 'one' : 1, e logo antes também o objeto que foi passado como parâmetro
d2['two'] # Não retorna erro, retorna um endereço de memória que seria o parâmetro passado no defaultdict (neste caso foi um object)
d2

d3 = defaultdict(lambda : 32)
d3['one'] # Retorna 32 por causa da função lambda passada como parâmetro
d3