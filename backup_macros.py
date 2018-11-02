# -*- coding: utf-8 -*-
"""
Create copy from macros in productivity.
Always add the path name and the 5 first letters of the archive to the variables:
    nomes:
    sources:
Automatize the process of backup and version control.
"""

import os
from shutil import copy, move
from sys import exit
import datetime
from zipfile import ZipFile, ZIP_DEFLATED


#Important variable, if other people is using, this have to change.
target = os.path.abspath(r'C:\Users\brmelovi\OneDrive - NESTLE\Script\backups')


def backup(source: str, name: str):
    """
    names don't have to be the WHOLE name
    Just a part of it.
    """
    try:
        arquivos_diretorio = os.listdir(source)
        for x in arquivos_diretorio:
            if x.startswith(name):
                arquivo = x
                break
        copy(source + '\\' + arquivo, target)
        status = True
        return status
    except IOError as e:
        status = False
        print("Error: " + e)
        exit(1)
        return status
    except:
        print("Error!!!")
        exit(1)


def create_folder():
    """
    create a log that count if the things go right or wrong.
    """
    efetuados = 0
    now = datetime.date.today()
    backup_diario = 'Backup ' + str(now)
    os.chdir(target)
    new_zip = ZipFile(file=backup_diario + '.zip', mode="w")
    try:
        arquivos_diretorio = os.listdir()
        for arqs in arquivos_diretorio:
            if os.path.isfile(arqs) and not arqs.endswith('.zip'):
                print(arqs)
                new_zip.write(filename=arqs, compress_type=ZIP_DEFLATED)
                os.remove(arqs)
                efetuados += 1
        os.mkdir(backup_diario)
        new_zip.close()
        move(backup_diario + '.zip', backup_diario)
        return efetuados
    except Exception as e:
        print('Deu ruim no log...' + e)
        return 0


def principal():
    """
    create the two main variables
    loop through all the items in the list
    to add just put a comma and change bellow
    """
    #Append names below:
    global nomes
    nomes = [ \
        'Credit Analysis', #0
    	'macro', #1
    	'Remessa Macro', #2
    	'Relatorios', #3
    	'Automação', #4
    	'macro', #5
    	'Macro Sucata', #6
    	'Planilha', #7
    	'Matriz', #8
    	'templateEc', #9
    	'Carta', #10
    	'template', #11
    	'db', #12
    	'Matriz_', #13
    	'email_refs', #14
    	'O2C Incident Log.xlsb', #15
    	'DB_O2C', #16
    	'Macro Tickets', #17
    	'Macro Cheques Chile', #18
	    ]
    #Append sources bellow:
    global sources
    sources = [ \
        r'N:\NBS_AR\SISTEMAS AR\Macro Credit Analysis & Collection', #0
    	r'N:\NBS_AR\COLLECTION\1.0 Times\2.0 Collections México\1. Macro de solicitação de Desglose', #1
    	r'N:\NBS_AR\OHM\9.0 Informações Equipe', #2
    	r'N:\NBS_AR\COLLECTION\1.0 Times\1.8 Collections Ecuador', #3
    	r'N:\NBS_AR\BACK OFFICE\1.0 Times\1.2 Nota de Crédito\1.3 Ajuste Aplicação', #4
    	r'N:\NBS_AR\BACK OFFICE\1.0 Times\1.2 Nota de Crédito\1.4 Ajuste Validação', #5
    	r'N:\NBS_AR\COLLECTION\1.0 Times\1.4 DVD & Perdas\1.4.12 Venda não operacional', #6
    	r'N:\NBS_AR\SISTEMAS AR\O2C_Planilha_Retencao', #7
    	r'N:\NBS_AR\COLLECTION\1.0 Times\1.8 Collections Ecuador\base Ecuador', #8
    	r'N:\NBS_AR\COLLECTION\1.0 Times\1.8 Collections Ecuador', #9
    	r'N:\NBS_AR\COLLECTION\1.0 Times\2.1 Collections Colombia\Cartas\Circularización', #10
    	r'N:\NBS_AR\COLLECTION\1.0 Times\2.1 Collections Colombia\Cartas\Circularización\base', #11
    	r'N:\NBS_AR\COLLECTION\1.0 Times\2.1 Collections Colombia\Cartas\Circularización\base', #12
    	r'N:\NBS_AR\CASH\CORPORATE\11.0 - Reporting\11.5 México\Vinicius', #13
    	r'N:\NBS_AR\CASH\CORPORATE\11.0 - Reporting\11.5 México\Vinicius\emails referencias', #14
    	r'N:\NBS_AR\SISTEMAS AR\O2C_Incident_Log', #15
    	r'N:\NBS_AR\SISTEMAS AR\O2C_Incident_Log', #16
    	r'N:\NBS_AR\CASH\APPLY\Argentina\9.0 - Documentos de uso diário', #17
    	r'N:\NBS_AR\CASH\APPLY\3.0 MATERIAL DE APOIO\3.1 MACROS', #18
	    ]
    status = []
    for i in range(len(sources)):
        status.append(backup(sources[i], nomes[i]))
    return status


def main():
    status = principal()
    efetuados = create_folder()
    assert efetuados == len(nomes)
    if (efetuados):
        print('Nice, were made: ' + str(efetuados) + ' backups!\n' + str(len(nomes)) + ' backups which should have been done!\n')
    else:
        print('Algo deu errado\n')

if __name__ == '__main__':
    main()
