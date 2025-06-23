'''Conversor de Temperatura: Crie uma função que receba uma temperatura em 
Celsius e retorne a temperatura em Fahrenheit. Para tanto,
use a fórmula: (Celsius * 9/5) + 32'''

def temperatura(celsius):
    return (celsius * 9/5) + 3

valor = float(input("Digite a temparatura em graus Celsius: "))
resultado = temperatura(valor)
print(f"A temperaura {valor} é {resultado} em Fahrenheit .")