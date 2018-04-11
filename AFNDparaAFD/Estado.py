#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Estado:                       #Estrutura para representar os estados do automato
    idEstado = None                 #"nome" do estado
    transicoes = None               #transicoes do estado
    final = None                    #booleano para representar se é final ou nao
    equivalentes = None             #estados que sao iguais
    usado = None                    #booleano para evitar repetições na construção do automato minimizado
    estadoNovo = None               #referencia o seu estado equivalente no automato minimizado
    estadosAlcancaveis = None
    cor = None


    def __init__(self):             #construtor de Estado
        self.final = False
        self.transicoes = []
        self.equivalentes = []
        self.usado = False
        self.estadoNovo = False
        self.estadosAlcancaveis = set()
        self.cor = "B"

    def printEstado(self):
        s = "\nID do Estado: \n"
        s += "q" + self.idEstado

        s += "\nAlcança: \n"
        for estado in self.estadosAlcancaveis:
            s += "q" + estado.idEstado + "\n"
