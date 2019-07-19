quantidadeDeSomas = int(input('Quantos números voce deseja fazer a média?: '))
count = 0
total = 0
while count < quantidadeDeSomas:
    num = int(input('insira o número: '))
    total += num
    count += 1
print(total / count)
