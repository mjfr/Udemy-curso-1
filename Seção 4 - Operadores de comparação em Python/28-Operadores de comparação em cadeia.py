a = 1
b = 2
c = 1

# Operadores de comparação em cadeia: 'and' e 'or' agregam múltiplas comparações e retorna um único booleano
# Operador 'and' ambos os lados da comparação DEVEM resultar em verdadeiro para que o resultado seja verdadeiro
a == 1 and c == 1 #Verdadeiro
a == 1 and c == b #Falso

# Operador 'or' não há necessidade de ambos os lados apresentarem resultados verdadeiros. Basta um lado apresentar um resultado verdadeiro (mesmo o outro sendo falso [prolixo]) que o resultado será verdadeiro
a == 1 or b == 94994949494949 #Verdadeiro
a == 5 or c == b #Falso

# Combinação de operadores
(a == 1 or b == 5) and c == a #Verdadeiro
(a == c or b == 2) and c == b #Falso