print('Isira o salário e a porcentagem de aumento para fazer o reajuste')
s = float(input('Salário: '))
p = float(input('Porcentagem de aumento: '))
aumento = s * p / 100
reajuste = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %reajuste)
