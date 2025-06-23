'''Crie uma matriz 4x1 com números fornecidos pelo usuário 
e imprima seus elementos multiplicados por 2.'''

matriz = []

print("Digite os 4 valores da matriz 4x1:")
for i in range(4):
    valor = int(input(f"Valor para posição [{i}][0]: "))
    matriz.append([valor]) 


# Impressão dos elementos multiplicados por 2
print("\nElementos multiplicados por 2:")
for i in range(4):
    print(f"{matriz[i][0]} x 2 = {matriz[i][0] * 2}")