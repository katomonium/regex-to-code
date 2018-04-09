class Estado:                       #Estrutura para representar os estados do automato
    idEstado = None                 #"nome" do estado
    transicoes = None               #transicoes do estado
    final = None                    #booleano para representar se é final ou nao
    equivalentes = None             #estados que sao iguais
    usado = None                    #booleano para evitar repetições na construção do automato minimizado
    estadoNovo = None               #referencia o seu estado equivalente no automato minimizado
    estadosAlcancaveis = None
    cor = None


    def __init__(self):             #construtor de Estado
        self.final = False
        self.transicoes = []
        self.equivalentes = []
        self.usado = False
        self.estadoNovo = False
        self.estadosAlcancaveis = set()
        self.cor = "B"

    #~ def getAlcancaveis(self):
        #~ if(self.cor == "P"):
            #~ return self.estadosAlcancaveis
            
        #~ if(self.cor == "B"):
            #~ self.cor = "C"
            #~ self.estadosAlcancaveis.add(self)
            #~ for transicao in self.transicoes:
                #~ if(transicao.letra == "λ"):
                    #~ destino = transicao.destino
                    #~ if(destino.cor == "C"):
                        #~ for alcancavel in self.estadosAlcancaveis:
                            #~ destino.estadosAlcancaveis.add(alcancavel)
                        #~ self.estadosAlcancaveis = destino.estadosAlcancaveis
                        
                    #~ else:
                        #~ print("atual = " + self.idEstado + " COR = " + self.cor)
                        #~ print("atual = " + destino.idEstado + " COR = " + self.cor)
                        #~ alcancaveisDoDestino = destino.getAlcancaveis()
                        #~ for alcancavel in alcancaveisDoDestino:
                            #~ self.estadosAlcancaveis.add(alcancavel)
            #~ self.cor = "P"
            #~ return self.estadosAlcancaveis
            
    def printEstado(self):
        s = "\nID do Estado: \n"
        s += "q" + self.idEstado

        s += "\nAlcança: \n"
        for estado in self.estadosAlcancaveis:
            s += "q" + estado.idEstado + "\n"
        print(s)
                        

    #~ def getAlcancaveis(self):
        #~ if(self.cor == "B"):
            #~ self.setAlcancaveis()
        #~ return self.estadosAlcancaveis
