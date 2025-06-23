''' Calculadora de Área de Retângulo: 
Crie uma função que receba a base e a altura de um retângulo e retorne a área.'''


def calcular_area_retangulo(base, altura):
    return base * altura

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = calcular_area_retangulo(base, altura)
print(f"A área do retângulo é {area}.")
