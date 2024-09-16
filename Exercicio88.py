import time


def contagem(inicio, fim, quantidade):
    time.sleep(1)
    if inicio < fim:
        for c in range(inicio, fim + 1, abs(quantidade)):
            print(c, end=' ')
            time.sleep(0.25)
        print('FIM!')
        print('~' * 30)
    else:
        for c in range(inicio, fim - 1, -abs(quantidade)):
            print(c, end=' ')
            time.sleep(0.25)
        print('FIM!')
        print('~' * 30)


print('~' * 30)
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)
print(f'Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, 2)
print(f'Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
while p == 0:
    p = int(input('Passo não pode ser 0: '))
print('~' * 30)
print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
contagem(i, f, p)
