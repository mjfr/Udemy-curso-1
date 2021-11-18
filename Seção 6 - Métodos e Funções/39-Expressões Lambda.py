# Expressões lambda são ferramentas úteis que são funções definidas em apenas uma linha e possuem existência temporária (só existem naquela linha em que foi declarada)

# Função normal
def quadrado(num):
    return num * num
quadrado(9)

# Função lambda. Como é temporária, e logo após o final da linha ela deixa de existir, não precisa de nome
# Se apenas declarada sem atribuir a uma variável, um objeto do tipo lambda é retornado. Ao atribuir a uma variável, podemos utilizar como uma função normal.
# Sua forma geral é: lambda parâmetro: Faz algo
quadrado_lambda = lambda num: num ** 2
quadrado_lambda(16)

par = lambda x: x % 2 == 0
par(2)

primeiro_char = lambda s: s[0]
primeiro_char('Olá, mundo!')

inverte_string = lambda s: s[::-1]
inverte_string('suehtaM')