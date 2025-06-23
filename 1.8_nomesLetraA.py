'''.8. Peça 4 nomes de alunos e
exiba apenas os nomes que começam com a letra “A”.'''

alunos = []


for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)

print("Nomes que começam com a letra 'A':")
for nome in alunos:
    if nome.upper().startswith("A"):
        print(nome)