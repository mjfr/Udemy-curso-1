# StringIO se comportará de forma semelhante ao file
import io
mensagem = 'Essa é uma string normal'

# A partir daqui, ganhamos basicamente os mesmos acessos que temos ao criar um arquivo
f = io.StringIO(mensagem)
f.seek(0)

f.read()

f.seek(0)

f.write('Segunda linha escrita aqui.')

f.seek(0)

f.read()