# -*- coding: utf-8 -*-

from django.shortcuts import render
from perfis.models import Perfil

#Follow the convention about insert the html page inside the 'templates' folder!!!
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)

    print("Id do perfil recebido: %s" % (perfil_id))
    return render(request, 'perfil.html', {'perfil' : perfil})
