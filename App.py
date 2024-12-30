import os

restaurantes = ['Mc Donalds', 'La Brasa', 'Garoupa']

def ExibirNomePrograma():
    print ("""""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def ExibirOpcoes():

    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar Restaurantes')
    print ('4. Sair\n')

def OpcaoInvalida():
    print('Opcao inválida!\n')
    Voltar()

def CadastrarRestaurante() :

    ExibirSubtitulo('Cadastro de novos restaurantes')

    nomeRestaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nomeRestaurante) # Inserindo o valor do nome a lista criada. 
    print(f'O restaurante {nomeRestaurante} foi cadastrado com sucesso!\n')

    Voltar()

def ListarRestaurantes() : 
    
    ExibirSubtitulo('Listagem de restaurantes cadastrados')
    
    for restaurante in restaurantes:
        print(f'{restaurante}')
        Voltar()

    


def EscolherOpcoes(): 
    try: 
        opcaoEscolhida  = int(input('Escolha uma opção: '))

        if (opcaoEscolhida == 1) : 
            CadastrarRestaurante()
        elif (opcaoEscolhida == 2) : 
            ListarRestaurantes() 
        elif (opcaoEscolhida == 3) :
            print('3')
        elif (opcaoEscolhida == 4) :
            Finalizar_app()
        else : 
            OpcaoInvalida()
    except:
        OpcaoInvalida()

def Finalizar_app() :

    ExibirSubtitulo('Finalizando o app ...')

def Voltar() : 

    input('\nDigite uma tecla para voltar ao menu ')
    main()

def ExibirSubtitulo(subtitulo) :
    os.system('cls')
    print(subtitulo)
    print()

def main():

    os.system("cls")
    ExibirNomePrograma()
    ExibirOpcoes()   
    EscolherOpcoes()

if __name__ == '__main__' : 
    main()


    
