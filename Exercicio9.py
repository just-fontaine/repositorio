import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print(f'\033[33mÂngulo: {an:.0f}°\033[m')
print(f'\033[31mSeno: {seno:.2f}\033[m')
print(f'\033[35mCosseno: {cosseno:.2f}\033[m')
print(f'\033[34mTangente: {tan:.2f}\033[m')
