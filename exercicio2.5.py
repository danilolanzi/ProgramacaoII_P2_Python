'''Leia uma matriz 2x3, conte e mostre separadamente quantos 
elementos são par e quantos elementos são impar.'''

matriz = []
pares = 0
impares = 0

# Leitura da matriz 2x3
print("Digite os valores da matriz 2x3:")
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor para posição [{i}][{j}]: "))
        linha.append(valor)
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    matriz.append(linha)

# Exibe a matriz
print("\nMatriz 2x3:")
for linha in matriz:
    print(linha)

# Exibe os resultados
print("\nQuantidade de elementos pares:", pares)
print("Quantidade de elementos ímpares:", impares)