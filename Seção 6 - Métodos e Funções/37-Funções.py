# Funções são blocos de construção de código cuja ideia é agrupar instruções semelhantes para reutilizar futuramente
# Para definir uma função, basta usar: def nome_função(parâmetros opcionais):

# Declarando uma função. Executará todo o código dentro dela.
def primeira_funcao():
    print('Olá, mundo!')

# Chamando uma função
primeira_funcao()

l = [1, 2, 3, 4, 5]
# Criando uma descrição para a função: Deve-se colocar três áspas simples ou áspas duplas para descrevê-la.
def funcao_pi():
    '''Printa o número 3.14'''
    print(3.14)
funcao_pi()

# Criando função que recebe argumentos (valores passados para a função que serão trabalhados dentro da mesma)
def somar(num1, num2):
    print(num1 + num2)

# Para chamar a função, devemos passar os argumentos necessários
somar(3, 7)

# Conceito importante: return. O return permite que a função retorne um valor
def multiplicar(num1, num2):
    return num1 * num2

# Podemos atribuir o retorno da função a uma variável
a = multiplicar(8, 8)
a

# Podemos definir funções dentro de funções, porém, essas funções só serão visíveis dentro das funções em que foram declaradas
def primo(num):
    '''
    Checa se um número é primo
    '''

    def divisivel(a, b):
        return a % b

    for n in range(2, num):
        if divisivel(num, n):
            print('Não é primo')
            break
    else:
        print('Primo')
primo(117)