# Listas são 'arrays', estruturas que permitem guardar multiplos tipos de dados e seu tamanho não é constante
var = 1
my_list = [1, 2, 3]
my_list
my_list2 = [1, 'String', 1.3456]
my_list2

# Listas são sequências, assim também podem ser indexadas
my_list2[1]
my_list2[-1]
my_list2[:1]

# Também é possível juntar listas
my_list2 + my_list

# E multiplicar também
my_list2 * 30

# Alguns métodos presentes nas listas:
# .append() adiciona um elemento ao final da lista
my_list2.append('Mais um elemento adicionado')
my_list2

# .pop() retira por padrão o último item da lista e retorna o mesmo, ou podemos definir o índice do item que será retirado
my_list2.pop(2)
my_list2

new_list1 = ['a', 'e', 'i', 'o', 'u']
# .reverse() inverte a ordem da lista
new_list1.reverse()
new_list1[::-1]
new_list1

new_list2 = [5, 2, 4, 7, 9, 3, 1, 2, 1]
# .sort() ordena a lista por ordem alfabética ou numérica
new_list2.sort()
new_list2

# Listas dentro de listas, matrizes.
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
matriz = [lst_1, lst_2, lst_3]
matriz

# Também indexável, tanto dentro da matriz quanto dentro de seus elementos
matriz[2]
matriz[1][1]

# Método de compreensão em listas (utiliza laços de repetição que serão estudados na Seção 5 - Declarações em Python)
primeira_coluna = [coluna[2] for coluna in matriz]
primeira_coluna