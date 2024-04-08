import time
import random

print("---------------------")
print("       JOKENPO       ")
print("---------------------")

print("Vamos jogar Jokenpo?")

time.sleep(1)

print("Regras:")

time.sleep(1)

print("Tesoura corta papel\nPapel cobre pedra\nPedra esmaga lagarto\nLagarto envenena Spock\nSpock esmaga (ou derrete) tesoura\nTesoura decapita lagarto\nLagarto come papel\nPapel refuta Spock\n○ Spock vaporiza pedra\n○ Pedra amassa tesoura")

Start = int(input("Vamos Jogar? \n1-Sim \n "))




def Jogar():
    time.sleep(1)





def resultado(Jogada, JogadaPC):
    resultados = {
        (1, 1): "Você empatou!",
        (1, 2): "Você perdeu!",
        (1, 3): "Você ganhou!",
        (1, 4): "Você ganhou!",
        (1, 5): "Você perdeu!",
        (2, 1): "Você ganhou!",
        (2, 2): "Você empatou!",
        (2, 3): "Você perdeu!",
        (2, 4): "Você perdeu!",
        (2, 5): "Você ganhou!",
        (3, 1): "Você perdeu!",
        (3, 2): "Você ganhou!",
        (3, 3): "Você empatou!",
        (3, 4): "Você ganhou!",
        (3, 5): "Você perdeu!",
        (4, 1): "Você perdeu!",
        (4, 2): "Você ganhou!",
        (4, 3): "Você perdeu!",
        (4, 4): "Você empatou!",
        (4, 5): "Você perdeu!",
        (5, 1): "Você ganhou!",
        (5, 2): "Você perdeu!",
        (5, 3): "Você ganhou!",
        (5, 4): "Você perdeu!",
        (5, 5): "Você empatou!"
    }
    resultado_jogo = resultados.get((Jogada, JogadaPC), "Jogada inválida!")
    print(f"O PC jogou {JogadaPC}")
    print(f"Voce jogou {Jogada}")
    print(resultado_jogo)
    return resultado_jogo




if Start == 1:
    Jogar()
    Jogada = int(input("Qual é sua Jogada?\n1-Pedra (Rock)\n2-Papel (Paper)\n3-Tesoura (Scissors)\n4-Lagarto (Lizard)\n5-Spock (Spock)?\n"))
    JogadaPC = random.randrange(0, 6)
    resultado(Jogada, JogadaPC)