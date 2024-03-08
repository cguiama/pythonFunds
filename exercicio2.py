"""
## Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

ex:
fifa 23 → **fi#a 23**
restart→ resta#t

## Substituindo caractere repetido
Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

ex: abc xyz → **xyc abz**
"""
# Ex 1
# text = input("Digite uma palavra\n")
# minusc = text[0].lower()
# firstLetter = minusc
# frase = text[1:]
# print(firstLetter+frase.replace(firstLetter, "$"))

#Ex 2
frase1 = input("Digite a primeira frase:\n")
frase2 = input("Digite a segunda frase:\n")

initFrase1 = frase1[:2]
initFrase2 = frase2[:2]


print(frase1 +" "+ frase2)
# print(initFrase2+frase1[2:])
# print(initFrase1+frase2[2:])
print(frase1.replace(frase1[:2],frase2[:2])+" "+frase2.replace(frase2[:2],frase1[:2]))