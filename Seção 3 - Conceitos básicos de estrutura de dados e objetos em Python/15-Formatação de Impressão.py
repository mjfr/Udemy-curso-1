a = 1111
b = 'String teste'

# %s serve como uma 'marca' que dita uma substituição por um elemento externo que será convertido em string. Ao final deve ser passado entre parênteses qual a string que sera substituída.
print('Isso é uma %s auxiliar.' %(a))

# %X.Yf onde Y é um número inteiro que representa a quantidade de casas pós ponto é outro método de formatação utilizado para inserir números flutuantes em strings.
# No caso de X ser maior que a quantidade de dígitos disponíveis, o restante será preenchido com zeros.
# X é um número inteiro cuja quantidade será utilizada para preencher frente ao ponto flutuante
print('Printando pontos flutuantes: %1.3f' %(876.54321))

# É possível utilizar em uma mesma string a mesma 'marca' para substituir diferentes valores
print('Essa %s aqui, e este número %s aqui foram substituídos.' %(b, a))

# Métodos imbutidos em strings
# Ao utilizarmos do método .format(), estamos criando um dicionário, algo que será visto na aula 19-Dictionaries
a1 = 'One: {a}, Two: {b}, Three: {c}'.format(a=1, b = 'dois', c=12.34)
a1


# Site recomendação sobre formatação em Python
# https://pyformat.info/

# Como visto no site, certas maneiras de formatar uma string como %s, %d foram substituídas por chaves com índices.
print('O novo método troca o \%s por {0} com o cuidado de adicionar índices nas {1}'.format('"Chave, índice, chave"', 'posições corretas'))