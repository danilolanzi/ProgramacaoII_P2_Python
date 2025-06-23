''' Um professor quer calcular a média das idades dos 6 alunos 
que participaram de uma aula. Solicite as idades e exiba a média.
'''

idades = []

for i in range(6):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    idades.append(idade)

#calculo da media
media = sum(idades) / len(idades)

# Exibição da média
print(f"\nA média das idades é: {media:.2f} anos")