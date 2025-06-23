print("Bem-vindo ao mundo da energia Solar!")
valor = float(input("Digite o valor da conta de energia: R$ "))

for i in range(300, 600):
    if valor == i:
        print("Precisa de placa solar! Seu projeto vai ficar entre R$10.000 e R$16.000")
        break
for i in range(600, 1001):
    if valor == i:
        print("Precisa de placa solar! Seu projeto vai ficar entre R$17.000 e R$22.000")
        break
if valor < 300 or valor > 1000:
    print("Entre em contato para mais informações.")