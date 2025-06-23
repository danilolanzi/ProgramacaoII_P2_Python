'''Elevador com limite de peso: Imagine que um elevador suporta até 500 kg. 
Peça ao usuário que informe o peso total atual no elevador. 
Se o peso ultrapassar o limite, exiba: "Peso excedido! Não é seguro subir."
'''

limite = float(input("Informe o valor total em KG a ser colocado no elevador: "))

if limite > 500:
    print("Peso excedido! Não é seguro subir.")
