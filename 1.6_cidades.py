'''1.6. Crie uma lista com o nome de 3 cidades
 e depois mostre os nomes em ordem inversa à digitada.'''

cidades = []

for i in range(3):
    nome = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(nome)
    
print("\nCidades em ordem inversa:")
for cidade in reversed(cidades):
    print(cidade)