'''Programa que mostra o seguinte padrão de saída:

1 2 3 PIM 5 6 7 PIM 9 10 11 PIM 13 14 15 PIM 17 18 19 PIM
'''


for i in range(1, 21):
    if i % 4 == 0:
        print("PIM", end=' ')
    else:
        print(i, end=' ')