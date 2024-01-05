def getPossibleShapesBySymbol(board : list[list[chr]], symbol: chr, pattern : list[tuple[int]]):
    """
    The function returns a list of all the possible shapes that can be 
    done from the given board. Each shape is represented as a list of 
    positions, created by a given pattern. A pattern is a list of the 
    positions relative to the top-left corner of the shape. Ex. [(0,0),
    (0,1), (1,0), (1,1)] represents the small circle shape.
    
    Arguments: 
        board: a matrix on which to check the possible shapes
        pattern: a list of the positions relative to the top-leftmost 
        point of the shape
        symbol: the symbol of the pieces to make the shape

    Returns:
        possibleShapes: a list of all the possible shapes that can be 
        done from the given board, symbol and pattern.
    """

    # get the size of the size of the shape
    length = max([x for (x,y) in pattern]) + 1
    height = max([y for (x,y) in pattern]) + 1

    # get all the possible pivots that can hold shapes
    allPossiblePivotPositions = [
        (x,y) for x in range(len(board)) 
            for y in range(len(board[x]))
                if (0 <= x and x <= len(board) - length) and (0 <= y and y <= len(board[x]) - height)
    ]

    # apply the pattern for all the possible pivots and
    # get the shape as a set of it's pieces' positions
    possibleShapes = []
    for (x, y) in allPossiblePivotPositions:
        shape = []
        for (i, j) in pattern:
            shape += [(x + i, y + j)]
        possibleShapes += [shape]
    
    i = 0
    while i < len(possibleShapes):
        exists = False;
        forAll = True;
        for (x,y) in possibleShapes[i]:
            exists = exists or board[x][y] == symbol
            forAll = forAll and (board[x][y] == symbol or board[x][y] == '_')
        if not (exists and forAll):
            del possibleShapes[i]
            i -= 1
        i += 1
    
    return possibleShapes

def getPossibleShapesOfBoard(board : list[list[chr]], piecesOutside : list[chr]):
    """
    The function returns a dictionary that maps each piece symbol with all the
    possible shapes that can be done with the given board and the available pieces 
    outside. By default, priorizes the largest shapes.

    Arguments: 
        board: a matrix on which to check the possible shapes
        piecesOutside : a list of the current pieces available to make shapes with

    Returns:
        possibleShapes: a dictionary that maps each piece symbol with all the
        possible shapes
    """
    shapePatterns = {
        'X' : [
            [(0,0), (0,4), (4,4), (4,0), (1,1), (1,3), (3,3), (3,1), (2,2)],
            [(0,0), (1,1), (2,2), (2,0), (0,2)],
        ],
        'O' : [
            [(0,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (3,0), (2,0), (1,0)],
            [(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3), (3,2), (3,1), (3,0), (2,0), (1,0)],
            [(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0)],
            [(0,0), (0,1), (1,0), (1,1)],
        ],
        '-' : [
            [(0,0), (0,1), (0,2)],
            [(0,0), (0,1)],
        ],
        '+' : [
            [(0,2), (1,2), (2,2), (3,2), (4,2), (2,0), (2,1), (2,3), (2,4)],
            [(0,1), (1,1), (2,1), (1,0), (1,2)],
        ],
    }

    possibleShapes = {}
    for symbol in shapePatterns:
        # buffer variables
        patterns = shapePatterns[symbol]
        possibleShapesOfCurrentSymbol = []
        possibleShapes[symbol] = []

        # initialize value of number of available pieces
        availablePieces = piecesOutside.count(symbol)
        for pattern in patterns: 
            # get the number of possible shapes
            neededPieces = len(pattern)
            numPossibleShapes = availablePieces // neededPieces
            # update the number of available pieces according to the amount of possible shapes
            availablePieces -= neededPieces * numPossibleShapes

            # add the shape if there's enough pieces
            if(numPossibleShapes > 0):
                possibleShapesOfCurrentSymbol += getPossibleShapesBySymbol(board, symbol, pattern)

        possibleShapes[symbol] += possibleShapesOfCurrentSymbol 

    return possibleShapes