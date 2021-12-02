# Geradores são iteradores assim como listas, porém não são pré carregados na memória de uma vez só.
# Geradores são criados como funções, porém usam yield ao invés de return


# Diferentemente do gerador, essa função carrega na memória a lista
def cubes(n):
    lst = []
    for num in range(n):
        lst+=[num**3]
        return lst
        
# A lista é criada antes de realizar o print
for x in cubes(10):
    print(x)


# Agora no gerador, não há listas na memória
def gencubes2(n):
    for num in range(n):
        yield num ** 3

# Toda vez que o gerador é chamado ele gera o resultado e "dá uma pausa". Assim que chamado novamente, ele retorna de onde parou
for x in gencubes2(10):
    print(x)


def fib(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output += [a]
        a, b = b, a+b
    return output

fib(10)


# Diferentemente do return de uma função que encerra o código no momento em que ele é lido, o yield retorna o valor mas não necessariamente encerra o código
# Também, como dito acima, o gerador retorna de onde parou, logo, não atribuirá a = 1 e b = 1 novamente.
def genfib2(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in genfib2(10):
    print(num)

# Agora ele é solicitado a ser carregado na memória para ser convertido em lista
list(genfib2(10))


# Iteradores e geradores possuem um método específico next() que acessa o próximo valor de onde o gerador / iterável parou
g = genfib2(5)
next(g)

# O método iter() transforma sequências em iteraveis. Ex.:
s = 'Hello'
for char in s:
    print(char)

# A string não é iterável, porém podemos transformar a mesma em um iterável

s_iter = iter(s)
next(s_iter)