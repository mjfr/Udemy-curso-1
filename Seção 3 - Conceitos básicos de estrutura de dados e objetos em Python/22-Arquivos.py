# Abre um arquivo no caminho especificado
my_file = open('Udemy curso #1/Seção 3 - Conceitos básicos de estrutura de dados e objetos em Python/texto.txt')
my_file

# O método .read() lê o arquivo do começo ao fim
my_file.read()

# O método .readline() lê o arquivo até o fim da linha. Neste caso, ele age como um cursor cuja posição não reinicia sem o método .seek(0) que leva este 'cursor' ao início do arquivo
my_file.readline()
my_file.seek(0)
# Cada vez que o método .readline() é executado, o cursor avança e mantém a posição, até que o método .seek(X) seja ujtilizado
my_file.readline()

# O arquivo sendo iterável, podemos usar um laço de repetição para iterar o mesmo
my_file.seek(0)
for linha in my_file: print(linha)