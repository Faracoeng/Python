print('Insira a velocidade média e a distância de um trajeto para descobrir o tempo estimado em horas:')
d = float(input('Distância em km: '))
v = float(input('Velocidade média em km/h: '))
t = d / v
print ('Tempo aproximado em horas: %.1f' %t)
