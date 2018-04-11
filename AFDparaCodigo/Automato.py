#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from AFDparaCodigo.LeituraEscrita import Arquivo

class Automato:
    estados = None                  #lista de estados do automato
    estadosDic = None               #dicionario que referencia os estados
    alfabeto = None
    inicial = None
    finais = None                   #dicionario de estados finais
    
    pilha = None

    #cria um dicionario de estados para o automato

    def __init__(self, nomeArq = None):
        self.pilha = []
        
        if(nomeArq == None):        #se nao for passado o nome do arquivo por parametro, cria-se um automato vazio
            self.estados = []
            self.estadosDic = {}
            self.alfabeto = []
            self.finais = {}
            
          

        arquivo = Arquivo(nomeArq, 'r')         #instancia um objeto da classe arquivo (no arquivo LeituraEscrita)

        #operacoes de leitura do arquivo
        self.estados = arquivo.leEstados()
        self.estadosDic = self.criaDicionario(self.estados)
        self.alfabeto = arquivo.leAlfabeto()
        arquivo.leTransicoes(self)
        self.inicial = arquivo.leInicial()
        self.finais = arquivo.leFinais()
        #marca os estados finais
        for i in range(len(self.estados)):
            if(self.estados[i].idEstado in self.finais):
                self.estados[i].final = True
    
    
    def criaDicionario(self, estados):
        estadosDic = {}
        for i in range(len(estados)):
            estadosDic[estados[i].idEstado] = estados[i]
        return estadosDic
