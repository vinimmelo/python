#!/usr/bin/env python3
# Created on 22 November 2018
# @author vinimmelo
# Simple oo test


def cria_conta(numero, titular, saldo, limite):
    """ cria uma conta """"
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo,
        'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(conta['saldo'])
