def area_retangulo(a, b):
    return a * b


print('CONTROLE DE TERRENOS')
print('-' * 30)
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
print(f'Área: {area_retangulo(largura, altura):.1f}m²')
print('-' * 30)

