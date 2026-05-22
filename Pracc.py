# coding: utf-8
cars = [
    {
        "modelo" : "GTR NISMO",
        "marca" : "NISSAN",
        "ano" : 2024,
        "preco" : 650_000.00
    },
    {
        "modelo" : "PURO SANGUE",
        "marca" : "FERRARI",
        "ano" : 2022,
        "preco" : 1_300_000.00
    },
    {
        "modelo" : "URUS",
        "marca" : "LAMBORGHINI",
        "ano" : 2023,
        "preco" : 1_000_000.00
    },
    {
        "modelo" : "SUPRA",
        "marca" : "TOYOTA",
        "ano" : 2024,
        "preco" : 570_000.00
    }
]

contador2022 = 0
contador2024 = 0
carros2022 = []
carros2024 = []

for car in cars:
    if car['ano'] == 2022:
        contador2022 += 1
        carros2022.append(car)
    elif car['ano'] == 2024:
        contador2024 += 1
        carros2024.append(car)

print(f"\nQuantidade de carros do ano 2022: {contador2022}") 
for car in carros2022:
    print(f" - {car['modelo']}")

print(f"Quantidade de carros do ano 2024: {contador2024}")
for car in carros2024:
    print(f" - {car['modelo']}")
