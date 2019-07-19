print('Insira uma quantidade de dias, horas,minutos e segundos, e elas serão convertidas em segundos: ')
print('')
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))

total = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print (total)
