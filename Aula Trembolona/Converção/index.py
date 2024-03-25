print("--------------------------")
print("         Convertor        ")
print("--------------------------")

def converter_dolar_para_real(cotacao_dolar, quantidade_dolar):
    valor_em_real = cotacao_dolar * quantidade_dolar
    return valor_em_real

def main():
    cotacao_dolar = float(input("Digite a cotação do dólar (em reais): "))
    quantidade_dolar = float(input("Digite a quantidade de dólares que você possui: "))

    valor_em_real = converter_dolar_para_real(cotacao_dolar, quantidade_dolar)

    print("\nO valor em reais é: R$", valor_em_real)

if __name__ == "__main__":
    main()