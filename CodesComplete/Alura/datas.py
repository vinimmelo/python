# Created on 21 November 2018
# @author vinimmelo
# Format data

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
