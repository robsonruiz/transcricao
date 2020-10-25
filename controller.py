from model import Transcricao
from view import View

class ControllerTranscricao():
    def start(self):
        fitaMolde = self.view.start()
        rnaTranscrito = self.model.transcrever(fitaMolde)
        return self.view.mostraResultado(rnaTranscrito)
        
    def __init__(self):
        self.model = Transcricao()
        self.view = View()

if __name__ == "__main__":
    main = ControllerTranscricao()
    main.start()