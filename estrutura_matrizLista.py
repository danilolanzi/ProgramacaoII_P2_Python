matriz = []

print("Digite os valores para a matriz 2x2:")

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibe a matriz
print("Matriz digitada:")
for linha in matriz:
    print(linha)

# Soma dos elementos
soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento

print(f"Soma de todos os elementos: {soma}")