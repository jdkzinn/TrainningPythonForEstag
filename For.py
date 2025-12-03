lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
palavra = 'DKzin'

for i in lista: # o "i" pode ser qualquer nome, no caso será tipo o nome da variável do "for"
    print(i)

for letra in palavra:
    print(letra)

################################################

for i in range(10): 
    print(i)

print('fim')

for outraForma in range(11, 20): 
    print(outraForma)


nome = input('Digite seu nome: ')
for x in range(10):
    print(f'> {x + 1} {nome} <')

# range(valor_inicial, valor_final, incremento) ex:

for x in range(2, 20,2):
    print(x)

for x in range(20, 2, -2):
    print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedraTrue in pedras:
    if pedraTrue == 'Quartzo':
        continue # Diferente do break, essa instrução impedirá que imprima o Quartzo
    print(pedraTrue)