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

# Use of Algorithm A* 
# f(x) = g(x) + h(x) 
# g(x) = value of piece on board
# h(x) = number positions reserved on board that are not overlap     
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
    i = 0
    
    while frontier != []:
        
        # remove the best node from the frontier
        currentNode = frontier.pop(0)
        possiblePositions = currentNode.board.emptyPositions()
        
        if len(possiblePositions) <= 0 or len(currentNode.piecesOutside.listPiecesOutside) <= 0:
            print(i)
            print(currentNode.board.boardAsAnMatrix())
            return currentNode.positionsPlaced
        else:
            newPiecesOutside = deepcopy(currentNode.piecesOutside)
            piece = newPiecesOutside.getPieceToPutOnBoard()
            
            # expand all the nodes possible 
            # through the best node
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
            
            # remove the piece from the list of pieces outside
            newPiecesOutside.pieceToPutOnBoard()
            # sort the frontier through the heuristic function 
            frontier = sorted(frontier, key=lambda node: node.costValue + node.board.diffReservedPositLapReservedPosit(), reverse=True)
            # update frontier only to contain the best 25 nodes
            frontier = frontier[0:25]
            i+=1

# print('Start')          
# result = resolveGameIAHeuristic2(['X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'X', '-', '-', 'O', 'O', '-', 'X', 'X', 'X', 'X', '-', '-', '+', 'O', 'O', 'O', 'O'])
# print(result)