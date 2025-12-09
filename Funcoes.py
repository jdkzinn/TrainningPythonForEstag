# Funções
# Modularização, re-utilização de código e legibilidade.

def mensagem():
    name = 'Deryk Silva'
    age = 27
    enterprise = 'IBM USA'
    timing = '3 meses'
    print(f'Meu nome é {name}, tenho {age} anos e, trabalho na {enterprise} há {timing}.')

mensagem()


# Função com argumentos

def soma(a, b):
    print(a + b)
soma(10, 17)  # Estou somando com a função "soma" que calcua A + B (1° e 2° posições)

# Outro exemplo:

def mult(x, y):
    return x * y
print(mult(2, 5))
# ou
numberOne = 2
numberTwoo = 10
multNumber = mult(numberOne, numberTwoo) # Existem várias formas de fazer e receber o mesmo resultado.
print(f'{numberOne} x {numberTwoo} é = {multNumber}') 

def div(k, j):
    return k / j

if __name__ == '__main__':
    try:
        a = int(input(f'Digite um número: '))
        b = int(input(f'Digite outro número: '))
        r = div(a,b)
        print(f'{a} dividido por {b} é igual a {r}')
    except:
        print(f'Ímpossível dividir por 0, digite um número inteiro válido!')


# Outra forma

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9, 12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)

def contar (num = 0, caractere = ''):
    for i in range(1, num):
        print(caractere)

if __name__ == '__main__':
    contar(6, 'DK')


