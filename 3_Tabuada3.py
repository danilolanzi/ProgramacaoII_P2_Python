'''Crie um programa que exiba a tabuada do número 3, do 1 ao 10. 
O formato da resposta deve seguir o padrão: 3 x 1 = 3, 3 x 2 = 6, e assim por diante.'''

for i in range(1, 11):
    resultado = 3 * i
    print(f"3 x {i} = {resultado}")