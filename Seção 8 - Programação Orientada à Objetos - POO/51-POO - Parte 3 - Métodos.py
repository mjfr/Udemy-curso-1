# Métodos são funções internas de classes que podem fazer operações com os atributos

class Gato(object):
    especie = 'Mamífero'

    def __init__(self, raca):
        self.raca = raca

    # Criando um método (função dentro de classe). Como é uma função interna de uma classe, devemos passar o parâmetro self
    def miar(self):
        print('Miau!')

beerus = Gato(raca='Persa')
beerus.raca
beerus.miar()

class Circulo(object):
    pi = 3.14

    # Neste construtor estamos passando um parâmetro com valor pré definido. Caso não seja alterado futuramente, este será o valor padrão a ser usado
    def __init__(self, raio = 1):
        self.raio = raio

    def area(self):
        return (self.raio ** 2) * self.pi

    def definir_raio(self, raio):
        self.raio = raio
    
    def obterRaio(self):
        return self.raio

c = Circulo()
c.raio
c.area()

c_raio2 = Circulo(raio=2)
# Também podemos passar o parâmetro sem especificar qual o parâmetro que estamos passando
c_raio2 = Circulo(2)
c_raio2.raio
c_raio2.area()
c_raio2.definir_raio(7)
c_raio2.raio
c_raio2.area()

# Aqui fica evidente uma parte do poder da criação de classes:
# podemos criar diversas variáveis com as mesmas funções e o MESMO potencial de executar instruções, independentes entre si
circulo_pequeno = Circulo(3)
circulo_pequeno.raio
circulo_pequeno.area()
circulo_grande = Circulo(54)
circulo_grande.raio
circulo_grande.area()

# Também podemos salvar as informaçoes em variaveis
raio_circulo_grande = circulo_grande.obterRaio()
raio_circulo_grande