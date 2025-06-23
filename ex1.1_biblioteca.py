'''Biblioteca silenciosa: Imagine que você trabalha em uma biblioteca. 
Sempre que um usuário digita um número maior que 50 decibéis, uma mensagem de alerta deve ser exibida. 
Para tanto, peça ao usuário que informe o nível de ruído em decibéis. 
Se o valor for maior que 50, exiba a mensagem: "Por favor, mantenha o silêncio! '''

nivel_ruido = float(input("Informe o nível de ruído em decibéis: "))

# Verifica se o valor é maior que 50
if nivel_ruido > 50:
    print("Por favor, mantenha o silêncio!")