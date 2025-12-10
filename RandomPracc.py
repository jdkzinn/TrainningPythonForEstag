# Crie um programa que pergunte o nome do usuário, idade, empresa/cargo que trabalha e seu hobby.
# Após isso, trate com try, execpt, if/elif/else, finnaly e etc.

def coletarDados():
    name = input(f'Qual o seu nome? ')
    age = int(input(f'Legal {name}, qual sua idade? '))
    enterprise = input(f'Qual nome da empresa que você trabalha? ')
    role = input(f'E qual seu cargo na empresa {enterprise}? ')
    hobby = input(f'Qual seu hobby favorito {name}? ')

if __name__ == '__main__':
    while True:
        try:
            coletarDados()
        except ValueError:
            print(f'Digite dados válidos!')
        except:
            print(f'Ocorreu um erro inesperado, tente novamente!')
        else:
            print(f'\nDados Coletados com sucesso!')
        finally:
            print(f'Seu nome é {coletarDados.name},\
                você tem {coletarDados.age}, \
                trabalha na {coletarDados.enterprise} \
                no cargo de {coletarDados.role} \
                e, seu hobby é {coletarDados.hobby}')
