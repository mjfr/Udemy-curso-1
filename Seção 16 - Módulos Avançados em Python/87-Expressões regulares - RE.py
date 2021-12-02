# Nos permite encontrar padrões de textos
import re

padroes = ['termo1', 'termo_intruso', 'termo2']

texto = 'Essa é uma string com o termo1. Essa é outra string agora com o termo2.'
re.search(padroes[0], texto) # Não podemos trabalhar com listas nas expressões regulares. Nos retorna um objeto com uma tupla que indica o índice inicial e final do padrão encontrado e por fim o padrão encontrado.

for padrao in padroes:
    print('Procurando por {0} em: \n{1}'.format(padrao, texto))

    if re.search(padrao, texto):
        print('\nDeu match\n')
    else:
        print('\nNão deu match\n')

# Sintaxe de repetição
# Um padrão seguido por um metacaractere * é repetido zero ou mais vezes.
# Substitua o * por + e o padrão deve aparecer pelo menos uma vez.
# Usar ? significa que o padrão aparece zero ou uma vez.
# Para um número específico de ocorrências, use {m} após o padrão, onde me é substituído pelo número de vezes que o padrão deve repetir.
# Use {m, n} onde m é o número mínimo de repetições e n é o máximo

frase_teste = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
padroes_teste = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}'] # 1º s seguido de zero ou mais d's ; 2º s seguido de um ou mais d's ; 3º s seguido por zero ou um d ; 4º s seguido por três d's ;  5º s seguido de dois a três d's

def multi_re_find(patterns,phrase):
    '''
    Toma uma lista de padrões regex
    Imprime uma lista de todas as partidas
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')

multi_re_find(padroes_teste, frase_teste)

# Conjuntos de caracteres são usados para combinar qualquer grupo de caracteres na entrada. São utilizados os colchetes para contruir as entradas.
padroes_teste2 = ['[sd]', 's[sd]+'] # 1º s ou d ; 2º s seguido de um ou mias s ou d's
multi_re_find(padroes_teste2, frase_teste)

# Exclusão. Utiliza-se ^para excluir termos incorporados nos colchetes
re.findall('[^!.? ]+', frase_teste)

# Intervalo de caracteres
frase_teste2 = 'Essa frase é uma frase de exemplo, vamos ver se encontramos algumas letras'
padroes_teste3 = ['[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+'] # 1º sequência de letras minúsculas ; 2º sequências de letras maiúsculas ; 3º sequências de letras maiúsculas ou minúsculas ; 4º uma letra maiúscula seguida de lestras minúsculas
multi_re_find(padroes_teste3, frase_teste2)