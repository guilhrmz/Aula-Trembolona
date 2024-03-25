print("--------------------------")
print("         Salario          ")
print("--------------------------")

def calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_desconto):
    salario_bruto = valor_hora_aula * horas_trabalhadas
    desconto = salario_bruto * (percentual_desconto / 100)
    salario_liquido = salario_bruto - desconto
    return salario_bruto, salario_liquido

def main():
    valor_hora_aula = float(input("Digite o valor da hora-aula: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    percentual_desconto = float(input("Digite o percentual de desconto do INSS: "))

    salario_bruto, salario_liquido = calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_desconto)

    print("\nSalário Bruto: R$", salario_bruto)
    print("Salário Líquido: R$", salario_liquido)

if __name__ == "__main__":
    main()