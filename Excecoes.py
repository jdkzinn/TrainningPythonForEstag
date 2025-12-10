# Exceção é um objeto que representa um erro que ocorreu ao executar o programa.
# Blocos try ... except

def div(a, b):
    return round (a / b, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input(f'\nDigite um número: '))
            n2 = int(input(f'\nDigite um outro número: '))
            break
        except ValueError:
            print(f'\nDigite um número inteiro válido!')
    
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'\nNão é possivel dividir por ZERO!')
    else:
        print(f'\nResultado: {r}')
    finally:
        print(f'\nFim da divisão!')