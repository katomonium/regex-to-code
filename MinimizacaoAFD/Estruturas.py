# -*- coding: UTF-8 -*-
# GRUPO: Arthur Henrique, Pedro Silveira, João Pedro
# MODO DE EXECUCAO:
# python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>

from MinimizaicaoAFD.LeituraEscrita import *
from MinimizaicaoAFD.Estado import Estado
from MinimizaicaoAFD.Transicao import Transicao

class Par:                          #representa um par da tabela de minimizacao
    e1 = None                       #estado 1
    e2 = None                       #estado 2
    valido = None                   #se os estados desse par sao considerados iguais
    dependentes = None              #os pares dependentes desse par
    motivo = None                   #o motivo de nao serem iguais
    
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
        if(e1.final == e2.final):           #checa se os dois sao, ao mesmo tempo, finais ou nao-finais
            self.valido = True
            self.motivo = ""
        else:                               #se nao forem, considera-os diferentes e adiciona o motivo
            self.valido = False
            self.motivo = "final/nao-final"
        self.dependentes = []
        
    def getValidacao(self):                 #converte True para 1 e False para 0
        if(self.valido == False):           #em python isso nao e automatico
            return 1
        return 0
    
class Automato:
    estados = None                  #lista de estados do automato
    estadosDic = None               #dicionario que referencia os estados
    alfabeto = None
    inicial = None
    finais = None                   #dicionario de estados finais


    #gera o automato minimizado
    def novoAutomato(self):
        novoAutomato = Automato()
        
        for estado in self.estados:
            if not(estado.usado):                       #Se o estado nao foi usado, insere-o no novo Automato

                #Se houver estados equivalentes, une-os em um único                   
                if(len(estado.equivalentes) >0):        #OBS: Equivalentes sao adicionados durante a geracao da tabela
                    novoEstado = Estado()               
                    novoEstado.final = estado.final     #Se estados finais foram unidos, gera um estado tambem final, senao gera um nao-final
                    novoAutomato.estados.append(novoEstado)
                    estado.estadoNovo = novoEstado      #O antigo estado referencia o novo estado minimizado
                    nome = "q" + estado.idEstado
                    novoEstado.equivalentes.append(estado)  #Adiciona ao novo, os estados originais
                    ini = (estado.idEstado == self.inicial) #Se algum dos estados antigos for inicial, o novo estado tambem o é
                    estado.usado = True                     #Indica que o estado foi usado
                    
                    #Faz-se o mesmo para cada equivalente
                    for equivalente in estado.equivalentes:
                        novoEstado.equivalentes.append(equivalente)
                        equivalente.usado = True
                        nome += "q" + str(equivalente.idEstado)
                        equivalente.estadoNovo = novoEstado
                        if(equivalente.idEstado == self.inicial):
                            ini = True
                    novoEstado.idEstado = nome                          #O nome do novo estado é a concatenação dos nomes dos antigos
                    if(ini):
                        novoAutomato.inicial = novoEstado.idEstado
                
                #Se nao houver estados equivalentes, cria um novo estado igual ao antigo
                else:
                    novoEstado = Estado()
                    novoEstado.final = estado.final
                    novoAutomato.estados.append(novoEstado)
                    estado.estadoNovo = novoEstado
                    nome = "q" + str(estado.idEstado)
                    novoEstado.idEstado = nome
                    novoEstado.equivalentes.append(estado)
                    if(estado.idEstado == self.inicial):
                        novoAutomato.inicial = novoEstado.idEstado
                    
        novoAutomato.estadosDic = novoAutomato.criaDicionario(novoAutomato.estados)
        
        for i in range(len(self.estados)):      #Considera todos como nao usados novamente
            self.estados[i].usado = False
        
        #Pega as transições dos estados antigos e adiciona no novo automato 
        for estado in novoAutomato.estados:
            equivalente = estado.equivalentes[0]    #Pega o equivalente desse estado no automato antigo 
            for transicao in equivalente.transicoes:
                if (transicao.origem.estadoNovo == None):   #Se o estado nao foi minimizado, a origem se mantem 
                    e1 = "q" + transicao.origem.idEstado
                else:                                       #Senao, a origem se torna o estado minimizado
                    e1 = transicao.origem.estadoNovo.idEstado   
                
                #O mesmo acontece para o destino da transiçao
                if (transicao.destino.estadoNovo == None):
                    e2 = "q" + transicao.destino.idEstado
                else:
                    e2 = transicao.destino.estadoNovo.idEstado
                
                #Adiciona a transiçao no estado do automato novo
                e1 = novoAutomato.estadosDic[e1]
                e2 = novoAutomato.estadosDic[e2]
                novaTransicao = Transicao(e1, transicao.letra ,e2)
                if(novaTransicao not in e1.transicoes):
                    e1.transicoes.append(novaTransicao)
                
        novoAutomato.alfabeto = self.alfabeto
                
        return novoAutomato

    #cria um dicionario de estados para o automato
    def criaDicionario(self, estados):
        estadosDic = {}
        for i in range(len(estados)):
            estadosDic[estados[i].idEstado] = estados[i]
        return estadosDic
    
    
    def __init__(self, nomeArq = None):
        print("OEEEEEEEEEEEEE")
        if(nomeArq == None):        #se nao for passado o nome do arquivo por parametro, cria-se um automato vazio
            self.estados = []
            self.estadosDic = {}
            self.alfabeto = []
            self.finais = {}
            return
        
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
    
    
    #funcao de minimizacao
    def minimiza(self, arqTabela, arqMin):
        arquivoTabela = open(arqTabela, 'w')    #instancia um arquivo para escrever a tabela
        tabela = Tabela()                       #instancia o objeto que monta a tabela
        
        # cria os pares da tabela de minimizacao
        for i in range(len(self.estados)):
            for j in range(i+1, len(self.estados)):
                par = Par(self.estados[i], self.estados[j])
                tabela.pares.append(par)
        
        tabela.minimiza(self)                   #aplica o algoritmo de minimizacao na tabela
        tabela.imprimeTabela(arquivoTabela)     #escreve a tabela no arquivo
        
        escritor = Arquivo(arqMin, 'w')         #instancia o objeto para escrever o automato no arquivo
        escritor.escreveMinimizado(self)        #escreve o novo automato no arquivo
        


