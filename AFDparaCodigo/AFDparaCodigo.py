#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#~ from desenhaGrafo.fileHandler import lerAutomato
from string import Template
from Estado import Estado
from Transicao import Transicao
from Automato import Automato

class GeradorDeCodigo:
    
    automato = None
    
    definicaoClasse = Template('def q$nomeEstado(codigo, indice):\n')
    condicaoCaractere = Template('    if(codigo[indice] == "$letraTransicao"):\n        indice+=1\n        return q$estadoDestino(codigo,indice)\n')
    condicaoFinal = Template('    if(indice == len(codigo)):\n        return $booleano\n')
    cabecalho = "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\nimport sys\n\n"
    mainPrograma = Template("def main(args):\n    arquivo = open(args[1], 'r')\n    indice = 0\n    linhas = arquivo.read().splitlines()\n    print($estadoInicial(linhas[0], indice))")
    
    def __init__(self,automato):
        self.automato = automato
    
    def gerarCodigo(self):
        resultado = self.cabecalho
        for estado in self.automato.estados:
            resultado += self.criaFuncao(estado)
        print(self.automato.inicial + " okoko")
        print(self.automato.estadosDic)
        resultado += self.criaMain(self.automato.estadosDic[self.automato.inicial])
        return resultado
        
    
    def criaFuncao(self,estado):
        resultado = self.definicaoClasse.substitute(nomeEstado = estado.idEstado)
        if estado.final:
            resultado += self.condicaoFinal.substitute(booleano = 'True')
        else:
            resultado += self.condicaoFinal.substitute(booleano = 'False')
        for transicao in estado.transicoes:
            resultado += self.condicaoCaractere.substitute(letraTransicao = transicao.letra, estadoDestino = transicao.destino.idEstado)
        resultado += "    return False\n\n"
        return resultado
        
    def criaMain(self, estadoInicial):
        return self.mainPrograma.substitute(estadoInicial = estadoInicial.idEstado)

def AFDparaCodigo():
    if(len(sys.argv) < 3):
        return
    entrada = sys.argv[1]
    saida = sys.argv[2]
    #~ automato = lerAutomato(entrada)
    #~ print(automato.inicial)
    
    a = Automato(entrada)
    
    
    
    
    arquivo = open(sys.argv[2], 'w')
    
    gdc = GeradorDeCodigo(a)
    arquivo.write(gdc.gerarCodigo())
    print(gdc.gerarCodigo())
    
AFDparaCodigo()
