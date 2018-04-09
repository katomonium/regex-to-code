from PseudoEstado import PseudoEstado

class AutomatoFD:
    PErestantes = []
    pseudoEstados = []                  #lista de estados do automato
    estadosDic = {}               #dicionario que referencia os estados
    alfabeto = []
    inicial = None
    finais = []                   #dicionario de estados finais

    def printAFD(self):
        for PE in self.pseudoEstados:
            PE.printPE()

    def acabou(self):
        for estado in self.pseudoEstados:
            if(estado.verificado == False):
                return False
        return True

    def adicionaPE(self,PE):
        if(PE not in self.pseudoEstados):
            self.pseudoEstados.append(PE)
            self.PErestantes.append(PE)

    def estadoJaExiste(self,estados):
        for PE in self.pseudoEstados:
            if(len(PE.estados) == len(estados)):
                if all(PE.contem(estado) for estado in estados):
                    return PE
        return None

    def fundirEstadosSeNaoForamFundidos(self,estados):
        if(len(estados) == 0):
            return None
        pseudoEstado = self.estadoJaExiste(estados)
        if(pseudoEstado is not None):
            # print("ja fundiu")
            return pseudoEstado
        else:
            pseudoEstado = PseudoEstado()
            pseudoEstado.estados = estados
            pseudoEstado.setTransicoes()
            return pseudoEstado
