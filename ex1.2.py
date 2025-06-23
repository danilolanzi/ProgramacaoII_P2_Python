'''Dobro de um Número: Crie uma função que receba
 um número e retorne o dobro dele.'''

def dobro(numero):
    return numero * 2

valor = int(input("Digite um número: "))
resultado = dobro(valor)
print(f"O dobro de {valor} é {resultado}.")