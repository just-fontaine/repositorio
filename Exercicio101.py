def leia_int():
    while True:
        try:
            x = input('Digite um número inteiro: ').strip()
            x = int(x)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
    return x


def leia_float():
    while True:
        try:
            x = input('Digite um número real: ').strip()
            x = float(x)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
    return x


inteiro = leia_int()
real = leia_float()
print(f'O número inteiro foi {inteiro} e o real foi {real}.')
