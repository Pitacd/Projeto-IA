from boardClass import *
from piecesOutsideBoardClass import *
from reservePositionBoard import *
from brain import listPiecesOutside
from removePiece import removeForms

# create the frontier
frontier = []

# initialize the board with a empty board
startBoard = Board()
startBoard.createInitialBoard()
# initialize the list with pieces outside
# given by robot, read it by the sensor 
startLisPiecesOutside = PiecesOutSide(listPiecesOutside)

valueOfThisInitialNode = startLisPiecesOutside.getNumberPiecesRemoved() + startBoard.diffReservedPositLapReservedPosit() #+ startBoard.valuePositionForPieceOnBoard()


