# Falando sobre escopo, dizemos sobre a visibilidade das variáveis. O escopo é o determinante da visibilidade da variável

# Uma variável global:
x = 25

def printer():
    # Uma variável declarada dentro de uma função
    x = 50
    return x

print(x) # Variável global será printada
print(printer()) # A variável dentro da função será printada

# No geral, temos 4 escopos diferentes.
# Local
# Enclosing Functions
# Global
# Built-in
# O Python segue a regra LEGB:
# L: Local - Nomes atribuídos de qualquer forma dentro de uma função (def ou lambda) e declarações não globais nessa função.
# E: Enclosing function locals - Nome no escopo local de todas e quaisquer funções encapsuladas (def ou lambda), de dentro para fora.
# G: Global (módulo) - Nomes atribuídos no nível superior de um arquivo de módulo, ou declarados como global em uma def dentro do arquivo.
# B: Built-in (Python) - Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...

#Exemplos:
f = lambda x: x**2 # x é uma variável local

nome = 'Isso é uma variável global' # Variável global
def cumprimento():
    nome = 'Matheus' # Variável local
    def ola():
        print('Olá ' + nome)
    ola()
cumprimento()


x = 50 # Variável global
def func(x):
    print('x é', x)
    x = 2 # Variável local
    print('x mudou para', x)
func(x)
print('x ainda é', x)

# Também podemos definir uma variável global dentro de uma função ao utilizar o prefixo global antes do nome da variável
def func():
    global x
    print('Essa função agora usa o x global!')
    print('Por causa do x global, x agora é: ', x)
    x = 2
    print('Chamada a função func(), agora o x global mudou para: ', x)
print('Antes de chamar a função func(), o x era: ', x)
func()
print('Valor do x (fora da func()) é: ', x)

# Por fim, podemos usar as funções globals() e locals() para verificar as variáveis globais e locais
globals()
locals()