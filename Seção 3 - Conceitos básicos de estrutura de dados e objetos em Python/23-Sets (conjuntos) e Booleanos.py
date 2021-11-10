# Sets são conjuntos de dados que permitem valores únicos, diferente de listas, dicionários e tuplas
# Sets podem ser criados vazios para posteriormente adicionar valores
x = set()

# Métodos imbutidos no set
# O método add() adiciona valores no set. Valores repetidos são ignorados, logo, aparecem apenas uma vez no set
x.add(1)
x.add(1)
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x

# Listas se encapsuladas por sets, também não apresentarão valores repetidos.
y = set([1, 1, 1, 2, 3, 3, 4, 4])
y
# Seus retornos além de únicos são postos entre chaves.

# Booleanos são em essência, verdadeiro ou falso
a = True
b = False

# Em comparações, é retornado um valor booleano.
1 <= 2
1 >= 2

# Recursos extras para mais prática básica
#Prática básica:
#http://codingbat.com/python

#Mais prática matemática (e mais difícil):
#https://projecteuler.net/archives

#Lista de problemas práticos:
#http://www.codeabbey.com/index/task_list

#Um SubReddit dedicado a problemas de prática diária:
#https://www.reddit.com/r/dailyprogrammer

#Um site muito complicado com muito poucas dicas e problemas (Não para iniciantes, mas ainda interessantes)
#http://www.pythonchallenge.com/