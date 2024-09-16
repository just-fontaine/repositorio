def dicionario_notas(*notas, situacao=True):

    """
    ~CRIA UM DICIONÁRIO COM TOTAL DE NOTAS, MAIOR NOTA, MENOR NOTA, MÉDIA E SITUAÇÃO
    (BOA/RUIM), SENDO A SITUAÇÃO OPCIONAL~

    :param notas: recebe as notas (qualquer quantidade)

    :param situacao: se a situação for 'True' o dicionário recebe a situação (boa/ruim)
    de acordo com a média.

    exemplo: se a média for maior de 5 o dicionário recebe 'Situação': Boa
    caso contrário 'Situação': Ruim
    mas APENAS se a situação receber 'True'

    :return: retorna o dicionário completo com todas as informações
    """

    dicionario = {
        'Total de notas': len(notas),
        'Maior nota': max(notas),
        'Menor nota': min(notas),
        'Média': sum(notas) / len(notas)
    }
    if situacao:
        if dicionario['Média'] < 5:
            dicionario['Situação'] = 'Ruim'
        else:
            dicionario['Situação'] = 'Boa'
    return dicionario


# Programa principal
resp = dicionario_notas(5, 2, 3.2, 5.4, 5, 9, 10, 10, 9)
print(resp)

help(dicionario_notas)
