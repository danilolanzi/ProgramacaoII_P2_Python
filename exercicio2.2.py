''' Leia uma matriz 2x2 e calcule a soma de todos os seus elementos.'''

minhaMatriz = []
soma = 0

print("Digite os valores da matriz 2x2:")
for i in range (2):
    linha = []
    for j in range(2):
        valor = int(input('valor: '))
        linha.append(valor)
        soma += valor   
    minhaMatriz.append(linha)

    
for linha in minhaMatriz:
    print(linha)

print(soma)

