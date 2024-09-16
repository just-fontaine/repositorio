casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)
trintaporc = salario * 0.30

print(f'\nA prestação mensal é \033[31m{parcela:.2f}\033[m.')

if parcela < trintaporc:
    print('\n\033[34mO empréstimo foi aprovado, pois é possível financiar a casa.\033[m')
else:
    print('\n\033[31mO empréstimo foi negado, pois não é possível financiar a casa.\033[m.')
