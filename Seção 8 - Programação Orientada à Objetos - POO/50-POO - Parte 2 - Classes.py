# Para definirmos uma classe, devemos seguir a convenção de começar seu nome em caixa alta.
# O formato geral de uma classe é:
# class NomeDaClasse(object):
#   Conteúdo da classe

class ClasseTeste(object):
    pass

# Aqui estamos instanciando a classe Sample.
# Instanciar significa criar um objeto com o tipo da classe usada.
x = ClasseTeste()
type(x)

# Criando a classe Dog
class Dog(object):
    # No Python, ao criar uma instância de uma classe, ele sempre procura pela função interna da classe obrigatoriamente chamada de __init__
    # __init__ é uma função que também pode ser chamada de construtor
    # O Python pede por padrão um parâmetro chamado self que é o que indica que estamos nos referenciando a esta classe criada
    def __init__(self, raca):
        # Aqui estamos dizendo que a variável raca pertence a classe Dog (self é basicamente o this para outras linguagens)
        # Estamos acessando um atributo interno da classe
        # Em termos gerais: raca é igual a raca e self.raca é igual ao parâmetro interno da classe
        self.raca = raca

# Instanciamos a classe Dog em caramelo
caramelo = Dog(raca='Vira lata')

# Podemos utilizar o ponto para acessar atributos internos da classe
caramelo.raca

pluto = Dog(raca='Bloodhound')
pluto.raca

# Recriando a classe Dog
class Dog(object):
    # Aqui estamos criando uma variável interna da classe Dog, logo, não precisamos referenciar ela com o self
    especie = 'Mamífero'

    def __init__(self, raca):
        self.raca = raca
        # Também podemos trabalhar dentro do __init__ como trabalharíamos em uma função qualquer
        # Neste caso, usamos self.especie pois o construtor não sabe o que é especie, logo, referenciamos como uma variável interna de Dog
        self.qtd_caracteres_raca = len(self.especie)
        print('Print de dentro da classe Dog no construtor')

trovao = Dog(raca='Rottweiler')
trovao.raca
trovao.especie
trovao.qtd_caracteres_raca