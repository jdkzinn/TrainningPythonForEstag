# Lista: representa uma sequência de valoers

# Sintaxe: nome_lista = [valores]

notas = [1, 5, 8, 3, 2]
notas2 = [10, 9, 2, 78, 182]
valores = notas + notas2 
notasString = ['teste', 'acabacte', 'futebol']

for a in notasString:
    print(a)


bebidas = []
for i in range(5):
    bebida = input(f'Digite uma bebida favorita: ')
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)
print(f'\nSaúde!')
    