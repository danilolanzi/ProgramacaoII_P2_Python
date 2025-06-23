notas = []

# Coleta das 5 notas do usuário
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

# Exibição das notas digitadas
print("\nNotas digitadas:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {nota}")