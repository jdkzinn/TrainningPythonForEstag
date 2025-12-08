# O programa deve gerar um numero aleatorio entre 1 e 15, e pedir para o usuário adivinhar o numero gerado
# Se a tentativa do user nao for correta, o programa deve informar se ele tentou um valor baixo ou alto comparado ao gerado
# Se o user acertar: parabens, voce acertou!
# o programa deve permitir 3 tentativas por jogo
# a tecla s permite iniciar um novo jogo

import random

# Executar o programa quando o arquivo for chamado diretamente
if __name__ == '__main__':
    novoJogo = 's'
    
    while novoJogo == 's':
        print(f'\nBem vindo ao jogo de adivinhação do DK')
        print(f'Você terá 3 tentativas, use-as com sabedoria!')

        numeroSorteado = random.randint(1, 15) # gerando número aletório ente 1 e 15
        tentativas = 3  # Resetar tentativas para cada novo jogo
        acertou = False

        # Jogar:
        for i in range(3):
            tentativas_restantes = 3 - i - 1  # Calcula tentativas restantes corretamente
            
            try:
                chute = int(input(f'\nChute um número de 1 a 15: ')) # Criando variável para o chute
                
                if chute < 1 or chute > 15:
                    print('Por favor, digite um número entre 1 e 15!')
                    continue
                    
            except ValueError:
                print('Entrada inválida! Por favor, digite apenas números.')
                continue

            if (chute == numeroSorteado):
                print(f'\nParabéns, você acertou! Ganhou 500 dkPoints, e ainda sobraram {tentativas_restantes} tentativas')
                acertou = True
                break
            elif (chute > numeroSorteado):
                print(f'\nO número escolhido é maior que o número sorteado, restam {tentativas_restantes} tentativas')
            else:
                print(f'\nO número escolhido é menor que o número sorteado, restam {tentativas_restantes} tentativas')

        # Caso não tenha acertado, revelar o número secreto:
        if not acertou:
            print(f'\nO número secreto era o {numeroSorteado}')
            
        # O usuário deseja jogar novamente? 
        novoJogo = input(f'\nDeseja jogar outra vez? S para SIM, outra tecla para NÃO: \n')
        novoJogo = novoJogo.lower() # Não sabemos se o usuário irá utilizar CAPSLOCK ou NÃO.
    
    print('\nObrigado por jogar! Até logo!')




