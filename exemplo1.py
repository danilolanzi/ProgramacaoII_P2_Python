minhaMatriz = []

for i in range (2):
    linha = []
    for j in range(2):
        valor = int(input('valor: '))
        linha.append(valor)

minhaMatriz.append(linha)
for linha in minhaMatriz:
    print(linha)
