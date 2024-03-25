print("--------------------------")
print("         Volume           ")
print("--------------------------")

def calcular_volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

def main():
    comprimento = float(input("Digite o valor do comprimento da caixa retangular: "))
    largura = float(input("Digite o valor da largura da caixa retangular: "))
    altura = float(input("Digite o valor da altura da caixa retangular: "))

    volume = calcular_volume(comprimento, largura, altura)

    print("\nO volume da caixa retangular é:", volume)

if __name__ == "__main__":
    main()