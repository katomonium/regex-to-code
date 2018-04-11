#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#~ from desenhaGrafo.fileHandler import lerAutomato
from string import Template
from Estado import Estado
from Transicao import Transicao

class GeradorDeCodigo():
    t = Template('\tif(codigo[indice] == $letraTransicao):\n\t\tindice+=1\n\t\t$estadoDestino(codigo,indice)\n')
    inicio = Template('def $nomeEstado(codigo, indice):\n')

    def criaFuncao(self,estado):
        resultado = self.inicio.substitute(nomeEstado = estado.idEstado)
        for transicao in estado.transicoes:
            resultado += self.t.substitute(letraTransicao = transicao.letra, estadoDestino = transicao.destino.idEstado)
        return resultado

def AFDparaCodigo():
    #~ entrada = sys.argv[1]
    #~ saida = sys.argv[2]
    #~ automato = lerAutomato(entrada)
    #~ print(automato.inicial)
    
    #~ criarArquivo()
    e1 = Estado()
    e2 = Estado()
    e3 = Estado()
    e3.idEstado = "e3"
    e2.idEstado = "e2"
    e1.idEstado = "e1"
    t1 = Transicao(e3,"a",e1)
    t2 = Transicao(e3,"b",e2)
    e3.transicoes.append(t1)
    e3.transicoes.append(t2)
    
    gdc = GeradorDeCodigo()
    print(gdc.criaFuncao(e3))
