import os

restaurantes = ['lutiano', 'confraria', 'cia']

def exibir_subtitulo(texto):
    print(texto)
    print()

def retornar_menu():
    input('\nDigite uma tecla para retornar ao menu')
    main()

def limpar_console():
    os.system('cls')

def exibir_nome_do_programa():
    print('\n𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar_app():
    limpar_console()
    exibir_subtitulo('Encerrando o app')

def cadastrar_restaurante():
    limpar_console()
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O {nome_do_restaurante} foi cadastrado com sucesso!')
    retornar_menu()

def listar_restaurante():
    limpar_console()
    exibir_subtitulo('Listar restaurante')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    retornar_menu()

def ativar_restaurante():
    limpar_console()
    exibir_subtitulo('Ativar restaurante')

def opcao_invalida():
    limpar_console()
    exibir_subtitulo('Opção inválida')
    retornar_menu()

def escolhe_opcao():
    opcao_escolhida = int(input('Escolha uma opção\t '))

    try:
        match opcao_escolhida:
            case 1: cadastrar_restaurante()
            case 2: listar_restaurante()
            case 3: ativar_restaurante()
            case 4: finalizar_app()
            case _: opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_console()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolhe_opcao()

if __name__ == '__main__':
    main()