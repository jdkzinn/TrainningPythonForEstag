import random

for cont_ex in range(1, 6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5, 0, -1):
        print(f'Valor: {cont_in}')

print('Fim dos laços de repetição!')


for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1, 100)
        print(f'Valor: {num}')