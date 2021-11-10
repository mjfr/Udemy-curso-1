myList = [1, 2, 3]
myList[1]

# O uso do dicionário assemelha-se ao uso do .json
# Dicionários não apresentam ordem

# Diferente das listas (feitas com colchetes) dicionários são feitos com chaves.
# Dicionários funcionam através de {'chave':valor}
myDict = {'chave1':1.2, 'chave2':'shrimp', 'chave3':myList}
myDict

# Dicionários também são indexáveis, porém por suas respectivas chaves
myDict['chave2']
myDict[1]

# Dicionários aceitam alterações de seus elementos internos
myDict['chave1'] = 3.4
myDict

# É possível criar dicionários vazios e com a necessidade ir adicionando chaves e valores
dictVazio = {}
dictVazio['chave1'] = 'valor1'
dictVazio

# Alguns métodos imbutidos no dicionário
dictMetodos = {'chave1':8, 'chave2':'teste', 'chave3':myList,  'chave4':15.79,  'chave5':-33.2,  'chave6':[8, 'Lista', 3.3],  'chave7':'caixa alta'.upper(),  'chave8':0,  'chave9':3+3**3,  'chave10':'Ultimo valor'}
dictMetodos

# O método .keys() retorna as chaves presentes no dicionário
dictMetodos.keys()
# Passando para formato de lista:
list(dictMetodos.keys())

# O método .values() retorna os valores das chaves presentes no dicionário
dictMetodos.values()
# Passando para formato de lista:
list(dictMetodos.values())

# O método .items() retorna chaves e valores do dicionário em formato de tuplas (Tuplas serão estudadas na aula 21-Tuples)
dictMetodos.items()