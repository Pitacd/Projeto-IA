from positionClass import Position

class Board:
    def __init__(self, board = []):
        """
        The constructor for the class and initializes a board that is empty.
        """
        self.board = board
        
    def createInitialBoard(self):
        """
        The function creates an initial board by appending positions to a list.
        """
        for line in range(5):
            for column in range(5):
               self.board.append(Position((line,column)))

    def positionOnBoard(self, position):
        """
        The function calculates the position on a board based on the given position coordinates.
        
        Arguments:
            position : (line,column)
        
        Returns:
            An integer 
        """
        return position[0] * 5 + position[1]
    
    def putPieceOnTheBoard(self, position, piece):
        """
        The function puts a piece on the board at a specified position and resets its points.
        
        Arguments:
            position: (line, column)
            piece: a char
        """
        indexBoard = self.positionOnBoard(position)
        self.board[indexBoard].piece = piece

    def boardValueByTheHeuristic2(self):
        """
        The function calculates the board value given by the heuristic 2.
        
        Returns:
            An integer. The difference between the number of reserved positions 
            on the board and the number of positions that have a superposed reservation.
        """
        
        positionsReserved = 0
        positionsSuperpose = 0
        for position in self.board:
            if position.positionIsReserved():
                positionsReserved += 1
                if position.positionIsSuperposeReservation():
                    positionsSuperpose += 1
        
        return positionsReserved - positionsSuperpose
        
    def __str__(self):
        board = ""
        for Position in self.board:
            board += str(Position) + "\n"
        return board