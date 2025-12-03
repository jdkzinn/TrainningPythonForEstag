# Importa o módulo para obter o ano atual
from datetime import datetime

# Obtém o ano atual
ano_atual = datetime.now().year

# Solicita o ano de nascimento
ano_nascimento = int(input("Em que ano você nasceu? "))

# Calcula a idade
idade = ano_atual-ano_nascimento

# Exibe o resultado
print(f"Você tem {idade} anos ou fará {idade} anos este ano!")