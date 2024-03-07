name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo.\n"))
planIncluded = input("Está incluso no Gamepass?\n")

print("###Dados do Jogo###")
print("===================")
#Alternativa 1
# print("Nome do jogo:", name)
# print("Ano de lançamento:", yearLaunch)
# print("Preço:", gamePrice)
# print("Está Incluso na Gamepass?", planIncluded)
#Alternativa 2
# print("Nome do jogo:",name,"\nAno de lançamento:",yearLaunch,"\nPreço:",gamePrice,"Está inlcuso na Gamepass?",planIncluded)
# Alternativa 3
print(f"Nome do Jogo: {name}\nAno de lançamento: {yearLaunch}\nPreço: {gamePrice}\nEstá incluso na Gamepass? {planIncluded}")