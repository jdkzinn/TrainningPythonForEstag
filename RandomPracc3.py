# Programa para calcular o Índice de Massa Corporal (IMC) -- Prática livre 😉

name = input('\nDigite seu nome: ')
altura = float(input('\nDigite sua altura (m): '))
peso = float(input('\nDigite seu peso (kg): '))
imc = peso / (altura ** 2)

print(f'\n{name}, seu IMC é: {imc:.2f}')
