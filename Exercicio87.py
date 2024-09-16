def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)


escreva('Olá, mundo')
escreva('Gustavo Guanabara')
escreva('CeV')

escreva('KKKKKKKKKKKKKKK TA IN SHOK PAEZAO')


def escreva2(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


escreva2('Oi')
escreva2('Eu amo batata frita')
escreva2('Gosto de viajar, mas a pandemia do Covid19 impactou as nossas vidas')
