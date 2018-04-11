#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Transicao:                    #Estrutura para representar uma transição
    origem = None                   #Estado de origem
    destino = None                  #Estado de destino
    letra = None                    #Simbolo lido

    def __init__(self, origem, letra, destino):
        self.origem = origem
        self.destino = destino
        self.letra = letra
