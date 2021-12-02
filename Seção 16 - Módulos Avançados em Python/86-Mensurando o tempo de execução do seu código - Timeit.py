# Timeit é um módulo do Python que nos permite mensurar o tempo de execução do código

import timeit

'-'.join(str(n) for n in range(100))

timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)  # Devemos passar o método em string e o number significa a quantidade de vezes que o Python rodará o código

timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000) # Agora utilizamos o mesmo método com compreensão em listas

timeit.timeit("'-'.join(map(str, range(100)))", number=10000) # Agora com map...

# Por análise, vemos que o map é o melhor método que usamos para realizar a mesma tarefa


# Também podemos utilizar o line_profiler (uma biblioteca de terceiros) além de outros métodos