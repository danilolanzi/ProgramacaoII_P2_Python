'''Leia uma matriz 3x3 com valores inteiros e imprima todos os elementos.'''

minhaMatriz = []

for i in range (3):
    linha = []
    for j in range(3):
        valor = int(input('valor: '))
        linha.append(valor)
    minhaMatriz.append(linha)

    
for linha in minhaMatriz:
    print(linha)