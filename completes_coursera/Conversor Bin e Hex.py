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
        print("O valor binário é: ", binario.replace(',',""))
        
        
    
hexa(numero)
bina(numero)
print("Fim do trabalho!!!")
