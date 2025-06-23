''' Imagine que você está guardando moedas em um cofrinho. 
A cada vez que você adiciona uma moeda, o valor total aumenta. 
O programa deve continuar perguntando o valor das moedas depositadas 
até que o total ultrapasse R$ 10,00. Ao final, exiba: 
"Meta atingida! Você já tem R$ XX,XX no cofrinho."
'''

total = 0.0

while total <= 10.00:
    moeda = float(input("Digite o valor da moeda depositada (ex: 0.25): R$ "))
    total += moeda

print(f"\nMeta atingida! Você já tem R$ {total:.2f} no cofrinho.")
