'''Temperatura segura: Você está monitorando a temperatura de uma estufa.
Para segurança das plantas, a temperatura não deve ultrapassar 30 °C.
Dessa forma, peça ao usuário a temperatura atual.
Se ela for maior que 30, exiba: "Alerta: temperatura acima do permitido!".'''

temperatura = float(input("Informe a temperatura atual da estufa (em °C): "))

if temperatura > 30:
    print("Alerta: temperatura acima do permitido!")