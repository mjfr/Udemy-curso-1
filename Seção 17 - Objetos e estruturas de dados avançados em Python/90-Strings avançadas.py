s = 'hello world'

# capitalize() transforma apenas a PRIMEIRA letra de qualquer string em caixa alta ** não altera a string. Para isso, precisaríamos redefinir a string
s.capitalize()

# upper() transforma toda a string em caixa alta ** não altera a string. Para isso, precisaríamos redefinir a string
s.upper()

# lower() transforma toda a string em caixa baixa ** não altera a string. Para isso, precisaríamos redefinir a string
s.lower()

# podemos fazer contagens e localizações com a string
s.count('o') # Realiza a contagem de quantas letras 'o' há na string
s.find('o') # Localiza a primeira ocorrência da letra 'o' na string

# podemos definir um tamanho para a string centrando o conteúdo dela enquanto adicionamos letras, palavras, números ou símbolos na string ** não altera a string. Para isso, precisaríamos redefinir a string
s.center(20, 'z')

# temos métodos de verificação como isalnum() que retorna True caso todos os caracteres de uma string forem alfanuméricos (sem símbolos)
s.isalnum()
s2 = '#heLLo world'
s2.isalnum()

# podemos perguntar também se todos são alfabéticos com .isalpha()
s.isalpha()
s2.isalpha()

# podemos verificar se TODOS os caracteres estão em caixa baixa ou caixa alta com .islower() e .isupper()
s2.islower()
s2.isupper()

# verifica se a string termina com... .endswith()
s.endswith('o')

# .split() quebra a string em uma lista através do parâmetro passado (separa a string retirando o parâmetro) ** não altera a string. Para isso, precisaríamos redefinir a string
s.split('l')

# .partition() semelhante ao .split() com a diferença que ele não deixa o parâmetro de fora ** não altera a string. Para isso, precisaríamos redefinir a string
s.partition('l')