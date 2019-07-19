idade = int(input('Qual sua idade? '))
if idade < 18:
 print('menor de idade')
elif (idade >= 18) and (idade <65):
   print('maior de idade')
elif idade >= 65:
   print('idoso')
