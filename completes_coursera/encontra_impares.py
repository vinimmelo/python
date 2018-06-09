listab = []
def encontra_impares(lista):
    if len(lista)<=1:
        if lista[0]%2==1:
            listab.append(lista[0])
            return listab
        else:
            return listab
    else:
        if lista[0]%2==1:
            listab.append(lista[0])
            return encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])
