import copy

class Position:
    def __init__(self,position, piece = '_', points = None):
        """
        The function initializes an object with a position, a default piece, "_", and a default 
        dictionary of points of each piece in the position, that will be 0 for each one initially.
        
        Arguments:
            position: (line, column)
        """
        self.position = position
        self.piece = piece
        if points == None:
            self.points = {"X" : 0, "O" : 0, "+" : 0, "-" : 0}
        else:
            self.points = points
        
    def __deepcopy__(self, memo):
        new_instance = self.__class__(copy.deepcopy(self.position, memo),
                                    copy.deepcopy(self.piece, memo),
                                    copy.deepcopy(self.points, memo))
        return new_instance
    
    def resetPointsByPieceRemove(self, pieceRemove):
        """
        The function resets the points of the piece remove in a given position to zero.
        """
        self.points[pieceRemove] = 0
            
    def isEmpty(self):
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
    
    def valuePositionForPiece(self, piece):
        """
        The function returns the position value of a given piece based on a dictionary of points.
        
        Arguments:
            piece: a char
            
        Returns:
            totalPoints: an integer
        """
        return self.points[piece] * 3 - sum(self.points.values()) 
        
    # def __str__(self):
    #     return f'{self.position} : {self.piece} -> {self.points}'