import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #devolve uma lista de textos até apertar enter
    i = 1
    textos = []
    texto = str(input("Digite o texto " + str(i) +" (aperte enter para sair):"))
    while texto:
        textos.append(texto)
        i += 1
        texto = str(input("Digite o texto " + str(i) +" (aperte enter para sair):"))

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
    
    

def wal_txt(textos):
    sent = []
    fras = []
    pala = []

    total_palavras = 0
    tam = 0
    sent = separa_sentencas(textos)
    for y in sent:
      fras = separa_frases(y)
      for z in fras:
        pala = separa_palavras(z)
        for pal in pala:
          tam = tam + tam_med(pal)
          total_palavras += 1
    tamanhos_medios = tam/total_palavras
    
    return tamanhos_medios

def sal_txt(textos):
  fras = []
  pala = []
  

  tamanho_sentenca = 0
  sent = separa_sentencas(textos)
  numero_x = 0
  for y in sent:
    numero_x +=1
    fras = separa_frases(y)
    for z in fras:
      pala = separa_palavras(z)
      for pal in pala:
        tamanho_sentenca += len(pal)
  tamanho = tamanho_sentenca/numero_x
  
  return tamanho

def pal_txt(textos):
  fras = []
  pala = []
  
  caract = 0
  sent = separa_sentencas(textos)
  numero_x = 0
  for y in sent:
    fras = separa_frases(y)
    for z in fras:
      numero_x +=1
      pala = separa_palavras(z)
      for k in pala:
        caract = len(k) + caract
        
  tmdf = caract/numero_x
  return tmdf

def sac_txt(textos):
  fras = []
  sentenca = 0
  frase = 0
  sent = separa_sentencas(textos)
  for y in sent:
    sentenca += 1
    fras = separa_frases(y)
    frase = len(fras) + frase
  compds = frase/sentenca
  return compds
  
def ttr_txt(textos):
    sent = []
    fras = []
    pala = []
    
    lista_pal = []
    total_palavras = 0
    diferentes = 0
    sent = separa_sentencas(textos)
    for y in sent:
      fras = separa_frases(y)
      for z in fras:
        pala = separa_palavras(z)
        for pal in pala:
          total_palavras += 1
          lista_pal.append(pal)
    diferentes = n_palavras_diferentes(lista_pal)
    rtoken = diferentes/total_palavras
      
    return rtoken  

def hlr_txt(textos):
  sent = []
  fras = []
  pala = []
  lista_pal = []
  total_palavras = 0
  unicas = 0
  sent = separa_sentencas(textos)
  for y in sent:
    fras = separa_frases(y)
    for z in fras:
      pala = separa_palavras(z)
      for pal in pala:
        total_palavras += 1
        lista_pal.append(pal)
  unicas = n_palavras_unicas(lista_pal)
  rlegomana = unicas/total_palavras
  return rlegomana
    
  
def compara_assinatura(as_a, as_b):
  sominha = 0
  newlist = 0
  
  for x, y in zip(as_a, as_b):
    sominha += abs(x-y)
    newlist += sominha
    
  similaridade = newlist/6
  return similaridade

def calcula_assinatura(texto):
  tmdp = wal_txt(texto)
  tmds = sal_txt(texto)
  tmdf = pal_txt(texto)
  compds = sac_txt(texto)
  rtoken = ttr_txt(texto)
  rlegomana = hlr_txt(texto)
  listaShow = [tmdp, rtoken, rlegomana, tmds, compds, tmdf]
  
  return listaShow


def avalia_textos(textos, ass_cp):
  menor = compara_assinatura(ass_cp, calcula_assinatura(textos[0]))
  textoContador = 0
  for x in textos:
    assinatura = calcula_assinatura(x)
    similaridade = compara_assinatura(ass_cp, assinatura)
    textoContador += 1
    if(similaridade<=menor):
      resposta = textoContador

    
    
  return print("O autor do texto", resposta, "está infectado com COH-PIAH", end="\n")


def tam_med(frase):
  tamanho = 0
  for i in frase:
    tamanho = tamanho + len(i)
  
  return tamanho
  
def main_function():
  ass_cp = le_assinatura()
  textos = le_textos()
  avalia_textos(textos, ass_cp)
  return 0

              

main_function()
    
    

