from LeituraEscrita import Arquivo
from PseudoEstado import PseudoEstado
from AutomatoFD import AutomatoFD

class Automato:
    estados = None                  #lista de estados do automato
    estadosDic = None               #dicionario que referencia os estados
    alfabeto = None
    inicial = None
    finais = None                   #dicionario de estados finais

    #cria um dicionario de estados para o automato

    def __init__(self, nomeArq = None):
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
        # print(self.estadosDic)
        self.inicial = arquivo.leInicial()
        self.finais = arquivo.leFinais()

        #marca os estados finais
        for i in range(len(self.estados)):
            if(self.estados[i].idEstado in self.finais):
                self.estados[i].final = True
    
    #~ def buscaEmProfundidade(self):
        #~ for estado in self.estados:
            #~ buscaEmProfundidadeAUX(estado)
                        
    
    #~ def buscaEmProfundidadeAUX(self, estado):
        #~ if(estado.cor == "B"):
            #~ estado.estadosAlcancaveis.append(estado)
            #~ for transicao in estado.transicoes:
                #~ if(transicao.letra == "λ"):
                    #~ if(
    
    def criaDicionario(self, estados):
        estadosDic = {}
        for i in range(len(estados)):
            estadosDic[estados[i].idEstado] = estados[i]
        return estadosDic

    def tranformaEmAFD(self):
        automatoFD = AutomatoFD()
        estadoInicial = self.estadosDic[self.inicial]
        vetorEstadosIniciais = []
        vetorEstadosIniciais.append(estadoInicial)
        for transicao in estadoInicial.transicoes:
            if(transicao.letra == "λ"):
                vetorEstadosIniciais.append(trasicao.destino)
        PEinicial = automatoFD.fundirEstadosSeNaoForamFundidos(vetorEstadosIniciais)
        automatoFD.adicionaPE(PEinicial)
        # PEinicial.printPE()

        while(not automatoFD.acabou()):
            for PE in automatoFD.PErestantes:
                for letra in self.alfabeto:
                    vetorEstados = []
                    for transicao in PE.transicoes:
                        if(transicao.letra == letra):
                            if(transicao.destino not in vetorEstados):
                                vetorEstados.append(transicao.destino)
                    PEdestino = automatoFD.fundirEstadosSeNaoForamFundidos(vetorEstados)
                    if(PEdestino is not None):
                        automatoFD.adicionaPE(PEdestino)
                        PE.criarTransicaoReal(letra, PEdestino)
                PE.verificado = True
                automatoFD.PErestantes.remove(PE)
        automatoFD.printAFD()



    #funcao de minimizacao
    def minimiza(self, arqTabela, arqMin):
        arquivoTabela = open(arqTabela, 'w')    #instancia um arquivo para escrever a tabela
        tabela = Tabela()                       #instancia o objeto que monta a tabela

        #cria os pares da tabela de minimizacao
        for i in range(len(self.estados)):
            for j in range(i+1, len(self.estados)):
                par = Par(self.estados[i], self.estados[j])
                tabela.pares.append(par)

        tabela.minimiza(self)                   #aplica o algoritmo de minimizacao na tabela
        tabela.imprimeTabela(arquivoTabela)     #escreve a tabela no arquivo

        escritor = Arquivo(arqMin, 'w')         #instancia o objeto para escrever o automato no arquivo
        escritor.escreveMinimizado(self)        #escreve o novo automato no arquivo
