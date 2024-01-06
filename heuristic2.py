from boardClass import *
from piecesOutsideBoardClass import *
from reservePositionBoard import *
from removePiece import removeForms

class Node:
    def __init__(self, parent, board, piecesOutside, piece = '_', position = None):
        self.board = board
        self.piecesOutside = piecesOutside
        self.costValue = piecesOutside.getNumberPiecesRemoved() + board.valuePositionForPieceOnBoard(piece, position)
        self.heuristicValue = board.diffReservedPositLapReservedPosit()
        self.positionPlaced = position
        self.parent = parent

# create the frontier
frontier = []

# initialize the board with a empty board
startBoard = Board()
startBoard.createInitialBoard()
#! make a function to give in the main after read colors
#! the list of pieces outside
startPiecesOutside = PiecesOutSide(['-','+','-'])
# create the first node
root = Node(None, startBoard, startPiecesOutside)

print(root.piecesOutside)

