class Position:
    def __init__(self,pos,piece,pon):
        self.pos = pos
        self.piece = piece
        self.pon = pon
    def __str__(self):
        return f"{self.pos}{self.piece}{self.pon}"

class Tabuleiro:
    def __init__(self):
        self.tab = []
    def criarTabuleiroInicial(self):
        for linha in range(5):
            for coluna in range(5):
               self.tab.append(Position((linha,coluna),"_",(0,0,0,0)))

    def calcular_pontuacao(self):
        pontuacao_total = 0
        for peca in self.tab:
            if peca.piece == "_":
                pontuacao_total += max(peca.pon)*2 - sum(peca.pon)
        return pontuacao_total

    def __str__(self):
        tab = ""
        for Position in self.tab:
            tab += str(Position) + "\n"
        return tab
    
t1= Tabuleiro()

t1.criarTabuleiroInicial()

print(t1)
print(t1.calcular_pontuacao())