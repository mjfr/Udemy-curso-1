# O if, elif e else permitem a execução de ações alternativas baseadas em condições
# Formato geral do if, elif, else
# if (condição):
#   Faz algo
# elif (condição):
#   Faz algo
# else:
#   Faz algo
a = 1
b = 1
bol = a == b

# Exemplo de if. Seria redundante comparar se bol (que é um boolean True) é igual a True. Logo, omitimos a comparação "if bol == True:" pois o if só prossegue se a condição for cumprida(verdadeira)
if bol:
    a += 10
a #11

if a == b:
    a + 10000
a # Continua sendo 11 pois 'a' deixou de ser igual a 'b' depois do primeiro if


# Exemplo de elif e else. Elif é usado para caso a primeira condição não seja satisfeita, uma nova condição será passada. Else é usado para caso TODAS as comparações não sejam satisfeitas, assim a linha de código após o else será executada.
nota_alunos = [10, 9, 9, 8, 5, 10, 7]
if nota_alunos[4] >= 6:
    print('Aprovado!')
elif nota_alunos[4] >= 7:
    print('Recuperação!')
else:
    print('Reprovado!')