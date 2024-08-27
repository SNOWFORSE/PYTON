import os

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


    

    def finalizar_programa():
        os.system("cls")
        print("Finalizando o Programa\n")

    def opcao_invalida():
        print("Esse carácter não é permitido")
        input("Aperte qualquer tecla para voltar")
        
def escolhe_opcao():       
    try:
        opcao_escolhida = int(input('Escolha um opção:'))

        if opcao_escolhida == 1:
            print("Você escolheu Cadastrar Celulares")
        elif opcao_escolhida == 2:
            print("Você escolheu Listar Celulares")
        elif opcao_escolhida == 3:
            print("Você escolheu Ativar Matricula")
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()

def main():
    os.system("cls")
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()