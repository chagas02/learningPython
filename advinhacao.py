import random

def adivinhar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontos = 1000


    print("qual nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")
    nivel = int(input("Defina o nível do jogo: "))

    if nivel == 1:
        numero_de_tentativas = 10
    elif nivel == 2:
        numero_de_tentativas = 5
    else:
        numero_de_tentativas = 3


    for rodado in range(1, numero_de_tentativas + 1):
        print("Tentativa: {} de {}".format(rodado, numero_de_tentativas))
        chute = int(input("Digite o seu número: "))
        print("Você digitou  ", chute)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("você errou! o seu chute foi maior do que o número secreto")
                if(rodado == numero_de_tentativas):
                    print("o número secreto era {}. você fez {} pontos.".format(numero_secreto, pontos))
            elif(menor):
                print("você errou! o seu chute foi menor do que o número secreto")
                if (rodado == numero_de_tentativas):
                    print("o número secreto era {}. você fez {} pontos.".format(numero_secreto, pontos))


    print("Fim do jogo")

if(__name__ == "__main__"):
    adivinhar()