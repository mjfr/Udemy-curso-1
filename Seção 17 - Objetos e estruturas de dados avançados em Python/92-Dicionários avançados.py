# Dicionários suportam compreensão em dicionários
{x:x**2 for x in range(10)} # Não é muito comum utilizar desta forma pois não temos controle sobre as chaves do dicionário

d = {'k1':1, 'k2':2}
d

# Iterar sobre as chaves do dicionário
for k in d.keys():
    print(k)

# Iterar sobre os valores do dicionário
for k in d.values():
    print(k)

# Gerar tuplas sobre cada par de chaves:valores
for k in d.items():
    print(k)

