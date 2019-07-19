minutosMensais = float(input('Quantos minutos de ligação houve no mês?: '))
if minutosMensais < 200:
    faturaMensal = minutosMensais * 0.2
    print('Preço da fatura é R$',faturaMensal,' reais')
    
elif minutosMensais >= 200 and minutosMensais <= 400:
    faturaMensal = minutosMensais * 0.18
    print('Preço da fatura é R$',faturaMensal,' reais')

elif minutosMensais >400:
    faturaMensal = minutosMensais * 0.15
    print('Preço da fatura é R$',faturaMensal,' reais')
