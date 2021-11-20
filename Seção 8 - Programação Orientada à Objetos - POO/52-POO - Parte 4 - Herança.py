# Herança permite que reutilizemos classes. (Classes futuras herdando métodos e parâmetros de classes anteriores)

class Animal(object):
    def __init__(self):
        print('Animal Criado')
    
    def quemSouEu(self):
        print('Eu sou um animal')
    
    def comer(self):
        print('Comendo...')

animal1 = Animal()
animal1.quemSouEu()
animal1.comer()

# Quando fazendos uma classe herdar a outra, passamos como parâmetro qual a classe que será herdada.
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado')

    def quemSouEu(self):
        print('Sou um cachorro')

    def latir(self):
        print('Au au')

caramelo = Cachorro()

# Ao chamarmos um método que também existe na classe do qual foi herdado, ele sobrescreve o método e utiliza o da classe que recebe a herança
caramelo.quemSouEu()
caramelo.latir()

# Método herdado
caramelo.comer()