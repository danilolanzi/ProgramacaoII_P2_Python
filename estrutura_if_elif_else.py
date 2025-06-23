print("Bem vindo ao mundo da energia Solar!")
valor = float(input("Digite o valor da conta de energia: R$ "))

if valor >= 300 and valor < 600:
    print("Precisa de placa solar! Seu projeto vai ficar entre R$10.000 e R$16.000")
elif valor >= 600 and valor <= 1000:
    print("Precisa de placa solar! Seu projeto vai ficar entre R$17.000 e R$22.000")
else:
    print("Entre em contato para mais informações.")
