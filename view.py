class View():
    def start(self):
        print("\nTRANSCRIÇÃO")
        return self.getFita()

    def getFita(self):
        fitaMolde = input("Insira a fita molde: ")
        list(fitaMolde)
        return fitaMolde.upper()

    def mostraResultado(self, rnaTranscrito):
        print(rnaTranscrito)