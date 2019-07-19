velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade > 110:
    velocidadeExcedida = (velocidade - 110)* 5 
    print('Multado em R$',velocidadeExcedida,' reais.')
else:
    print('Não foi multado')
