# Strings são um tipo de objeto que armazenam textos
# Pode-se usar áspas simples ou duplas para definir strings
'Texto aleatório'

# Método imbutido para mostrar outputs
print('Texto aleatório')

# Há alguns caracteres especiais que combinados com barras invertidas (espaço não é necessário), alteram a string como:
# \n que pula uma linha
print('Texto\naleatório')
# \t que tabula a palavra
print('Texto\taleatório')

# Como strings são tratadas como sequências, podemos utilizar o método len() para contar quantos caracteres estão presentes (espaços contam)
len('Texto aleatório')

# Indexação (acessar as posições dos elementos)
# Como strings não são mutáveis, não podemos utilizar da indexação para alterar elementos individuais
s = 'Texto aleatório'
# Retorno completo da sequência
s[:]
# Retorno do primeiro elemento
s[0]
# Retorno em intervalo [posição inicial : posição final]
s[3:9]
# Retorno do início até um determinado fim
s[:7]
# É possível realizar a indexação de trás para frente
s[-1]
# Também funciona com intervalos
s[-5:15]
s[-5:-1]
s[10:-3]
# Retorno do início até um determinado fim
s[:-8]

# Indexação com espaçamentos
# Padrão
s[::1]
# Retorna elementos de 2 em 2
s[::2]
# É possível inverter a sequência tornando o intervalo negativo
s[::-1]

# Strings são concatenáveis, ou seja, aceitam adições de outras strings
s + ' Teste'
# Também pode-se redefinir a string apenas adicionando uma string nova
s = s + ' Teste'
s
# Strings permitem multiplicação de seus elementos
s * 3

# Strings são objetos que possuem funções específicas
# Funções essas como:
# lower() para deixar todos os caracteres em caixa baixa
s.lower()
# split() divide a string em uma lista, por padrão divide sempre nos espaços
s.split()
# Também é possível passar um elemento que será utilizado como modelo para separar a string:
'Teste, testando o teste, Teste? Sim, teste!'.split(',')