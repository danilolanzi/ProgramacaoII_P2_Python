'''Avaliação de IMC (simplificada): Peça ao usuário seu IMC (Índice de Massa Corporal). 
Classifique-o conforme os seguintes intervalos:

Abaixo de 18.5: "Abaixo do peso"
Entre 18.5 e 24.9: "Peso normal"
25 ou mais: "Acima do peso" '''

imc = float(input("Informe seu IMC: "))

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
else:
    print("Acima do peso")