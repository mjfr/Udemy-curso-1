# O datetime nos dá muito poder para tratar dados temporais
import datetime
timestamp = datetime.time(4, 20, 1) # Parâmetros = hora, minuto, segundo
timestamp.hour
timestamp.minute
timestamp.second
timestamp.microsecond 
timestamp.tzinfo # Timezone 
datetime.time(0, 0)
datetime.time.max
print(datetime.time.resolution)
today = datetime.date.today()
print(today.ctime())
today.year
today.month
today.day
today

# Também podemos fazer operações aritiméticas com o tempo, lembrando que YYYY, M, D
dia_inicio = datetime.date(1999, 5, 1)
dia_fim = datetime.date(2021, 5, 1)

dia_fim-dia_inicio

dia_inicio
# Convertendo para string
str_date = dia_inicio.strftime('%Y-%m-%d')
str_date
type(str_date)

str_date.split('-')