'''Sistema de notas com conceito: Solicite uma nota de 0 a 10 e classifique o conceito do aluno:

9 a 10: "Conceito A"
7 a 8.9: "Conceito B"
5 a 6.9: "Conceito C"
Abaixo de 5: "Conceito D" '''

nota = float(input("Informe a nota do aluno (de 0 a 10): "))

if nota >= 9 and nota <= 10:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")

