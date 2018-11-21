# Created on 21 November 2018
# @author vinimmelo
# Jogo da forca.

from random import randint


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    with open('palavras.txt', 'r') as arquivo:
        palavras = [x.upper().strip() for x in arquivo]
        palavra_secreta = palavras[randint(0, len(palavras) - 1)]

    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1
            print(f"Errou.. faltam mais {6 - erros} tentativas!")
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (enforcou):
        print("Você perdeu... a palavra secreta era: " + palavra_secreta)
    else:
        print("Você ganhou!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
