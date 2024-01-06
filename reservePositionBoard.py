# dictionary that has an tuple with the number of pieces of 
# each type of piece to form the shapes tinny, big, mega and ultra 
# (in this sequence)
numberPieceNeedToShape = {'-' : (2,3), '+' : (5,9), 'X' : (5,9), 'O' : (4,8,12,16)}
# list that contains all the possible combinations
# to form the shape of a small minus
listPossibleSetMinusReservationSmallShape = [((line, column), (line, column + 1)) for line in range(5) for column in range(4)]
# list that contains all the possible combinations
# to form the shape of a big minus
listPossibleSetMinusReservationBigShape = [((line,column),(line,column+1),(line,column+2)) for line in range(5) for column in range(3)]
# list that contains all the possible combinations 
# to form the shape of a small plus (left,up,center,right,down)
listPossibleSetPlusReservationSmallShape = [((i,j-1),(i-1,j),(i, j),(i,j+1),(i+1,j)) for i in range(1, 4) for j in range(1, 4)]
# list that contains all the possible combinations 
# to form the shape of a big plus 
# [( down+, up, left, left+, down+, right, up+, center, down)]
listPossiblePlusReservationBigShape = [tuple(set([(2, j) for j in range(5)] + [(i, 2) for i in range(5)]))]
# list that contains all the possible combinations 
# to form the shape of a small X (left-up,right-up,center,right-down,left-down)
listPossibleSetXReservationSmallShape = [((i-1,j-1),(i-1,j+1),(i, j),(i+1,j+1),(i+1,j-1)) for i in range(1, 4) for j in range(1, 4)]
# list that contains all the possible combinations 
# to form the shape of a big X 
# [(right-down+, left-down+, right-up+, left-up+, left-down, left-up, right-down, center, right-up)]
listPossibleSetXReservationBigShape = [tuple(set([(j, j) for j in range(5)] + [(i, 4-i) for i in range(5)]))]
# list that contains all the possible combinations
# to form the shape of a small circle
listPossibleSetCircleReservationSmallShape = [((i,j),(i,j+1),(i+1,j),(i+1,j+1)) for i in range(4) for j in range(4)]
# list that contains all the possible combinations
# to form the shape of a middle circle
listPossibleSetCircleReservationMidShape = [((i,j),(i,j+1),(i,j+2),(i+1,j),(i+1,j+2),(i+2,j),(i+2,j+1),(i+2,j+2)) for i in range(3) for j in range(3)]
# list that contains all the possible combinations
# to form the shape of a big circle
listPossibleCircleReservationBigShape = [((i,j),(i,j+1),(i,j+2),(i,j+3),(i+1,j),(i+1,j+3),(i+2,j),(i+2,j+3),(i+3,j),(i+3,j+1),(i+3,j+2),(i+3,j+3)) for i in range(2) for j in range(2)]
# list that contains all the possible combinations
# to form the shape of a mega circle
listPossibleCircleReservationMegaShape = [tuple(set([(i,j) for i in range(5) for j in (0,4)] + [(i,j) for i in (0,4) for j in range(5)]))]

def listSmallShapeToUse(piece):
    """
    The function returns a list of possible small shapes to use based on the given piece.
    
    Arguments:
        piece : a char, one of the following values: '-', '+', 'X', or 'O'
        
    Returns:
        listOfPossibleSmallShapes: a list
    """
    match piece:
            case '-':
                return listPossibleSetMinusReservationSmallShape
            case '+':
                return listPossibleSetPlusReservationSmallShape
            case 'X':
                return listPossibleSetXReservationSmallShape
            case 'O':
                return listPossibleSetCircleReservationSmallShape

def listBigShapeToUse(piece):
    """
    The function returns a list of possible big shapes to use based on the given piece.
    
    Arguments:
        piece : a char, one of the following values: '-', '+', 'X', or 'O'
        
    Returns:
        listOfPossibleBigShapes: a list
    """
    match piece:
        case '-':
            return listPossibleSetMinusReservationBigShape
        case '+':
            return listPossiblePlusReservationBigShape
        case 'X':
            return listPossibleSetXReservationBigShape
        case 'O':
            return listPossibleSetCircleReservationMidShape

def possibleFormToDoInTheBoard(board, positionToPutPiece, listPossibleFormToDo, listPossibleSetReservationShape):
    """
    The function checks if a list of possible reservations can be made on a board by removing any
    reservations that have occupied positions.
    
    Arguments:
        board: a matrix 5x5
        positionToPutPiece: a (line,column)
        listPossibleFormToDo: a list 
        listPossibleSetReservationShape: a list
    """
    for possibleSetReservation in listPossibleSetReservationShape:
            positionIsThere = False
            positionHasPiece = False
            
            for position in possibleSetReservation:
                if board[position[0]][position[1]] != '_':
                    positionHasPiece = True
                    break
                if position == positionToPutPiece:
                    positionIsThere = True
            
            if not positionIsThere or positionHasPiece:
                listPossibleFormToDo.remove(possibleSetReservation)

def listSetPositionForPieceForm(numberOfPieces, piece, position, board):
    """
    The function returns a list of possible set positions for a given
    piece on a board, based on the number of available pieces and the shape of the piece.
    
    Arguments:
        numberOfPieces: an integer
        piece: a char
        position: a (line,column)
        board: a matrix 5x5
    """
    listPossibleSetReservation = []
    numberPiecePerShape = numberPieceNeedToShape[piece]

    if numberOfPieces >= numberPiecePerShape[0]:

        listSmallShape = listSmallShapeToUse(piece)
        listPossibleSetReservation += listSmallShape.copy()

        possibleFormToDoInTheBoard(board, position, listPossibleSetReservation, listSmallShape)

    if numberOfPieces >= numberPiecePerShape[1]:

        listBigShape = listBigShapeToUse(piece)
        listPossibleSetReservation += listBigShape.copy()

        possibleFormToDoInTheBoard(board, position, listPossibleSetReservation, listBigShape)

    if piece == 'O':
        if numberOfPieces >= numberPiecePerShape[2]:
            listPossibleSetReservation += listPossibleCircleReservationBigShape.copy()

            possibleFormToDoInTheBoard(board, position, listPossibleSetReservation, listPossibleCircleReservationBigShape)

        if numberOfPieces >= numberPiecePerShape[3]:
            listPossibleSetReservation += listPossibleCircleReservationMegaShape.copy()

            possibleFormToDoInTheBoard(board, position, listPossibleSetReservation, listPossibleCircleReservationMegaShape)

    return listPossibleSetReservation
