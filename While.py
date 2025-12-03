num = 0

while (num <= 25): # faz com que pare em 25
    print(num)
    num += 5 # adiciona de 5 em 5 ao num (0)
print ('Laço encerrado!')

nome = None

while True:
    print('Digite seu nome, ou X para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break # Faz com que pare a execução se a pessoar digitar X
    print(f'Bem vindo, {nome}')
print ('Até logo!')