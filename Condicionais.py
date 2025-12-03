# Simples, Composto, Encadeado
n1 = 0.0
n2 = 0.0
faltas = 0

n1 = float(input("Digite uma nota para o aluno: "))
n2 = float(input("Digite outra nota para o aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

media = (n1 + n2) / 2

if (faltas >= 10):
    print(f"Você faltou {faltas} dias, é uma pena.")
    print(f"Sua média foi {media:.2f}. Mas você está reprovado por falta.")
elif (media >= 7):
    print(f"Esta foi sua nota média: {media:.2f}")
    print("Parabéns, você está aprovado!")
elif (media >=5):
    print(f"Esta foi sua nota média: {media:.2f}")
    print("Tente melhorar no próximo bimestre, você está de recuperação.")
else:
    print(f"Esta foi sua nota média: {media:.2f}")
    print("Lamentamos muito, você está reprovado.")