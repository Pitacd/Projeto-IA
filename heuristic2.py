from boardClass import *
from piecesOutsideBoardClass import *
from removePiece import removeForms
from copy import deepcopy

class Node:
    def __init__(self, board, piecesOutside, piece = '_', position = None, listPositions = [], dadCostValue = 0):
        self.board = board
        self.piecesOutside = piecesOutside
        self.costValue = 1 + board.valuePositionForPieceOnBoard(piece, position) + dadCostValue 
        self.positionsPlaced = listPositions
        self.piecePlaced = piece
        if position != None:
            self.positionsPlaced.append(position)
        
def resolveGameIAHeuristic2(listPiecesOutside):
    # create the frontier
    frontier = []

    # initialize the board with a empty board
    startBoard = Board()
    startBoard.createInitialBoard()
    startPiecesOutside = PiecesOutSide(listPiecesOutside)
    # create the first node
    rootNode = Node(startBoard, startPiecesOutside)
    frontier.append(rootNode)
    
    while frontier != []:
        
        currentNode = frontier.pop(0)
        possiblePositions = currentNode.board.emptyPositions()
        
        if len(possiblePositions) <= 0 or len(currentNode.piecesOutside.listPiecesOutside) <= 0:
            print(currentNode.board.boardAsAnMatrix())
            return currentNode.positionsPlaced
        else:
            newPiecesOutside = deepcopy(currentNode.piecesOutside, {})
            piece = newPiecesOutside.getPieceToPutOnBoard()
            
            for position in possiblePositions:
                listNewBoards = currentNode.board.allPossibleBoardPiecePlace(newPiecesOutside.numberEachPiece[piece],piece,position)
                for board in listNewBoards:
                    frontier.append(Node(board,newPiecesOutside, piece, position, currentNode.positionsPlaced.copy(), currentNode.costValue))
                    # verify if there is a form of the piece 
                    # placed on this board to be removed
                    if frontier[-1].piecePlaced != '_':
                        (boardPiecesRemoved, pointsAcquired) = removeForms(frontier[-1].board.boardAsAnMatrix(), frontier[-1].piecePlaced, frontier[-1].positionsPlaced[-1][0],  frontier[-1].positionsPlaced[-1][1])
                        if pointsAcquired > 0:
                            frontier[-1].board.removePieceFormBoard(frontier[-1].piecePlaced, boardPiecesRemoved)
            
            newPiecesOutside.pieceToPutOnBoard()
            frontier = sorted(frontier, key=lambda node: node.costValue + node.board.diffReservedPositLapReservedPosit(), reverse=True)
            frontier = frontier[0:25]
            
# result = resolveGameIAHeuristic2(['-', '-', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', '+', 'O', '+', '+', 'O', '-', 'O', 'O', '+', '+'])
# print(result)