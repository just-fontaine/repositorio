import time
print('\n\033[33mCálculo de IMC de um adulto.\033[m')
time.sleep(1)
peso = float(input('\nDigite seu peso em kilos: '))
altura = float(input('\nDigite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'\n\033[33mSeu IMC é {imc:.0f} e você é considerado abaixo do peso.\033[m')
elif imc >= 18.5 and imc < 25:
    print(f'\n\033[34mSeu IMC é {imc:.0f} e você está no peso ideal.\033[m\033[m')
elif imc >= 25 and imc < 30:
    print(f'\n\033[33mSeu IMC é {imc:.0f} e você está com sobrepeso.\033[m')
elif imc >= 30 and imc < 40:
    print(f'\n\033[31mSeu IMC é {imc:.0f} e você é considerado obeso.\033[m')
else:
    if imc > 40:
        print(f'\n\033[31mSeu IMC é {imc} e você tem obesidade mórbida.\033[m')
