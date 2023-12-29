class PiecesOutSide:
    
    def __init__(self, listPiecesOutSide):
        self.listPiecesOutside = listPiecesOutSide
        self.numberOfEachPiece = {"X": 0, "O": 0, "-": 0, "+": 0}
        
    def initialPiecesOutSide(self):
        for piece in self.listPiecesOutside:
            self.numberOfEachPiece[piece] += 1
    
    def pieceToPutOnBoard(self):
        pieceToBePut = self.listPiecesOutside.pop()
        self.numberOfEachPiece[pieceToBePut] -= 1
        return pieceToBePut