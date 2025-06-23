'''Números múltiplos de 2 e 3 simultaneamente entre 1 e 20. Faça um programa que exiba 
todos os números múltiplos de 2 e 3 simultaneamento entre 1 e 20.'''


print("Os numeros multiplos de 2 e 3 no intervalo de 1 a 20 são: ")
for i in range(1, 21):
    if i % 2 == 0 and i % 3 == 0:
        print(i)