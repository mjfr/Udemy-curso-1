# O hex() converte um número em sua representação hexadecimal
hex(64)

# O bin() converte um número em sua representação binária
bin(64)

# Também podemos utilizar o método pow() para fazer potências e raízes
pow(2, 6) # Potência, equivalente ao trecho: 2 ** 6
pow(4096, 1/2) # Raíz, equivalente ao trecho: 4096 ** 1/2

# O método round() vai arredondar um número ao seu valor mais próximo
round(63.5)
round(64.4)
# Também podemos passar o número de dígitos que queremos arredondar
round(64.63567823543, 2)
# E também podemos arredondar números grandes como:
round(64368509, -6) # Neste caso arredondamos para a dezena de milhão mais próxima