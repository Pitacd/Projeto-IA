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
               
    def __str__(self):
        tab = ""
        for Position in self.tab:
            tab += str(Position)
        return tab
    
t1= Tabuleiro()

t1.criarTabuleiroInicial()

print(t1)

def calcular_pontuacao(Tabuleiro):
    pontuacao_total = 0
     for linha in tabuleiro:
       for peca in linha:
           if peca == 0:
               pontuacao_total +=1
               pontuacao_maxima = len(Tabuleiro) * len(Tabuleiro[0])
               pontos_restantes = pontuacao_total - pontuacao_maxima
               return pontos_restantes
           resultado = calcular_pontuacao(Tabuleiro)
           print("Pontos restantes depois de subtrair a pontuação máxima:",resultado)