import os
import library103


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler o arquivo')
    else:
        print('PESSOAS CADASTRADAS'.center(30))
        library103.linha()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')

            # Lê o arquivo de forma bonitinha
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
        a.close()
        if os.path.getsize(nome) == 0:
            print('\n\033[31mNinguém foi cadastrado ainda.\033[m\n')


def cadastrar(arquivo, nome='<Desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo.')
    else:
        try:
            if os.path.getsize(arquivo) == 0:
                a.write(f'{nome};{idade}')
            else:
                a.write(f'\n{nome};{idade}')
        except:
            print(f'Houve um erro ao escrever os dados.')
        else:
            print(f'\n\033[32mRegistro de {nome} adicionado.\033[m\n')
            a.close()


def excluir_arquivo(nome):
    try:
        os.remove(nome)
    except FileNotFoundError:
        print(f'O arquivo {nome} não foi encontrado.')
    except PermissionError:
        print(f'Permissão negada para excluir o arquivo {nome}.')
    except Exception as e:
        print(f'Ocorreu um erro ao tentar excluir o arquivo {nome}: {e}')
    else:
        print(f'\n\033[31mLista de nomes excluída.\033[m')
        quit()