class Tabela:
    pares = None
    
    def __init__(self):
        self.pares = []
        
        
    #propaga recursivamente o resultado de um par de estados
    def propaga(self, par):
        
        #se houver dependentes, para cada dependente propaga o resultado
        if(len(par.dependentes) > 0):
            for dep in par.dependentes:
                if(par != dep):
                    dep.valido = False
                    dep.motivo = "prop[" + par.e1.idEstado + "," + par.e2.idEstado + "]"
                    self.propaga(dep)               #propaga tambem para os dependentes desse dependente
    
    #aplica o algoritmo de minimizacao na tabela
    def minimiza(self, automato):
        for par in self.pares:
            for transicao1 in par.e1.transicoes:
                for transicao2 in par.e2.transicoes:
                    
                    #se o par ainda for considerado igual devem ser testadas as transicoes desse par
                    if(par.valido and transicao1.letra == transicao2.letra):    
                        
                        #se uma das transicoes tiver como destino um estado final e a outra nao, considera diferentes e propaga para seus dependentes
                        if((transicao1.destino.idEstado in automato.finais) != (transicao2.destino.idEstado in automato.finais)):
                            par.valido = False
                            par.motivo = transicao1.letra + "[" + transicao2.destino.idEstado + "," + transicao1.destino.idEstado + "]"
                            
                            self.propaga(par)
                                
                        #se nao,##SILVERAAA, explica isso#
                        else:
                            # if(transicao1.origem != transicao1.destino and transicao2.origem != transicao2.destino):
                            print(transicao1.origem != transicao1.destino and transicao2.origem != transicao2.destino)
                            print("procurando par: " + transicao1.destino.idEstado + " - " + transicao2.destino.idEstado)
                            for p in self.pares:
                                print("achei o: " + p.e1.idEstado + " -- " + p.e2.idEstado)
                                if(str(p.e1.idEstado) == str(transicao1.destino.idEstado) and str(p.e2.idEstado) == str(transicao2.destino.idEstado)):
                                    print("EUOOOOO")
                                    p.dependentes.append(par)

        #adiciona, ao estado, os estados iguais a ele
        for par in self.pares:
            if(par.valido):
                par.e1.equivalentes.append(par.e2)
                par.e2.equivalentes.append(par.e1)
                
    #formata o texto e escreve no arquivo
    def imprimeTabela(self, arquivo):
        saida = ("INDICE \t \t" + "D[i,j] = \t " + "S[i,j] = \t \t" + "MOTIVO\n")
        for par in self.pares:
            dep = "{ "
            if(par.dependentes != None):
                for i in range(len(par.dependentes)):
                    dep += "[" + par.dependentes[i].e1.idEstado + ", " + par.dependentes[i].e2.idEstado + "]"
                    if(i < len(par.dependentes) - 1):
                        dep += ","
            dep += " }"
            saida += ("[" + str(par.e1.idEstado) + "," + str(par.e2.idEstado)
                        + "] \t\t" + str(par.getValidacao()) + "\t \t" + str(dep) + "\t \t \t" + str(par.motivo) + "\n")
        arquivo.write(saida)           
            
            
            
            
            
            
            
            
            
            
            
