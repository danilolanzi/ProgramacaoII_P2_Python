'''Crie um jogo simples em que o programa “pensa” em um número secreto (por exemplo, 7) 
e o usuário tenta adivinhar. Enquanto o palpite estiver errado,
peça novo chute. Ao acertar, parabenize o jogador.
Dica: dê um import random, e use o método random.randint(1, 10)
para gerar um número aleatório entre 1 e 10, por exemplo.
'''

import random

# Gerador de número secreto aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

print("Tente adivinhar o número secreto entre 1 e 10!")

palpite = int(input("Digite seu palpite: "))

while palpite != numero_secreto:
    print("Errado! Tente novamente.")
    palpite = int(input("Digite seu palpite: "))

print(f"Parabéns! Você acertou, o número era {numero_secreto}.")