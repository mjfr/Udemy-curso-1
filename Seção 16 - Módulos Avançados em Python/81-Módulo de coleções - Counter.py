# Counter nos permite contar elementos dentro de iteráveis
from collections import Counter

l = [1, 2, 3, 3, 3, 3, 1, 2, 1, 1, 1, 4, 5, 6, 3, 2, 2, 1, 4, 2, 5, 6, 1]
Counter(l)

Counter('Aasafdgdsfssaertastreryfgassaasasasassdfgewsasasasasasdewdfggdf')

s = 'Quantas palavras aparecem dentro desta frase? Serão 4 palavras que aparecem?'
c = Counter(s.split())
print(c)
n = len(c)

# Alguns padrões comuns ao usar o objeto Counter()
sum(c.values())                 # Total de todas as contagens
c.clear()                       # Redefinir todas as contagens
list(c)                         # Elementos exclusivos da lista
set(c)                          # Converter para um conjunto
dict(c)                         # Converter para um dicionário regular
c.items()                       # Converter para uma lista de pares (elem, cnt)
Counter(dict(c))                # Converter de uma lista de pares (elem, cnt)
c.most_common()[:-n-1:-1]       # Os n elementos menos comuns
c += Counter()                  # Remove zero e contagens negativas