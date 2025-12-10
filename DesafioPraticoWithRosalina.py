# Criar um jogo de pedra papel ou tesoura entre o usuário e a máquina = Concluído
import random

novo_jogo = 's'

def jogo():
    computador = random.choice(['pedra', 'papel', 'tesoura'])
    usuario = input('Digite o que deseja escolher para jogar: Pedra, papel ou tesoura?\n')
    usuario = usuario.lower()
    
    if usuario not in ['pedra', 'papel', 'tesoura']:
        raise ValueError('Entrada inválida')

    if usuario == computador:
        print(f'Empate! Você jogou {usuario} e o computador também jogou {computador}')
    elif usuario == 'pedra' and computador == 'papel' or usuario == 'papel' and computador == 'tesoura' \
        or usuario == 'tesoura' and computador == 'pedra':
        print(f'Você perdeu! O computador jogou {computador}, e {computador} ganha de {usuario}')
    else:
        print(f'Parabéns, você ganhou! {usuario} ganha de {computador}')


while novo_jogo == 's':
    try:
        jogo()
    except ValueError as e:
        print(f'Erro: {e}')
        print('Por favor, escolha uma das opções: pedra, papel ou tesoura.\n')
        continue
    
    novo_jogo = input('Deseja jogar novamente? Digite "s" para sim e "n" para não.\n')
    novo_jogo = novo_jogo.lower()

# Tarefa: adicionar tratamento de exceções = Concluído