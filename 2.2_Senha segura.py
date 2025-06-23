''' Senha segura: Você precisa criar um sistema de acesso com verificação de senha.
 O programa deve pedir ao usuário que digite a senha até que ela esteja correta.
   A senha correta é "segredo123". Quando o usuário acertar, exiba: "Bem-vindo ao sistema!"
'''

while True:
    senha = input("Digite a senha: ")
    if senha == "segredo123":
        print("Bem-vindo ao sistema!")
        break
    else:
        print("Senha incorreta, tente novamente.\n")