nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))
nota4 = int(input("Informe a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print ("A média das notas é: ", media)
if media < 6:
 print('abaixo da média')
if media > 6:
 print('acima da média')
if media == 6:
 print('na média')
