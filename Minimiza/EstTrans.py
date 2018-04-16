#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Estado:                       #Estrutura para representar os estados do automato
    idEstado = None                 #"nome" do estado
    transicoes = None               #transicoes do estado
    final = None                    #booleano para representar se é final ou nao
    equivalentes = None             #estados que sao iguais
    usado = None                    #booleano para evitar repetições na construção do automato minimizado 
    estadoNovo = None               #referencia o seu estado equivalente no automato minimizado
    
    
    def __init__(self):             #construtor de Estado
        self.final = False
        self.transicoes = []
        self.equivalentes = []
        self.usado = False
        self.estadoNovo = False

class Transicao:                    #Estrutura para representar uma transição
    origem = None                   #Estado de origem
    destino = None                  #Estado de destino
    letra = None                    #Simbolo lido
    
    def __init__(self, origem, letra, destino):
        self.origem = origem
        self.destino = destino
        self.letra = letra
