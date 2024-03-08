'''
1 - Escreva um programa em Python que leia um número e represente o número antecessor e sucessor do número lido utilizando operadores de atribuição.
2 - Escreva um programa em Python que leia quatro números e calcule a média entre estes numeros.
'''

# 1
num1 = int(input("Digite um número:\n"))
print(f"O número antecessor de {num1} é {num1 - 1}\nO sucessor de {num1} é {num1 + 1}.")

# 2
num1 = float(input("Digite o primeiro valor\n"))
num2 = float(input("Digite o segundo valor\n"))
num3 = float(input("Digite o terceiro valor\n"))
num4 = float(input("Digite o quarto valor\n"))

media = (num1+num2+num3+num4)/4
print(f"A média dos valores digitados é: {media}")