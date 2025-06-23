'''1.10. [Exercício] Armazene 5 números inteiros e mostre o menor valor.'''

numeros = []

# Coletando 5 livros
for numero in range(5):
    numero = float(input(f"Digite o preço {numero + 1}: "))
    numeros.append(numero)

# Encontrando o menor valor 
menor_numero = min(numeros)           # Retorna o maior valor


print(f"Menor numero: {menor_numero} ")
