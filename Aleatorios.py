import random

print('\nGerar 5 números inteiros aleatórios entre 1 e 50:')
for int in range(5):
    n = random.randint(1, 50)
    print(f'Numero gerado: {n}')


print('\nGerar 5 números floats aleatórios entre 1 e 20:')
for float in range(5):
    valor = random.random()
    print(f'Numero gerado: {round(valor * 20, 2)}') # o round arredonda, onde está o "2" indica casas decimais


valor = random.uniform(1, 100)
print(f'Número: {round(valor, 2)}')


list = [1, 2, 3, 4, 65, 2823, 26, 253, 45, 9238, 100, 3736, 726, 80]
number = random.choice(list)
print(f'Numéro escolhido {number}\n')


number = random.sample(list, 3) # Retorna 3 números da lista 
print(f'Números escolhidos: {number}')

#Embaralhar abaixo:
print(f'Exibir lista original: {list}')
number = random.shuffle(list)
print(f'Embaralhar a lista e exibi-la: {list}')