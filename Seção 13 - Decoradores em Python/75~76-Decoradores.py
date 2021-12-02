# Decoradores são funções que alteram o comportamento de outras funções

s = 'Variável Global'

def func():
    a = 1
    return locals()
func()

globals()['s']


def hello(nome='Matheus'):
    return 'Olá, '+ nome
hello()

boasvindas = hello # Após atribuir a função ao boasvindas, boasvindas não tem mais relações com o hello
# logo é possível deletar o hello
del(hello)
boasvindas()

# Função dentro de função
def hello2(nome='Matheus'):
    print('Olá, ' + nome)

    def tudobem():
        print('Tudo bem?')

    def comovoceesta():
        print('Como você está?')

    print(locals())

hello2() # Como tudobem() e comovoceesta() estão dentro da função hello2, são locais

# Função dentro de função 2. Também podemos retornar funções dentro de função
def hello3(nome='Matheus'):
    print('Olá, ' + nome)

    def tudobem():
        print('Tudo bem?')

    def comovoceesta():
        print('Como você está?')

    if nome == 'Matheus':
        return tudobem
    else:
        return comovoceesta

hello3() # Como tudobem() e comovoceesta() estão dentro da função hello2, são locais

func = hello3()
func()

# Funções também podem ser usadas como argumentos de outras funções

def hello4():
    print('Olá!')

def outra(func):
    print('Outra função aqui dentro')
    func()

outra(hello4)

def novo_decorador(func):
    def funcao_interna():
        print('Código executado antes da função')
        func()
        print('Código executado depois da função')
        
    return funcao_interna

def precisa_decorar():
    print('Essa função precisa de decorador')

novo_decorador(hello4)()

precisa_decorar = novo_decorador(precisa_decorar)
precisa_decorar()

# Agora podemos utilizar a anotação @
# Ao colocar a notação, o Python entende que isso é um decorador, sendo uma função que é recebida como input e devolve a função abaixo alterada
# Logo, não precisamos declarar a função em cima e atribuir a mesma a uma variável.
@novo_decorador
def precisa_decorar():
    print('Essa função precisa de decorador!')

precisa_decorar()

# Exemplo de decorador do Programiz: https://www.programiz.com/python-programming/decorator
def smart_divide(func):
    def inner(a, b):
        print('Dividing', a, 'by', b)
        if b == 0:
            print('Cannot divide by 0!')
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

value1 = divide(15, 3)
print(value1)

value2 = divide(5, 0)
print(value2)