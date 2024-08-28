import os

celulares = [{'nome':'iPhone', 'Modelo':'11', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'11 Pro','ativo': True},
             {'nome':'iPhone', 'Modelo':'11 Pro Max', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'12 Mini', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'12', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'12 Pro', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'12 Pro Max', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'13 Mini', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'13', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'13 Pro', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'13 Pro Max', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'14', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'14 Plus', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'14 Pro', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'14 Pro Max', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'15', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'15 Plus', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'15 Pro', 'ativo': True},
             {'nome':'iPhone', 'Modelo':'15 Pro Max', 'ativo': True},
             ]

def mostra_titulo():
    print("""
    ░█▀▀█ █▀▀ █── █── 　 ▀▀█▀▀ █▀▀ █▀▀ █──█ 
    ░█─── █▀▀ █── █── 　 ─░█── █▀▀ █── █▀▀█ 
    ░█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ 　 ─░█── ▀▀▀ ▀▀▀ ▀──▀
    """)

def mostra_escolhas():
    print('1. Cadastrar Celulares')
    print('2. Listar Celulares')
    print('3. Ativar Celulares')
    print('4. Sair')


def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system('cls')
        print(texto)
        print('')

    def retorna_menu():
            input("Aperte qualquer tecla para retornar")
            main()

    def cadastro_Celulares():
            exibir_subtitulo('Cadastrar Celulares')

            os.system('cls')
            print('Cadastro de novos Celulares')
            destino_celular = input("Digite para onde vai o seu Celular")
            celulares.append(destino_celular)
            print(f" O seu Celular foi Cadastrado com sucesso e será enviado para: {destino_celular} ")

            retorna_menu()

    def listar_celulares():
        exibir_subtitulo('Lista de Celulares Cadastrados')
        
        for celular in celulares:
            nome_celular = celular['nome']
            modelo_celular = celular['Modelo']
            ativo = celular['ativo']
            print(f' - {nome_celular} | {modelo_celular} | {ativo}')
        
        retorna_menu()
    
    def finalizar_app():
        os.system('cls')
        print("Finalizando programa")

    def opcao_invalida():
        print("Opçao Invalida")
        input("Aperte um botão para retornar")
        main()

    opcao_escolhida = int(input('Escolha uma opção:'))
    try:
        if opcao_escolhida == 1:
            cadastro_Celulares()
        elif opcao_escolhida == 2:
            listar_celulares()
        elif opcao_escolhida == 3:
            print('Ativar Celular')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    mostra_titulo()
    mostra_escolhas()
    escolher_opcao()

if __name__ == "__main__":
    main()