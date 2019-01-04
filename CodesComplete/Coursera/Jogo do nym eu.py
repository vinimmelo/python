"""
@author: vinimmelo

NIM Game
Based on the course: [Introdução a ciência da computação - Coursera]
>>> website link Part 1: https://pt.coursera.org/learn/ciencia-computacao-python-conceitos
>>> website link Part 2: https://pt.coursera.org/learn/ciencia-computacao-python-conceitos-2
"""

computador = 0
usuario = 0
rodada = 0
r = 0
n = 1
m = 1

def computador_escolhe_jogada(n, m):
        r=0
        while 1>=0:
                if n%(m+1)==0:
                        print("Agora restam ", n-m, " peças no tabuleiro.")
                        return m
                        break
                else:
                        print("Agora restam ", n-(n%(m+1)), " peças no tabuleiro.")
                        return n%(m+1)




def usuario_escolhe_jogada(n, m):
        usuario=0
        while 1>0:

                r = int(input("Quantas peças você vai tirar? "))
                if r<=m and r>0:
                        print("Agora restam ", n-r, " peças no tabuleiro.")
                        return r
                        break
                else:
                        usuario= 1+usuario
                        print("Oops! Jogada inválida! Tente de novo")


def partida():
	while 1>0:
		n = int(input("Quantas peças? "))
		if n>0:
			break
		else:
			print("Oops, tente novamente!")

	while 1>0:
		m = int(input("Limite de peças por jogada? "))
		if m>0 and m<=n:
			break
		else:
			print("Oops, tente novamente!")
	if n%(m+1)==0:
		print("Você começa!")
		while n>0:
			usuario = usuario_escolhe_jogada(n,m)
			print("Você tirou", usuario, "peças.")
			n = (n-usuario)
			computador = computador_escolhe_jogada(n,m)
			print("O computador tirou", computador, "peças")
			n = (n-computador)
			if n==0:
				print("Fim de jogo! O Computador ganhou!")
				break
	else:
		print("Computador começa!")
		while n>0:
			computador = computador_escolhe_jogada(n,m)
			print("O computador tirou", computador, "peças")
			n = (n - computador)
			if n==0:
				print("Fim de jogo! O computador ganhou!")
				break
			else:
				usuario = usuario_escolhe_jogada(n,m)
				print("Você tirou", usuario, "peças.",)
				n = n-usuario


def campeonato():
	print("**** Rodada 1 ****")
	partida()
	print("**** Rodada 2 ****")
	partida()
	print("**** Rodada 3 ****")
	partida()
	print("**** Final do Campeonato! ****")
	print("Placar: Você 0 x 3 Computador")



print("Bem-vindo ao jogo do NIM! Escolha:")


while computador>=0:
		print("1 - para jogar uma partida isolada ")
		tipo_jogo = int(input("2 - para jogar um campeonato "))
		if tipo_jogo==1:
			print("Você escolheu uma partida isolada.")
			partida()
			print("Final do jogo, você perdeu!!!")
			break
		elif tipo_jogo==2:
			print("Você escolheu um campeonato! ")
			campeonato()
			break
		else:
			print("Escolha apenas entre 1 ou 2")
