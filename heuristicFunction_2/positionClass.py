class Position:
    def __init__(self,position):
        """
        The function initializes an object with a position, a default piece, "_", and a default 
        dictionary of points of each piece in the position, that will be 0 for each one initially.
        
        Arguments:
            position: (line, column)
        """
        self.position = position
        self.piece = "_"
        self.points = {"X" : 0, "O" : 0, "+" : 0, "-" : 0}
    
    def resetPointsByPieceRemove(self, pieceRemove):
        """
        The function resets the points of the piece remove in a given position to zero.
        """
        self.points[pieceRemove] = 0
            
    def positionIsEmpty(self):
        """
        The function checks if the position is empty by comparing the piece at that position to "_".
        
        Returns:
            An boolean. True if the piece at the position is "_", indicating that the position
            is empty.otherwise False.
        """
        return self.piece == "_" 
    
    def positionIsSuperposeReservation(self):
        """
        The function checks if there are more than one point with a value higher than 0, to see
        if there is superpose reservation of the position.
        
        Returns:
            True if there are more than one points with a value higher
            than 0, and False otherwise.
        """
        nPtsHigherThan0 = 0
        for pts in self.points.values():
            if pts > 0:
                nPtsHigherThan0 += 1
                if nPtsHigherThan0 > 1:
                    return True
        return False
    
    def positionIsReserved(self):
        """
        The function checks if any position is reserved by summing the values of the points dictionary.
        
        Returns:
            A boolean value. True if the sum of the values in the `self.points`
            dictionary is greater than 0, indicating that at least one position is reserved. It returns
            False otherwise.
        """
        return sum(self.points.values()) > 0
    
    def __str__(self):
        """
        The function returns a string representation of an object, including its position, piece, and
        points.
        
        Returns:
            A string representation of the object, with the position, piece, and points of the object.
        """
        return f"Position: {self.position} Piece: {self.piece} Points: {self.points}"
