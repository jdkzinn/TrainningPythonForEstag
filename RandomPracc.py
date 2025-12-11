# Crie um programa que pergunte o nome do usuário, idade, empresa/cargo que trabalha e seu hobby
# Após isso, trate com try, execpt, if/elif/else e finnaly (se aplicável)

def coletarDados():
    listarDados = [] # Colchete vazio
    try:
        name = input(f'Qual o seu nome? ')
        listarDados.append(name)
        age = int(input(f'Legal {name}, qual sua idade? '))
        listarDados.append(age)
        enterprise = input(f'Qual nome da empresa que você trabalha? ')
        listarDados.append(enterprise)
        role = input(f'E qual seu cargo na empresa {enterprise}? ')
        listarDados.append(role)
        hobby = input(f'Qual seu hobby favorito {name}? ')
        listarDados.append(hobby)
    except ValueError:
        print(f'Digite um valor correto de acordo com o que é solicitado!')
    
    return listarDados

if __name__ == '__main__':
    dadosPessoa = 's'

    while dadosPessoa == 's':
        print(f'Responda as perguntas abaixo\n')
        try:
            colect = coletarDados()
        except ValueError:
            print('Ocorreu um erro inesperado, tente novamente.')
        else:
            print(f'Seu nome é {colect[0]},\
                você tem {colect[1]}, \
                trabalha na {colect[2]} \
                no cargo de {colect[3]} \
                e, seu hobby é {colect[4]}')
        finally:
            print(f'\nDados Coletados com sucesso!')
    
        dadosPessoa = input(f'\nDeseja responder outra vez? S para SIM, outra tecla para NÃO: \n')
        dadosPessoa = dadosPessoa.lower() # Não sabemos se o usuário irá utilizar CAPSLOCK ou NÃO.
        if dadosPessoa != 's':
            print(f'Até a próxima, amigo(a)!\n')
