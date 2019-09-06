# Gere um número random entre 1 e 100 (incluindo o 100),
# pergunte ao usuário que adivinhe o número, então diga
# a ele se ele chutou muito baixo, muito alto ou exatamente certo.

# - Mantenha o jogo rodando até que o usuário digite "sair"
# - Matenha a contagem de quantas vezes o usuario tentou acertar
# até que ele consiga acertar, então printe a quantida de vezes
# após o fim do jogo
import random


def main():
    numero_randomico = random.randrange(1, 101)
    contador = 0
    while True:
        numero_escolhido = input("Escolha um número entre 1 e 100, ou digite sair: ")
        contador += 1
        if numero_escolhido == 'sair':
            exit()
        if int(numero_escolhido) == numero_randomico:
            print(f'Você digitou {contador} até acertar!')
            print("certo")
            break
        elif int(numero_escolhido) > numero_randomico:
            print("numero deve ser menor")
        else:
            print("numero deve ser maior")


if __name__ == '__main__':
    print('Estou rodando')
    main()
