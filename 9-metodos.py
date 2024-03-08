"""Retorna o texto em maiusculo `print(texto.upper())`

Retorna o texto todo minusculo `print(texto.lower())`

Retorna primeira letra `print(texto.capitalize())` ou `print(texto.title())`

Retornar string centralizada `(print(texto.center())` podemos informar a quantidade de caracteres que queremos a frase final e qual caractere utilizar para preencher  `(print(texto.center(10, "-"))"""
texto = "batatinha"

print(texto.center(len(texto) + 18, "-"))
print(texto.capitalize())
print(texto.lower())
print(texto.upper())