# não completado

numeros = list()
maior = menor = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        numeros.append(num)
        maior = num
        menor = num
    if c > maior:
        maior = num
        numeros.append(maior)
    if c < menor:
        menor = num
        numeros.insert(menor)
print(numeros)
