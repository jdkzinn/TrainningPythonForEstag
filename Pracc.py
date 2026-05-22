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
        "preco" : 1_100_000.00
    },
    {
        "modelo" : "SUPRA",
        "marca" : "TOYOTA",
        "ano" : 2024,
        "preco" : 570_000.00
    }
]

for car in cars:
    print(f"Modelo: {car['modelo']} | Marca: {car['marca']}")

print(f"\nCarros com preço acima de R$600.000,00:\n")
for car in cars:
    if car['preco'] >= 600_000.00:
        print(f"Carro: {car['modelo']} | Preço: R${car['preco']:.2f}")
