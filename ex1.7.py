''' Nome Completo: Crie uma função que receba o primeiro nome e 
o sobrenome e retorne o nome completo formatado.'''

def nome_completo(primeiro_nome, sobrenome):
    primeiro_nome = input("Qual é o seu nome? ")
    sobrenome = input("Qual é o seu sobrenome? ")
    print("Seu nome e sobrenmome é,", primeiro_nome, sobrenome)

nome_completo("primeiro_nome", "sobrenome")