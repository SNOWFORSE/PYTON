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
        os.system('clear')
        linha = "*" * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print('')

    def retorna_menu():
            input("Aperte qualquer tecla para retornar")
            main()

    def cadastro_Celulares():
            exibir_subtitulo('Cadastrar Celulares')

            print('Cadastro de novos Celulares')
            nome_celular = input(" Digite qual Celular você quer: ")
            modelo_celular = input(f' Digite qual modelo que você está procurando: ')
            dados_do_celular = {'nome':nome_celular, 'Modelo':modelo_celular, 'ativo': True}
            celulares.append(dados_do_celular)
            print(f" O Celular {nome_celular} foi Cadastrado com Sucesso!")


            retorna_menu()

    def listar_celulares():
        exibir_subtitulo('Lista de Celulares Cadastrados')
        
        for celular in celulares:
            nome_celular = celular['nome']
            print(f"{nome_celular.ljust(22)} | {modelo.ljust(20)} | Status ")
            modelo_celular = celular['Modelo']
            ativo = celular['ativo']
            print(f' - {nome_celular.ljust(20)} | {modelo_celular.ljust(20)} | {ativo}')
        
        retorna_menu()
    
    def ativar_celular():
        exibir_subtitulo("Ativar Celular")
        nome_celular = input("Digite o nome do Celular que você deseja ativar:")
        celular_encontrado = false

        for celular in celulares:
            if nome_celular == celular["nome"]:
                celular_encontrado = True
                celular["ativo"] = not celular["ativo"]
                mensagem = f"O Celular {nome_celular} foi ativado com sucesso." if celular["ativo"] else f"O Celular {nome_celular} foi desativado com sucesso."
                print(mensagem)

        if not celular_encontrado:
            print("Não encontrado")
        retorna_menu()
    
    def finalizar_app():
        exibir_subtitulo("Finalizando o programa\n")

    def opcao_invalida():
        print("Esse carácter não é permitido")

    retorna_menu()

    opcao_escolhida = int(input('Escolha uma opção:'))
    try:
        if opcao_escolhida == 1:
            cadastro_Celulares()
        elif opcao_escolhida == 2:
            listar_celulares()
        elif opcao_escolhida == 3:
            ativar_celular()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    mostra_titulo()
    mostra_escolhas()
    escolher_opcao()

if __name__ == "__main__":
    main()