x = y = z = 0
x = int(input('Digite um número: ')) # Convertendo o input para inteiros
y = int(input('Digite outro número: ')) # Convertendo o input para inteiro
z = x + y
print(f"A soma de x + y é: {z}")

# Desafio: melhore o código do exercício anterior, de modo que ele exiba além da soma: a subtração, a multiplicação,
# a divisão, módulo (%), o primeiro elevao ao segundo (Exponenciação). Entre os valores x e y digitados pelo usuário.

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y
modulo = x % y
potencia = x ** y

print(f"A soma de x + y é: {soma}")
print(f'A subtração de x - y é: {subtracao}')
print(f'A multiplicação de x * y é: {multiplicacao}')
print(f'A divisão de x / y é: {divisao}')
print(f'O módulo de x % y é: {modulo}')
print(f'O primeiro elevado ao segundo (x ** y) é: {potencia}')