'''Calculadora de média até negativo: Você quer calcular a média de várias notas de aluno,
 mas não sabe quantas ainda vai receber. Faça um programa que peça notas
 (valores entre 0 e 10) ao usuário repetidamente, até que ele digite um valor negativo. 
 Ao final, mostre a média de todas as notas, sem considerar o valor negativo.
'''

soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota entre 0 e 10 (ou um valor negativo para sair): "))
    
    if nota < 0:
        break

    if 0 <= nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")

if quantidade > 0:
    media = soma / quantidade
    print(f"\nMédia das {quantidade} notas: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")