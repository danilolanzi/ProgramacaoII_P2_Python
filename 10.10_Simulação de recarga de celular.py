'''Simule um crédito de telefone que começa em R$ 0,00.
O usuário insere valores de recarga até que o crédito atinja pelo menos R$ 20,00.
A cada recarga informe o saldo atual. Quando atingir um valor igual ou maior que R$ 20,00, 
exiba “Saldo mínimo atingido” e encerre.'''

saldo = 0.0

while saldo < 20.00:
    recarga = float(input("Digite o valor da recarga: R$ "))
    saldo += recarga
    print(f"Saldo atual: R$ {saldo:.2f}\n")

print("Saldo mínimo atingido!")