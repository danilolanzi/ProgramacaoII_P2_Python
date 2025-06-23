'''Verificação de trânsito: Um motorista precisa verificar se está acima do limite de velocidade de 80 km/h. 
Peça a velocidade atual e exiba "Multa por excesso de velocidade" se for maior que 80,
ou "Velocidade dentro do permitido" caso contrário.'''

velocidade = float(input("Informe a velocidade atual (em km/h): "))

# Verifica se está acima do limite
if velocidade > 80:
    print("Multa por excesso de velocidade")
else:
    print("Velocidade dentro do permitido")