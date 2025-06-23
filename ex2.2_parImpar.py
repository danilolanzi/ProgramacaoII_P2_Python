''' Número par ou ímpar: Peça um número inteiro ao usuário e diga se ele é par ou ímpar.'''

numero = int(input("Informe um numero inteiro: "))

if numero % 2 == 0:
    print("Numero Par")
else:
    print("Numero Impar")