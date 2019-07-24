print ('-' * 50)  #Repete 30 vezes o caractere '-'
print('{:^50}'.format('Simulador de Caixa eletrônico')) #centralisa o texto
print ('-' * 50)
valorParaSaque = int(input('Qual valor você deseja sacar?'))
montante = valorParaSaque
cedula = 100
totalCedulas = 0
while True:
    if montante >= cedula:
        montante = montante - cedula
        totalCedulas += 1
    else:
        print('Total de ',totalCedulas,' cedulas de R$',cedula)
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        totalCedulas = 0
        if montante == 0:
            break
            
