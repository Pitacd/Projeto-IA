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
    
    def __str__(self):
        """
        The function returns a string representation of an object, including its position, piece, and
        points.
        
        Returns:
            A string representation of the object, with the position, piece, and points of the object.
        """
        return f"Position: {self.position} Piece: {self.piece} Points: {self.points}"

class Board:
    def __init__(self):
        """
        The constructor for the class and initializes a board that is empty.
        """
        self.board = []
        
    def createInitialBoard(self):
        """
        The function creates an initial board by appending positions to a list.
        """
        for line in range(5):
            for column in range(5):
               self.board.append(Position((line,column)))

    def boardPoints(self):
        """
        The function calculates the total points on a game board based on points on each position that are empty
        subtracting the higher value by the rest of the points.
        
        Returns:
            totalPoints: an integer
        """
        totalPoints = 0
        for position in self.board:
            if position.piece == "_":
                listPointsInPosition = position.points.values()
                totalPoints += max(listPointsInPosition)*2 - sum(listPointsInPosition)
        return totalPoints

    def __str__(self):
        board = ""
        for Position in self.board:
            board += str(Position) + "\n"
        return board
    
t1= Board()

t1.createInitialBoard()

print(t1)
print(t1.boardPoints())