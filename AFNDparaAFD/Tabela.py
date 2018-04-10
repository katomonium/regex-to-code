class Tabela:
    def __init__(self, automato):
        self.automato = automato

    def printTabela(self):
        s = ""
        for estado in self.automato.estados:
            s += "q"+estado.idEstado + "    "
            for letra in self.automato.alfabeto:
                s += letra + "{"

            s += "\n"

        print(s)
