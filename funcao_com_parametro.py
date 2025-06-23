'''Calcula o valor do frete estimado para importação da China,
    baseado no peso da mercadoria.'''

def calcular_frete_importacao(peso):
    return peso * 5

peso = float(input("Digite o peso em quilos: "))
frete = calcular_frete_importacao(peso)

print(f"O frete estimado é de {frete} dólares.")
