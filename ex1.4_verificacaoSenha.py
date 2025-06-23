'''Verificação de senha: Em um sistema de login, a senha correta é “12345”. 
Peça que o usuário digite a senha. 
Se a senha estiver correta, mostre: "Acesso autorizado."'''


senha_correta = "12345"

senha_digitada = input("Digite a senha: ")

if senha_digitada == senha_correta:
    print("Acesso autorizado.")