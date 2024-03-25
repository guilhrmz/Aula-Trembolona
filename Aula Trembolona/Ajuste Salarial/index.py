print("--------------------------")
print("     Ajuste Salarial      ")
print("--------------------------")

print("Seu salario é de R$ 1.412")
Porcentagem = int(input("Qual é o percentual de aumento salarial? (Não use %): "))
SalarioMin = int(1412)
SalarioNew = int((100 + Porcentagem) / 100 * 1412)
print(f"Seu novo salario é {SalarioNew}")