from positionClass import Position
from reservePositionBoard import *
import copy

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
    
    def emptyPositions(self):
        """
        The function returns a list of positions on the board that are empty.
        
        Returns:
            listEmptyPositions: a list of tuples, (line, column)
        """
        listEmptyPositions = [] 
        for position in self.board:
            if position.isEmpty():
                listEmptyPositions.append(position.position)
        
        return listEmptyPositions
    
    def positionOnBoard(self, position):
        """
        The function calculates the position on a board based on the given position coordinates.
        
        Arguments:
            position : (line,column)
        
        Returns:
            An integer 
        """
        return position[0] * 5 + position[1]
    
    def removePieceFormBoard(self, piece, matrix):
        """
        The function removes a specified shape piece from a board, given by the matrix 5x5
        result of that removed, by setting its points to 0 and updating the board it self. 
        
        Arguments:
            piece: a char
            matrix: a matrix 5x5
        """
        for line in range(5):
            for column in range(5):
                positionBoard = self.positionOnBoard((line,column))
                
                if self.board[positionBoard].piece == piece:
                    if matrix[line][column] == '_':
                        self.board[positionBoard].points[piece] = 0
                        self.board[positionBoard].piece = '_'
    
    def putPieceOnTheBoard(self, position, piece):
        """
        The function puts a piece on the board at a specified position and resets its points.
        
        Arguments:
            position: (line, column)
            piece: a char
        """
        indexBoard = self.positionOnBoard(position)
        self.board[indexBoard].piece = piece
    
    def putPointsOnThePositions(self, piece: chr, pattern: list[tuple[int]]):
        """
        The function assigns points to positions on a board based on the given
        piece and pattern.
        
        Arguments:
            piece: a char
            pattern: a list of tuples, where each tuple represents a position on the board
        """
        points = len(pattern)
        
        if piece == '-':
            if len(pattern) > 2:
                middlePosition = pattern[int(len(pattern)/2)]
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = points
                    if position == middlePosition:
                        self.board[self.positionOnBoard(position)].points[piece] = points-1
            else:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = points
            
        elif piece == '+' or piece == 'X':
            if len(pattern) > 5:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = points
                    if position == (2,2):
                        self.board[self.positionOnBoard(position)].points[piece] = points-1
            else:
                for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = points 

        elif piece == 'O':
            for position in pattern:
                    self.board[self.positionOnBoard(position)].points[piece] = points
    
    def reservationForPiece(self, piece):
        """
        The function checks if a given piece has a reservation on the board.
        
        Arguments: 
            piece: a char
        
        Returns:
            pieceHasReservation: a boolean
        """
        pieceHasReservation = False
        for position in self.board:
                if position.points[piece] > 0:
                    pieceHasReservation = True
        return pieceHasReservation

    def valuePositionForPieceOnBoard(self, piece, position):
        """
        The function returns the value of a position on the board for a given piece.
        
        Arguments:
            piece: a char
            position: a (line,column)
            
        Returns:
            valuePositionForPiece: an integer
        """
        if piece == '_':
            return 0
        else:
            return self.board[self.positionOnBoard(position)].valuePositionForPiece(piece)
    
    def diffReservedPositLapReservedPosit(self):
        """
        The function calculates the difference between the number of reserved positions and the number
        of positions that have overlapping reservations on a board.
        
        Returns:
            The difference between the number of reserved positions and the number of positions
        that have a superposed reservation.
        """
        
        positionsReserved = 0
        positionsSuperpose = 0
        for position in self.board:
            if position.positionIsReserved():
                positionsReserved += 1
                if position.positionIsSuperposeReservation():
                    positionsSuperpose += 1
        
        return positionsReserved - positionsSuperpose
    
    def allPossibleBoardPiecePlace(self,numberOfPieces, piece, position):
        """
        The function returns a list of all possible boards that can be
        created by placing a given number of pieces on a board at a given position.
        
        Arguments:
            numberOsPieces: a integer
            piece: a char
            position: a (line,column)
            
        Returns:
            listPossibleBoards: a list of Boards
        """
        
        listPossibleBoards = [] 
        if not self.reservationForPiece(piece):
            currentBoard = self.boardAsAnMatrix()
            listSetPossibleShape = listSetPositionForPieceForm(numberOfPieces, piece, position, currentBoard)
            if len(listSetPossibleShape) > 0:
                for reservation in listSetPossibleShape:
                    newBoard = copy.deepcopy(self)
                    newBoard.putPointsOnThePositions(piece, reservation)
                    newBoard.putPieceOnTheBoard(position,piece)
                    listPossibleBoards.append(copy.copy(newBoard))
                    newBoard = None
            else:
                newBoard = copy.deepcopy(self)
                newBoard.putPieceOnTheBoard(position,piece)
                listPossibleBoards.append(newBoard)
        else:
            newBoard = copy.deepcopy(self)
            newBoard.putPieceOnTheBoard(position,piece)
            listPossibleBoards.append(newBoard)
        
        return listPossibleBoards
            
    def __str__(self):
        board = ""
        for Position in self.board:
            board += str(Position) + "\n"
        return board

# board = Board()
# board.createInitialBoard()

# boardSons = board.allPossibleBoardPiecePlace(3,'-',(0,0))
# for son in boardSons:
#     print(son)
#     print('------------------------------')

#TODO add a tree class and node class to make the IA 
#TODO make a function to see if there is a reserved position to that type of piece, case there is put it there if not try to create a new shape, if empty put in an empty spot 