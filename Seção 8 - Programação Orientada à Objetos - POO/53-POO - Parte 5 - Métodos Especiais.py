# Métodos especiais são métodos que podemos definir dentro da classe e permitirão a classe ter comportamentos diferentes quando a classe for utilizada junto com métodos imbutidos do Python como print(), len() etc.

class Livro(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
livro1 = Livro('Um título aqui', 'Matheus', 423)

# Desta forma, recebemos o tipo de objeto (Livro) e a seu endereço na memória
print(livro1)

# Refazendo a classe livro, agora ela possui métodos especiais
class Livro2(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método especial, neste caso, sempre que printarmos a instância de Livro2, este será o retorno (ao invés do tipo de objeto e endereço de memória)
    def __str__(self):
        return 'Título: {0}\nAutor: {1}\nPáginas: {2}'.format(self.titulo, self.autor, self.paginas)

    # Método especial que retorna o tamanho do livro
    def __len__(self):
        return self.paginas

    # Método especial que fará uma ação quando 'del' for utilizado
    def __del__(self):
        print('Livro destruído')

livro2 = Livro2('Outro título aqui', 'Matheus José', 721)

print(livro2)
livro2.__len__()
del livro2