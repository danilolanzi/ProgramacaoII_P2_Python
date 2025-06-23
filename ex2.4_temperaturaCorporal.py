''''Verificação de temperatura corporal: Peça ao usuário que informe sua temperatura corporal. 
Se for maior ou igual a 37.5, exiba "Possível febre"; caso contrário, "Temperatura normal".'''

temperatura = float(input("Informe sua temperatura corporal (em °C): "))

# Verifica se há possível febre
if temperatura >= 37.5:
    print("Possível febre")
else:
    print("Temperatura normal")