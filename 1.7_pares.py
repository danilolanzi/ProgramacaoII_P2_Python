''' 1.7. Solicite 5 números ao 
usuário e mostre quantos deles são pares.'''

numeros = []


for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Contador de números pares
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1

# Exibição do resultado
print(f"\nQuantidade de números pares: {pares}")

