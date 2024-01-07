class PiecesOutSide:
    
    def __init__(self, listPiecesOutside, numberOfPiecesRemoved = 0):
        """
        The function initializes an object with a list of pieces outside and a dictionary to keep track
        of the number of each piece.
        
        Arguments:
            listPiecesOutside : a list that contains the pieces (the following
            characters: "X", "O", "-", "+") that are outside of the game board.
        """
        self.listPiecesOutside = listPiecesOutside
        self.numberOfPiecesRemoved = numberOfPiecesRemoved
        self.numberEachPiece = {'-': listPiecesOutside.count('-'),
                                '+': listPiecesOutside.count('+'),
                                'O': listPiecesOutside.count('O'),
                                'X': listPiecesOutside.count('X')}
        
    def pieceToPutOnBoard(self):
        """
        The function removes a piece from a list of pieces outside the board,
        updates the count of that piece, and returns the removed piece.
        
        Returns:
            pieceToBePut: a char
        """
        pieceToBePut = self.listPiecesOutside.pop(0)
        self.numberEachPiece[pieceToBePut] -= 1
        self.numberOfPiecesRemoved += 1
    
    def getPieceToPutOnBoard(self):
        """
        The function returns the first piece from a list of pieces outside the board.
        
        Returns:
            pieceToPutOnBoard: a char
        """
        return self.listPiecesOutside[0]
    
    def __str__(self):
        return str(self.listPiecesOutside)