# Escreva um laço `for` que imprima todos os elementos entre -5 e 5 usando a função `range`.

for i in range(-5, 6):
    print(i)

# Imprima os elementos da seguinte lista: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'].
# Certifique-se de seguir as convenções do Python.

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

# Escreva um programa em Python usando um laço `for` que imprima números de 1 a 15, mas:

# Ignore múltiplos de 3.
# Interrompa o laço se o número for maior que 12.

for i in range(1, 16):
    if i % 3 == 0:
        continue  # skip multiples of 3
    if i > 12:
        break     # stop if number > 12
    print(i)



import numpy as np  # pyright: ignore[reportMissingImports]

a=np.array([1,1,1,1,1])

sum = a+10
print(sum)

V={'A','B','C' }
V.add('C')
print(V)

x="Go"

if(x=="Go"):
    print('Go ')
else:
    print('Stop')

print('Mike')


A=['1','2','3']

for a in A:
    print(2*a)


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_point(self):
        print('x = ',self.x,'y=',self.y)

    

class Points(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(self):
        print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x=2

p2.print_point()