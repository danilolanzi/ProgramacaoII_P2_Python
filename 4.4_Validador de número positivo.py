'''4. Validador de número positivo: O programa deve pedir ao usuário 
que digite um número positivo. Caso o número informado seja negativo,
 o programa deve pedir novamente, até que o usuário informe um valor válido. 
 Quando isso acontecer, exiba: "Valor aceito: X"
'''

numero = int(input("Digite um número positivo: "))

while numero < 0:
    print("Valor inválido. Tente novamente.")
    numero = int(input("Digite um número positivo: "))

print(f"Valor aceito: {numero}")