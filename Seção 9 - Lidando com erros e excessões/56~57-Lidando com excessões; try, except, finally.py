# O try é o bloco de código no qual achamos ou sabemos que poderá resultar em um erro, logo, tentaremos executar o código
try:
    file = open('testfile', 'w')
    file.write('Testando') # Como é possível escrever
# O except é onde deixamos o erro gerado, executando um bloco de código para tratar o erro.
except IOError: # Não é necessário especificar o erro, independende de especificar ou não, quando houver erros o código passará pelo except
    print('Erro ao tratar arquivo.')
# Se não houver erros, o bloco de código executado será outro
else:
    print('Não houve erro.')

# Neste bloco de try e finally, o código sempre executará o finally, independente de erros ou sucessos. Também, ao executar este bloco, vemos que há uma excessão aparecendo no terminal.
#  Ela aparece pois estamos tentando ESCREVER em um arquivo apenas para LEITURA e não tratamos com o bloco except.
try:
    f = open('testfile', 'r')
    f.write('Teste novamente')
finally:
    print('Sempre será executado')