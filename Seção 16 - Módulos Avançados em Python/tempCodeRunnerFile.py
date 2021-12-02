# Um debugger nos permite percorrer o programa para encontrar falhas.
import pdb

x = [1, 2, 3]
y = 2
z = 3

result = z + y
print(result)

pdb.set_trace()

result2 = x + result # Resulta em erro, neste caso não podemos concatenar lista com int. Adicionamos acima um pdb.set_trace() para parar nesta linha e logo em seguida no terminal teremos acesso de escrita para verificar possíveis variáveis
# Ao digitar 'c' estamos dando o comando de continuar para o pdb
# Por exemplo, sabemos que x é uma lista e não seria concatenada com um int, logo, no pdb podemos mudar x para uma int e aí verificamos se o erro persiste ou se foi arrumado
print(result2)