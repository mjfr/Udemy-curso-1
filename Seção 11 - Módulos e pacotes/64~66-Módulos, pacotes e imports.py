# O Python não deixa bibliotécas carregadas por padrão, logo, devemos importar as bibliotecas que iremos usar
# Exemplo: Para fazer uma potência,
5 ** 3

# Importando da biblioteca math:
import math

math.pow(5, 3)

# Importando biblioteca de terceiros: devemos usar no cmd o comando: pip install "NOME DA BIBLIOTECA", com tanto que ela exista no pip
# Nesta seção e aula, como teste foi pedido para importar bibliotecas de terceiros. As bibliotecas importadas foram:
# Numpy
# Pandas
# Tensorflow <--- Tentei porém aparentemente a versão disponível não suporta o Python mais recente


# Importando um módulo que eu criei
# O módulo não era reconhecido se estivesse na mesma pasta ou subpasta do curso, logo, precisou ficar fora para ser reconhecido.

# O módulo importado contém este trecho de código
# Teste de criação do meu próprio módulo no Python
#def helloworld():
#    print('Hello from a module')

import hello
hello.helloworld()


# Se mais que um arquivo for usado para importar módulos, criamos um arquivo vazio chamado __init__.py dentro da pasta cujos módulos estão armazenados
