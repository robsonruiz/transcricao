class Transcricao():
    def transcrever(self, fitaMolde):
        rnaTranscrito = []
        for i in fitaMolde:
            if(i=='A'):
                rnaTranscrito.append('U')
            elif(i=='T'):
                rnaTranscrito.append('A')
            elif(i=='C'):
                rnaTranscrito.append('G')
            elif(i=='G'):
                rnaTranscrito.append('C')
            else:
                print("Fita molde inválida")
                rnaTranscrito = []
                break
        rnaTranscrito = "".join(rnaTranscrito)
        return rnaTranscrito