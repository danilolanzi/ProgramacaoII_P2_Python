''' Leia uma matriz 2x3 e conte quantos elementos são maiores que 10.'''

matriz = []
contador = 0

# Leitura da matriz 2x3
print("Digite os valores da matriz 2x3:")
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor para posição [{i}][{j}]: "))
        linha.append(valor)
        if valor > 10:
            contador += 1
    matriz.append(linha)

# Exibe a matriz
print("\nMatriz 2x3:")
for linha in matriz:
    print(linha)

# Exibe a quantidade de elementos maiores que 10
print("\nQuantidade de elementos maiores que 10:", contador)