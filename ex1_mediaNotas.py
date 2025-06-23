'''Crie um programa em Python que:

Peça ao usuário que digite 4 notas (valores float) e armazene essas notas em um vetor.
Calcule a média das notas.
Imprima a média e uma mensagem:
    Se a média for maior ou igual a 7.0: "Aprovado"
    Caso contrário: "Reprovado"
'''

# Criando um vetor vazio para armazenar as notas
notas = []

# Coletando 4 notas com estrutura de repetição
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)  # Adiciona a nota ao vetor

# Calculando a média das notas
media = sum(notas) / len(notas)

# Exibindo a média
print(f"Média: {media:.2f}")

# Verificando a situação
if media >= 7.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")