# -*- coding: utf-8 -*-

from django.shortcuts import render
from perfis.models import Perfil

#Follow the convention about insert the html page inside the 'templates' folder!!!
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil(nome='Flavio Almeida', email='flavio@flavio.com.br', telefone= '34411441', nome_empresa='Alura')
    elif perfil_id == '2':
        perfil = Perfil('Romulo Henrique', 'romulo@romulo.com.br', '888888', 'Caelum')
    elif perfil_id == '3':
        perfil = Perfil('Vinícius Melo', 'vinicius@vinicius.com', '99999999', 'Open Source')

    print("Id do perfil recebido: %s" % (perfil_id))
    return render(request, 'perfil.html', {'perfil' : perfil})
