# Programa que verifica se você pode participar do evento (exercício para AND)

idade = int(input("Informe a idade "))
altura = float(input("Informe a altura (ex: 1.75) "))

resultado = (idade >= 18) and (altura >= 1.70)
msg = f"Pode participar do evento? {resultado}"

if resultado == True:
    print(msg)
else:
    print(msg)


# Programa de disparo de alarme (exercício para OR)

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')

msgAlarme = f"Alarme disparado? {str(alarme)}"

print(msgAlarme)


# Programa para saber se tem dinheiro (exercício para NOT)

temDinheiro = False

temDinheiro = not temDinheiro # Ele alterna o estádo lógico

msgHaveMoney = f"Tem dinehiro? {str(temDinheiro)}"

print (msgHaveMoney)