# coding: utf-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

cars = [    
    {
        "modelo" : "GTR NISMO",
        "marca" : "NISSAN",
        "ano_fabricacao" : 2024,
        "ano_modelo" : 2025,
        "preco" : 650_000.00
    },
    {
        "modelo" : "PURO SANGUE",
        "marca" : "FERRARI",
        "ano_fabricacao" : 2022,
        "ano_modelo" : 2023,
        "preco" : 1_300_000.00
    },
    {
        "modelo" : "URUS",
        "marca" : "LAMBORGHINI",
        "ano_fabricacao" : 2023,
        "ano_modelo" : 2024,
        "preco" : 1_000_000.00
    },
    {
        "modelo" : "SUPRA",
        "marca" : "TOYOTA",
        "ano_fabricacao" : 2024,
        "ano_modelo" : 2025,
        "preco" : 570_000.00
    }
]

for car in cars:
    print(f"Carro disponível: {car['marca']} - {car['modelo']} {car['ano_fabricacao']}/{car['ano_modelo']} | Preço: R${car['preco']:,.2f}")

print(f"\nCarros com preço acima de R$600.000,00:")
for car in cars:
    if car['preco'] > 600_000.00:
        print(f"{car['modelo']} | Preço: R${car['preco']:,.2f}")
    elif car['preco'] < 600_000.00:
        print(f"\nCarros com preço abaixo de R$600.000,00:")
        print(f"{car['modelo']} | Preço: R${car['preco']:,.2f}")



contador2022 = 0
contador2024 = 0
carros2022 = []
carros2024 = []

for car in cars:
    if car['ano_fabricacao'] == 2022:
        contador2022 += 1
        carros2022.append(car)
    elif car['ano_fabricacao'] == 2024:
        contador2024 += 1
        carros2024.append(car)

print(f"\nQuantidade de carros do ano 2022: {contador2022}") 
for car in carros2022:
    print(f"{car['marca']} - {car['modelo']}")

print(f"\nQuantidade de carros do ano 2024: {contador2024}")
for car in carros2024:
    print(f"{car['marca']} - {car['modelo']}")
