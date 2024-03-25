import time

print("--------------------------")
print("       Troca Troca        ")
print("--------------------------")

Numero_A = input("Digite qualquer coisa para o valor A: ")
Numero_B = input("Digite qualquer coisa para o valor B: ")

time.sleep(1)

print(f"Numero A = {Numero_A}, Numero B = {Numero_B}")

time.sleep(1)

print("Trocando Valores...")

time.sleep(2)

Numero_C = Numero_A

Numero_A = Numero_B 

Numero_B = Numero_C 

print(f"Numero A = {Numero_A}, Numero B = {Numero_B}")