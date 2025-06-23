'''Maior de Dois Números: Crie uma função que 
receba dois números e retorne o maior deles.'''

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("O maior número é:", maior_numero(num1, num2))