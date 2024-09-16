import library103
import arquivo103
import time


def linha():
    # Função de criar linha
    print('~' * 30)


# Nome do arquivo
arq = 'listadenomes.txt'

# Se o arquivo não existir, criar o arquivo
if not arquivo103.arquivo_existe(arq):
    arquivo103.criar_arquivo(arq)

# Estrutura principal do menu dentro de um 'While infinito'
while True:
    library103.menu()

    # Opção lê um número inteiro
    opcao = library103.opcao()

    # Se a opção não for 1, 2, 3 ou 4 ela reinicia
    while opcao not in (1, 2, 3, 4):
        print('\033[31mEscolha uma opção de 1 a 4.\033[m')
        time.sleep(1)
        library103.menu()
        opcao = library103.opcao()

    if opcao == 1:
        # Listar o conteúdo do arquivo
        linha()
        arquivo103.ler_arquivo(arq)
        time.sleep(1)

    if opcao == 2:
        # Cadastrar uma nova pessoa
        linha()
        print('\033[33mNOVO CADASTRO\033[m'.center(30))
        linha()
        try:
            nome = str(input('\033[33mNome:\033[m '))
        except KeyboardInterrupt:
            break
        idade = library103.ler_idade()
        arquivo103.cadastrar(arq, nome, idade)

    if opcao == 3:
        # Excluir lista
        arquivo103.excluir_arquivo(arq)

    if opcao == 4:
        # Sair do programa
        linha()
        print(f'Saindo do sistema...')
        time.sleep(1)
        break
