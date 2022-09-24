from forca import forca
from advinhacao import adivinhar


print("*********************************")
print("*******Escolhao seu jogo!********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    forca()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhar()