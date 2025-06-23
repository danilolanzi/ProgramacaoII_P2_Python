'''1.5. Uma livraria quer registrar os preços de 5 livros. 
Depois, exiba o maior valor registrado.'''


livros = []

# Coletando 5 livros
for livro in range(6):
    livro = float(input(f"Digite o preço {livro + 1}: "))
    livros.append(livro)

# Encontrando o maior valor 
maior_preco = max(livros)           # Retorna o maior valor


# Exibindo os resultados
print(f"Maior preco: {maior_preco} ")
