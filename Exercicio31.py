nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'\n\033[31mSua média e você está reprovado\033[m')
elif 5 < media < 7:
    print(f'\n\033[33Sua média é {media} e você está de recuperação.\033[m')
else:
    print(f'\n\033[34mSua média é {media} e você está aprovado!\033[m')
