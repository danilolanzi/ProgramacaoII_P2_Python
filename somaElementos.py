'''Função que soma elementos de uma lista'''

def somar_lista(lista):
    total = 0
    for item in lista:
        total += item
    return total

'''Uso:'''

valores = [2, 3, 5]
print("Soma:", somar_lista(valores))
