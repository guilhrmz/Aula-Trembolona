print("---------------------")
print("    CIRCUFERENCIA    ")
print("---------------------")

pi = 3.14159265

def calcular_area(raio):
    area = pi * (raio ** 2)
    return area

raio = float(input('Digite o raio da circunferência: '))

area_calculada = calcular_area(raio)

print('A área da circunferência é:', area_calculada)

