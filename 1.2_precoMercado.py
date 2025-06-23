'''Um supermercado deseja armazenar os preços de 4 produtos. 
Após o preenchimento, exiba apenas os preços maiores que R$10,00.'''

precos = []


for i in range(4):
    preco = float(input(f"Digite o preço do produto {i+1}: R$ "))
    precos.append(preco)


print("\nPreços maiores que R$10,00:")
for preco in precos:
    if preco > 10.00:
        print(f"R$ {preco:.2f}")