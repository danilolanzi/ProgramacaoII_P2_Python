'''Crie uma proposta original de programa que utilize a estrutura de repetição for.
Pense em uma situação diferente das que já foram trabalhadas anteriormente e elabore um pequeno programa que faça uso do laço for.
Na sua resposta, apresente uma breve descrição do que o programa faz e, em seguida, mostre a implementação do código.
'''

total_litros = 0

print("Registro de abastecimento dos 7 veículos:\n")

for i in range(1, 8):
    litros = float(input(f"Digite a quantidade de litros abastecidos no veículo {i}: "))
    total_litros += litros
    print(f"Veículo {i}: {litros:.2f} litros abastecidos.\n")

media = total_litros / 7

print(f"Total de litros abastecidos no dia: {total_litros:.2f}")
print(f"Média de litros por veículo: {media:.2f}")
