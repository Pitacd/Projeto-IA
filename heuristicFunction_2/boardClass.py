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
               
    def boardAsAnMatrix(self):
        """
        The function converts a board represented as a list into a matrix
        representation.
        Returns:
            matrixBoard: an 5x5
        """
        matrixBoard = []
        boardLineList = []
        for position in self.board:
            boardLineList.append(position.piece)
            if len(boardLineList) > 4:
                matrixBoard.append(boardLineList.copy())
                boardLineList.clear()
        
        return matrixBoard

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
    
    def putPointsOnThePositions(self, piece: chr, pattern: list[tuple[int]]):
        """
        The function assigns points to positions on a board based on the given
        piece and pattern.
        
        Arguments:
            piece: a char
            pattern: a list of tuples, where each tuple represents a position on the board
        """
        
        if piece == '-':
            if len(pattern) > 2:
                middlePosition = pattern[int(len(pattern)/2)]
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = 2
                    if position == middlePosition:
                        self.board[self.positionOnBoard(position)].points[piece] = 1
            else:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = 1
            
        elif piece == '+' or piece == 'X':
            if len(pattern) > 5:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = 2
                    if position == (2,2):
                        self.board[self.positionOnBoard(position)].points[piece] = 1
            else:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = 1

        elif piece == 'O':
            for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = 1
    
    def reservationForPiece(self, piece):
        """
        The function returns a list of positions on the board where a given piece
        can be reserved.
        
        Arguments:
            piece: a char
            
        Returns:
            listReservationPiece: a list of tuples
        """
        listReservationPiece = []
        for position in self.board:
                if position.points[piece] > 0:
                    if position.positionIsEmpty():
                        listReservationPiece.append(position.position)
        return listReservationPiece
                
    
    def __str__(self):
        board = ""
        for Position in self.board:
            board += str(Position) + "\n"
        return board

board = Board()
board.createInitialBoard()
board.putPointsOnThePositions('-', [(0,1),(0,2),(0,3)])
print(board.reservationForPiece('-'))
    
#TODO add a tree class and node class to make the IA 
#TODO make a function to put the piece in a position with a value higher than 0 for that type 
#TODO make a function to increase the position points for each piece put in that shape (dot make sense now)
#TODO make a function to clean the points in the positions with the pieces removed
#TODO make a function to see if there is a reserved position to that type of piece, case there is put it there if not try to create a new shape, if empty put in an empty spot 