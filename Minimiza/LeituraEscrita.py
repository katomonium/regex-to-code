#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from Minimiza.EstTrans import Estado
from Minimiza.EstTrans import Transicao
#classe que gerencia arquivo
class Arquivo:
    arq = None
    linhas = None
    posErro = None
    def __init__(self, nomeArq, modo):
        print(nomeArq)
        self.arq = open(nomeArq, modo)              #Abre o arquivo no modo desejado ('w' - escrita, 'r' - leitura)
        if(modo == 'r'):                            #Se for estado de leitura, le o arquivo dividindo-o por linhas
            self.linhas = self.arq.read().strip().splitlines()
        
    def leEstados(self):
        estadosRetorno = []
        aux = re.compile("q(\d+)")                  #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        estados = aux.findall(self.linhas[1])       #Procura esse padrao na linha 2 do arquivo, retornando uma lista com os digitos que satisfazem o padrao
        
        #Cria uma instancia de Estado para cada item da lista
        for i in range(len(estados)):               
            novo = Estado()
            novo.idEstado = estados[i]
            estadosRetorno.append(novo)
        estadoErro = Estado()
        estadoErro.idEstado = "ERRO"
        estadosRetorno.append(estadoErro)
        self.posErro = len(estadosRetorno) - 1
        return estadosRetorno
    
    
    def leAlfabeto(self): #alfabeto é uma lista
        i = 2
        aux = re.compile("{(.*)}")         
                                                       
        alf = ''.join(aux.findall(self.linhas[2]))
        #~ self.linhas[2] = self.linhas[2].strip().split()
        #~ while(i < len(self.linhas[2]) - 2):
            #~ aux.append(self.linhas[2][i])
            #~ print(self.linhas[2][i])
            #~ i += 1
        #~ aux = ''.join(aux)
        alfabeto = alf.strip().split(",")
        return alfabeto
        
    def leTransicoes(self, automato):
        self.arq.seek(0)                                #Volta ao inicio do arquivo
        texto = self.arq.read()                         #Le o arquivo completo
        aux = re.compile("q(\d+),(.+)->q(\d+)")         #Define aux como o seguinte padrao "q(\d+),(\w)->q(\d+)", 
                                                        #onde (\d+) é um ou mais digitos e (\w) é uma palavra qualquer
        transicoes = aux.findall(texto)                 #Procura em "texto" esse padrao e retorna uma lista de tuplas
        
        #Para cada tupla da lista "transicoes", cria-se um objeto da classe Transicao e armazena-a no estado de origem
        for item in transicoes:
            i = item[0]
            estadoOrigem = automato.estadosDic[i]
            
            letra = item[1]
            
            i = item[2]
            estadoDestino = automato.estadosDic[i]
            
            transicao = Transicao(estadoOrigem, letra, estadoDestino)
            estadoOrigem.transicoes.append(transicao)
        
        completo = True
        for letra in automato.alfabeto:
            if(letra != "λ"):
                for estado in automato.estados:
                    if(estado.idEstado != "ERRO"):
                        achou = False
                        for t in estado.transicoes:
                            if(t.letra == letra):
                                achou = True
                        if(not achou):
                            completo = False
                            estadoOrigem = automato.estados[int(estado.idEstado)]
                            
                            i = str(automato.estados[self.posErro].idEstado)
                            estadoDestino = automato.estadosDic[i]
                            
                            transicao = Transicao(estadoOrigem, letra, estadoDestino)
                            estadoOrigem.transicoes.append(transicao)
        if(completo):
            i = str(automato.estados[self.posErro].idEstado)
            automato.estadosDic.pop(i)
            automato.estados.pop(self.posErro)
            posErro = None
        else:
            for letra in automato.alfabeto:
                if(letra != "λ"):
                    estadoOrigem = automato.estados[self.posErro]
                                
                    i = str(automato.estados[self.posErro].idEstado)
                    estadoDestino = automato.estadosDic[i]
                                
                    transicao = Transicao(estadoOrigem, letra, estadoDestino)
                    estadoOrigem.transicoes.append(transicao)
        
        
            
        return
    
    def leInicial(self):
        ini = re.compile("q(\d+)")                      #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        inicial = ini.findall(self.linhas[-3])          #Encontra esse padrao na antepenultima linha do arquivo
        inicial = inicial[0]
        return inicial
    
    def leFinais(self):
        fin = re.compile("q(\d+)")                      #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        finais = fin.findall(self.linhas[-2])           #Encontra esse padrao na penultima linha do arquivo
        dicionario = {}                                 #Cria um dicionario para armazenar os estados finais
        for i in range (len(finais)):
            if(not(finais[i] in dicionario)):
                f = finais[i]
                dicionario[f] = f
        return dicionario
    
    #Formata o texto para escrever no arquivo
    def escreveMinimizado(self, automato):
        novo = automato.novoAutomato()                  #Gera o automato minimizado para escrevê-lo no arquivo
        # novo = automato
        
        novo.renomeia()
        saida = "(\n\t{"
        for i in range(len(novo.estados)):
        #if(novo.estados[i].idEstado != "qERRO"):
            saida += novo.estados[i].idEstado
            if(i < len(novo.estados) - 1):
                saida += ","
            
        saida += "},\n\t{"
        for l in novo.alfabeto:
            saida += l
            if(l != novo.alfabeto[len(novo.alfabeto) - 1]):
                saida += ","
        
        saida += "},\n\t{\n"
        for i in range(len(novo.estados)):
        #if(novo.estados[i].idEstado != "qERRO"):
            for j in range(len(novo.estados[i].transicoes)):
               # if(novo.estados[i].transicoes[j].destino.idEstado != "qERRO"):
                    saida += "\t\t(" + novo.estados[i].transicoes[j].origem.idEstado + "," + novo.estados[i].transicoes[j].letra + "->" + novo.estados[i].transicoes[j].destino.idEstado + ")"
                    if((j < len(novo.estados[i].transicoes) - 1) or (i < len(novo.estados) - 1)):
                        saida += ","
                        saida += "\n"
        
        saida += "\t},\n\t"
        saida += novo.inicial + ","
        saida += "\n\t{"
        qtdFin = 0
        for i in range(len(novo.estados)):
            if(novo.estados[i].final):
                if(qtdFin > 0):
                    saida+=","
                saida += novo.estados[i].idEstado
                qtdFin += 1
        saida += "}\n)"
        
        self.arq.write(saida)


    def imprimeAut(self, novo):
        saida = "(\n\t{"
        for i in range(len(novo.estados)):
            saida += novo.estados[i].idEstado
            if(i < len(novo.estados) - 1):
                    saida += ","
                
        saida += "},\n\t{"
        for l in novo.alfabeto:
            saida += l
            if(l != novo.alfabeto[len(novo.alfabeto) - 1]):
                saida += ","
        
        saida += "},\n\t{\n"
        for i in range(len(novo.estados)):
            for j in range(len(novo.estados[i].transicoes)):
                saida += "\t\t(" + novo.estados[i].transicoes[j].origem.idEstado + "," + novo.estados[i].transicoes[j].letra + "->" + novo.estados[i].transicoes[j].destino.idEstado + ")"
                if((j < len(novo.estados[i].transicoes) - 1) or (i < len(novo.estados) - 1)):
                    saida += ","
                saida += "\n"
        
        saida += "\t},\n\t"
        saida += novo.inicial + ","
        saida += "\n\t{"
        qntFinais = 0
        for i in range(len(novo.estados)):
            if(novo.estados[i].final):
                if(qntFinais > 0):
                    saida+=","
                saida += novo.estados[i].idEstado
                qntFinais += 1
                # if(i < len(novo.finais)):
                #     saida += ","
        saida += "}\n)"
        print(novo.finais)
        print(saida)
