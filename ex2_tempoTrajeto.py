'''Peça ao usuário que digite 5 tempos de trajeto (em minutos), armazenando-os em um vetor.
Ao final, mostre:
O maior tempo informado.
A posição (índice) do maior valor no vetor.'''

'''Criando o vetor para armazenar os tempos'''
tempos = []

# Coletando 5 tempos de trajeto
for i in range(5):
    tempo = int(input(f"Digite o tempo {i + 1}: "))
    tempos.append(tempo)

# Encontrando o maior valor e seu índice
maior_tempo = max(tempos)           # Retorna o maior valor
indice_maior = tempos.index(maior_tempo)  # Retorna o índice do maior valor

# Exibindo os resultados
print(f"Maior tempo: {maior_tempo} minutos")
print(f"Índice: {indice_maior}")

