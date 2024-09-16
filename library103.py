cores = {'padrao': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'amarelo': '\033[33m'}


def opcao():
    while True:
        try:
            while True:
                x = input(f'{cores["amarelo"]}Sua opção:{cores["padrao"]} ').strip()
                x = int(x)
                break
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
    return x


def menu():
    linha()
    print('MENU PRINCIPAL'.center(30))
    linha()
    print(f'{cores["amarelo"]}1-{cores["padrao"]} {cores["azul"]}Ver pessoas cadastradas{cores["padrao"]}\n'
          f'{cores["amarelo"]}2-{cores["padrao"]} {cores["azul"]}Cadastrar uma nova pessoa{cores["padrao"]}\n'
          f'{cores["amarelo"]}3-{cores["padrao"]} {cores["azul"]}Limpar lista{cores["padrao"]}\n'
          f'{cores["amarelo"]}4-{cores["padrao"]} {cores["azul"]}Sair do programa{cores["padrao"]}')
    linha()


def linha():
    print('~' * 30)


def ler_idade():
    while True:
        try:
            x = input('\033[33mIdade:\033[m ').strip()
            x = int(x)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
    return x
