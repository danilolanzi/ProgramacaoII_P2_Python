'''Verificação de Número Par: Crie uma função que receba um número e retorne 
True se ele for par, ou False caso contrário.'''

def num_par(numero):
    return numero % 2 == 0

valor = int(input("Digite um número: "))
if num_par(valor):
    print(f"{valor} é par!")
else:
    print(f"{valor} é impar!")
