variavel = 0
numero = int(input("Digite o número decimal à ser convertido: "))

lista_marota = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def hexa(numero):
    hexadecimal = []
    if numero<=0:
        print("Você digitou o número: ", numero)
    else:
        while not numero == 0:
            variavel = divmod(numero, 16)
            hexadecimal.insert(0,lista_marota[variavel[1]])
            numero = variavel[0]
    hexadecimal = str(hexadecimal)
    return print("O valor hexadecimal é: ", hexadecimal.replace(',',""))
   

def bina(numero):
    binario = []
    if numero<=0:
        print("Você digitou o número: ", numero)
    else:
        while not numero == 0:
            variavel = divmod(numero, 2)
            binario.insert(0, variavel[1])
            numero = variavel[0]
    binario = str(binario)
    return print("O valor binário é: ", binario.replace(',',""))

def octal(numero):
    octogonal = []
    if numero<=0:
        print("Você digitou algo errado: ", numero)
    else:
        while not numero==0:
            variavel = divmod(numero, 8)
            octogonal.insert(0, variavel[1])
            numero = variavel[0]
    octogonal = str(octogonal)
    return print("O valor de base octal é: ", octogonal.replace(',',""))        


def tri(numero):
    ternario = []
    if numero<=0:
        print("Você digitou algo errado: ", numero)
    else:
        while not numero==0:
            variavel = divmod(numero, 3)
            ternario.insert(0, variavel[1])
            numero = variavel[0]
    ternario = str(ternario)
    return print("O valor de base ternária é: ", ternario.replace(',',""))

hexa(numero)
octal(numero)
tri(numero)
bina(numero)
print("Fim do trabalho")
                      


                 
                     
