import os
import Twofer 

caminho_pasta = './Twofer'

def main_menu():
    print("Bem-vindo ao Menu de Programas:")
    print("1. ajuste-salarial")
    print("2. algarismo")
    print("3. circuferencia")
    print("4. conversao")
    print("5. converter-dolar")
    print("6. eleicao")
    print("7. fizz-buz")
    print("8. jokenpo")
    print("9. media")
    print("10. ordenados")
    print("11. palidromo")
    print("12. Pedra-papel-tesoura-lagarto-Spock")
    print("13. projetil")
    print("14. quadrado-soma")
    print("15. quadrados")
    print("16. salario")
    print("17. somando")
    print("18. troca-troca")
    print("19. Twofer")
    print("20. volume")
    print("0. Sair")

def main():
    
    os.chdir(caminho_pasta)

    while True:
        main_menu()
        opcao = input("Escolha uma opção (1-20) ou 0 para sair: ")

        if opcao == '1':
            
            pass
        elif opcao == '2':
            
            pass
        elif opcao == '3':
        
            pass
    
        elif opcao == '0':
            print("Obrigado por utilizar o Menu de Programas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()