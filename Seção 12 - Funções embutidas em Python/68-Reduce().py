# Faz basicamente a mesma coisa do map(). A única diferença é que ele segue fazendo a mesma operação até que o iterável seja reduzido a um único valor
# AULA DESATUALIZADA. REDUCE FOI REMOVIDO NO PYTHON 3, PARA USAR DEVEMOS IMPORTAR DA FUNCTOOLS O REDUCE.
from functools import reduce

lst = [47, 11, 42, 13]

reduce(lambda x,y: x+y, lst)
