# Método bem relevante para criações de listas pré determinadas
# Contrói uma lista de sequência de números que pode utilizar três parâmetros:
# range(início da lista, fim da lista, intervalo opcional por padrão 1)
range(0, 10) # Cria um objeto gerador (será estudado na Seção 14: Geradores). Funciona como um conjunto de regras na memória porém não inicializados ainda.
serie = range(0, 10) # A variável serie é um objeto gerador, podemos utilizar com o método list para obtermos uma lista
list(serie)

# Criando uma lista com valores de 2 em 2
list(range(0, 100, 2))

# Também utilizando em laços de repetição:
for i in range(0, 100):
    print(i)
    if i > 10:
        break