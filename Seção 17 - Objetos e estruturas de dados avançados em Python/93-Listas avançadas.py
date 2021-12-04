# Uma das diversas formas de se adicionar itens em listas é o .append()
l = [1, 2, 3]
l.append(4)
l

# Também podemos retornar quantas vezes um certo elemento ocorre em uma lista com .count()
l.count(2)

# O .extend() funciona assim como o .append() porém se passarmos uma lista ele quebra a lista e adiciona os elementos da lista quebrada como elementos individuais a nova lista
l.append(['Lista', 1, 'passada', 'por', 6, 'append'])
l
l.extend(['Agora', 'a', 534, 'lista', 3, 5, 6, 'foi passada por', 0, 'extend'])
l

# Listas possuem o índice que nos retorna o índice do elemento passado
l.index('Agora')

# Podemos inserir elementos em uma lista passando o índice que queremos que o mesmo apareça
l.insert(12, 'NOVO ELEMENTO DO ÍNDICE 12')
l

# O método .pop() remove da lista o último elemento dela e é possível salvar em uma variável
pop_ultimo = l.pop()
pop_ultimo
l

# O método .remove() remove da lista a primeira ocorrência do valor passado como parâmetro
l.remove(3)
l

# O método .reverse() reverte a ordem da lista
l.reverse()
l

# O método .sort() ordena a lista, porém podem ocorrer erros com tipos de dados diferentes em lista
l.remove(['Lista', 1, 'passada', 'por', 6, 'append'])
l.remove('Agora')
l.remove('a')
l.remove('lista')
l.remove('foi passada por')
l.remove('NOVO ELEMENTO DO ÍNDICE 12')
l.sort()
l