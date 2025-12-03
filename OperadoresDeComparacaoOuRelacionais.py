x = y = z = False
n1 = n2 = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 == n2:
    print('São iguais!')
else:
    print('São diferentes!')

if n1 > n2:
    print('N1 é maior que N2!')
else:
    print('N2 é maior que N1')

x = n1 == n2
print(f"São iguais? {x}")

z = n1 > n2
print(f"{n1} É maior que {n2}? {z}")

y = n1 != n2
print(f"São diferentes? {str(y)}")