numeros = []

print("Digite 5 números:")

for i in range(5):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

print("Dobro de cada número:")
for num in numeros:
    print(num * 2)