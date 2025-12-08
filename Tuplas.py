# São imutáveis, ou seja (não podem ser alteradas)

from typing import Literal


paises = ('BR', 'EUA', 'US', 'SPA', 'JPA', 'CH')
gases = ('HE', 'NE', 'AR', 'XE', 'KR', 'RN')
t1 = (1, 5, 6, 0, 18, 237, 5, 367, 4, 92, 5, 0)
all = paises + gases

print(sum(t1))

# Operações não disponíveiss em tuplas: .sort(), .append(), .reverse(), .pop() e etc...
## Qualquer método que altere a tupla.


grupoDePaises = list(paises)
grupoDePaises[1] = 'UK'
print(grupoDePaises)

for pais in grupoDePaises:
    print(f'País: {pais}')

# Também é possível alterar uma LISTA para TUPLA:

grupoUm = ['LA', 'HOLL', 'TX', 'BSB', 'SP', 'RJ']
teste = tuple(grupoUm)
print(type(teste))
print(sorted(teste))

