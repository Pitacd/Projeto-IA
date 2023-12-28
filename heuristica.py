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
            tab += str(Position) + "\n"
        return tab
    
t1= Tabuleiro()

t1.criarTabuleiroInicial()

print(t1)

class PiecesOutSide:
    def __init__(self,listOutSide):
        self.arrayListOutSide = listOutSide
        self.possibleForms = {"X":(0,0),"O":(0,0,0,0),"-":(0,0),"+":(0,0)}
        
    def nPiecesOutSide(self):
        npieces = {"X": 0, "+": 0, "-": 0, "O": 0}
        for piece in self.arrayListOutSide:
            npieces[piece] += 1
        return npieces
    
    def possibleForms(self):
        forms = self.nPiecesOutSide()
        for piece in forms:
            if forms[piece] > 0:
                if piece == "X" or piece == "+":
                    self.arrayListOutSide[piece][0] = forms[piece] / 9
                    self.arrayListOutSide[piece][1] = forms[piece] / 5
                elif piece == "-":
                    self.arrayListOutSide[piece][0] = forms[piece] / 3
                    self.arrayListOutSide[piece][1] = forms[piece] / 2
                elif piece == "O":
                    self.arrayListOutSide[piece][0] = forms[piece] / 16
                    self.arrayListOutSide[piece][1] = forms[piece] / 12
                    self.arrayListOutSide[piece][2] = forms[piece] / 8
                    self.arrayListOutSide[piece][3] = forms[piece] / 4
    
                    
                    
                    
                    
                
                    
                    
                
            
        
    