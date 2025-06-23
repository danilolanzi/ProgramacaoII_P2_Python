'''Programa para controlar quantidade de agua ingirida em um dia'''

total_agua = 0

print("Meta: beber 2000 ml de água por dia.\n")

while total_agua < 2000:
    quantidade = int(input("Digite a quantidade de água ingerida (em ml): "))
    
    if quantidade > 0:
        total_agua += quantidade
        print(f"Total ingerido: {total_agua} ml\n")
    else:
        print("Quantidade inválida. Digite um valor positivo.\n")

print("Meta de hidratação atingida!")