#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Automato:
    estados = None
    alfabeto = None
    transicoes = None
    estadoInicial = None
    estadoFinal = None

    def __init__(self, estadoInicial = None, estadoFinal = None, alfabeto = None):
        self.alfabeto = alfabeto
        self.estados = {}
        self.alfabeto = {}
        self.transicoes = []
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        if(self.estadoInicial != None):
            self.estados[self.estadoInicial] = self.estadoInicial
        if(self.estadoFinal != None):
            self.estados[self.estadoFinal] = self.estadoFinal
        
    def acrescentaAutomato(self, indice, acrescentado):
        link = {}
        for estado in acrescentado.estados:
            link[estado] = indice
            self.estados[indice] = indice
            indice += 1
        for transicao in acrescentado.transicoes:
            for estado in acrescentado.estados:
                if(estado == transicao[0]):
                    t = (link[estado], transicao[1], link[transicao[2]])
                    self.transicoes.append(t)
        if(self.estadoInicial == None and self.estadoFinal == None):
            self.estadoInicial = link[acrescentado.estadoInicial]
            self.estadoFinal = link[acrescentado.estadoFinal]
        return [indice, link]