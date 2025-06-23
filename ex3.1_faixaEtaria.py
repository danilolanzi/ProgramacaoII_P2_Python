'''Classificação por faixa etária: Um sistema de saúde classifica as pessoas conforme sua idade.
Sendo assim, solicite a idade de uma pessoa e classifique-a como:

"Criança" se tiver até 12 anos
"Adolescente" entre 13 e 17
"Adulto" a partir de 18 anos '''

idade = int(input("Informe a sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")