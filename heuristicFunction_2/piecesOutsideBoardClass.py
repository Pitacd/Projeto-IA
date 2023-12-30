class PiecesOutSide:
    
    def __init__(self, listPiecesOutside):
        """
        The function initializes an object with a list of pieces outside and a dictionary to keep track
        of the number of each piece.
        
        Arguments:
            listPiecesOutside : a list that contains the pieces (the following
            characters: "X", "O", "-", "+") that are outside of the game board.
        """
        self.listPiecesOutside = listPiecesOutside
        self.numberOfEachPiece = {"X": 0, "O": 0, "-": 0, "+": 0}
        
        self.initialPiecesOutSide()
        
    def initialPiecesOutSide(self):
        """
        The function increments the count of each piece in the list of pieces outside.
        """
        for piece in self.listPiecesOutside:
            self.numberOfEachPiece[piece] += 1
    
    def pieceToPutOnBoard(self):
        """
        The function removes a piece from a list of pieces outside the board,
        updates the count of that piece, and returns the removed piece.
        
        Returns:
            pieceToBePut: a char
        """
        pieceToBePut = self.listPiecesOutside.pop()
        self.numberOfEachPiece[pieceToBePut] -= 1
        return pieceToBePut
    
    def getPieceToPutOnBoard(self):
        """
        The function returns the first piece from a list of pieces outside the board.
        
        Returns:
            pieceToPutOnBoard: a char
        """
        return self.listPiecesOutside[0]