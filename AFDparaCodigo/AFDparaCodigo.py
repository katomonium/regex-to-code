#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#~ from desenhaGrafo.fileHandler import lerAutomato
from string import Template
from AFDparaCodigo.Estado import Estado
from AFDparaCodigo.Transicao import Transicao
from AFDparaCodigo.Automato import Automato

class GeradorDeCodigo:
    
    automato = None
    
    definicaoClasse = Template('def q$nomeEstado(codigo, indice):\n')
    condicaoCaractere = Template('    if(codigo[indice] == "$letraTransicao"):\n        indice+=1\n        return q$estadoDestino(codigo,indice)\n')
    condicaoFinal = Template('    if(indice == len(codigo)):\n        return $booleano\n')
    cabecalho = "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\nimport sys\n\n"
    mainPrograma = Template("""
def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().strip().splitlines()
    for lin in linhas:
        print(q$estadoInicial(lin, indice))
        
main(sys.argv)""")
    
    def __init__(self,automato):
        self.automato = automato
    
    def gerarCodigo(self):
        resultado = self.cabecalho
        for estado in self.automato.estados:
            resultado += self.criaFuncao(estado)
        resultado += self.criaMain(self.automato.estadosDic[self.automato.inicial])
        return resultado
        
    
    def criaFuncao(self,estado):
        if(estado.idEstado == "qERRO1"):
            return ""
        resultado = self.definicaoClasse.substitute(nomeEstado = estado.idEstado)
        if estado.final:
            resultado += self.condicaoFinal.substitute(booleano = 'True')
        else:
            resultado += self.condicaoFinal.substitute(booleano = 'False')
        for transicao in estado.transicoes:
            if(transicao.letra == "␣"):
                transicao.letra = " "
            resultado += self.condicaoCaractere.substitute(letraTransicao = transicao.letra, estadoDestino = transicao.destino.idEstado)
        resultado += "    return False\n\n"
        return resultado
        
    def criaMain(self, estadoInicial):
        return self.mainPrograma.substitute(estadoInicial = estadoInicial.idEstado)


def AFDparaCodigo(argv):
    if(len(argv) < 2):
        return
    entrada = argv[0]
    saida = argv[1]
    
    a = Automato(entrada)
    arquivo = open(saida, 'w')
    
    gdc = GeradorDeCodigo(a)
    arquivo.write(gdc.gerarCodigo())