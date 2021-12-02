# Namedtuples criam "classes" com a diferença que elas são indexadas, logo podemos acessar essas "classes" através de índices, assim como acessaríamos uma tupla normal
# No caso são tuplas que nos permitem acessar atributos através de índices.
from collections import namedtuple

# Criamos uma namedtuple chamada Dog, primeiramente passamos o nome da namedtuple depois passamos todos os parâmetros que queremos que ela tenha separados por espaço
Dog = namedtuple('Dog', 'age breed name')

cachorro1 = Dog(age=2, breed='Vira latas', name='Caramelo')
cachorro1

cachorro1[2] # Retorna o nome