from boardClass import *
from piecesOutsideBoardClass import *
from removePiece import removeForms
from copy import deepcopy

class Node:
    def __init__(self, board, piecesOutside, piece = '_', position = None, listPositions = []):
        self.board = board
        self.piecesOutside = piecesOutside
        self.valuePiecePlaceOnBoard = 1/(2**self.board.valuePositionForPieceOnBoard(piece, position))
        self.heuristicValue = board.diffReservedPositLapReservedPosit() 
        self.positionsPlaced = listPositions
        self.piecePlaced = piece
        if position != None:
            self.positionsPlaced.append(position)
        
def resolveGameIAHeuristic3(listPiecesOutside):
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
            newPiecesOutside = deepcopy(currentNode.piecesOutside)
            piece = newPiecesOutside.getPieceToPutOnBoard()
            
            for position in possiblePositions:
                listNewBoards = currentNode.board.allPossibleBoardPiecePlace(newPiecesOutside.numberEachPiece[piece],piece,position)
                for board in listNewBoards:
                    frontier.append(Node(board,newPiecesOutside, piece, position, currentNode.positionsPlaced.copy()))
                    # verify if there is a form of the piece 
                    # placed on this board to be removed
                    if frontier[-1].piecePlaced != '_':
                        (boardPiecesRemoved, pointsAcquired) = removeForms(frontier[-1].board.boardAsAnMatrix(), frontier[-1].piecePlaced, frontier[-1].positionsPlaced[-1][0],  frontier[-1].positionsPlaced[-1][1])
                        if pointsAcquired > 0:
                            frontier[-1].board.removePieceFormBoard(frontier[-1].piecePlaced, boardPiecesRemoved)
            
            newPiecesOutside.pieceToPutOnBoard()
            piecesIndexes = [i + 1 for i in range(len(newPiecesOutside.listPiecesOutside)) if newPiecesOutside.listPiecesOutside[i] == piece]
            
            frontier = sorted(frontier, key=lambda node: heuristic(node, piecesIndexes) + node.valuePiecePlaceOnBoard)
            frontier = frontier[0:25]

def heuristic(node : Node, piecesIndexes : list):
    pieceSymbol = node.piecePlaced
    piecesToCompleteTheShape = len(node.board.listPositionReservedForPiece(pieceSymbol))
    numberOfPiecesOnTheReservationsSpots = node.board.numberOfPieceOnReservedPositionsOnBoard(pieceSymbol)
    
    if piecesToCompleteTheShape > 0:
        
        if len(piecesIndexes) + numberOfPiecesOnTheReservationsSpots >= piecesToCompleteTheShape:
            index = piecesToCompleteTheShape - numberOfPiecesOnTheReservationsSpots - 1
            if index < len(piecesIndexes) and index >= 0:
                movesBetweenFirstAndLastPieces = piecesIndexes[index]
                return movesBetweenFirstAndLastPieces
            else:
                return len(node.piecesOutside.listPiecesOutside)
        else:
            return len(node.piecesOutside.listPiecesOutside)
    else:
        return len(node.piecesOutside.listPiecesOutside)

print('Start')
result = resolveGameIAHeuristic3(['X', 'O', '+', '-', 'O', '-', '-', '+', '+', '+', '+', 'O', 'O', 'X', '+'])
print(result)
