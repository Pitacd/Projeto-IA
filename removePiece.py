# variables that represents
# each piece on the board 
minusPiece = "-"
plusPiece = "+"
xPiece = "X"
oPiece = "O"
# variable that represents 
# a position without pieces 
blankSpot = "_"

# variable that indicates which
# form to remove for each piece type (+,-,X,O) 
# 0 indicates that there is nothing to be removed 
# higher than 0 indicates the form to remove in the respective piece type
whichFormRemove = 0 

def removeForms(board, piece, line, column): #returns [bWithAlterations,points]
    """
    The function places a piece on the board, at the position given by 
    the line and column, and then verify if with that piece a shape was form,
    removing that shape from the board.
    
    Arguments:
        board: an matrix 5x5
        piece: an char ('+','-','O','X')
        line: an integer
        column: an integer
    
    Returns:
        boardPoints: [board, points] 
    """
    board[line][column] = piece
    
    if piece == minusPiece:
        return verifyMinus(board, line, column)
    elif piece == plusPiece:
        return verifyPlus(board)
    elif piece == xPiece:
        return verifyX(board)
    elif piece == oPiece:
        return verifyCircle(board)
    else:
        print("Piece doesnt exist.\n")
        return [board,0]

#---------------------------------------//----------------------------------------------- 
# "-" piece 

def verifyMinus(board, line, column):
    """
    The function checks if there are adjacent minus pieces in a line in a given board and updates
    the board accordingly, returning the updated board and the number of points earned.
    
    Arguments:
        board: an matrix 5x5
        line: an integer
        column: an integer
    
    Returns:
        boardPoints: [board, points] 
    """
    points = 0
    numberOfMinus = 1
    
    if not column == 0:
        if board[line][column-1] == minusPiece:
            board[line][column-1] = blankSpot
            numberOfMinus += 1
            
    if not column == 4:
        if board [line][column+1] == minusPiece:
            board[line][column+1] = blankSpot
            numberOfMinus += 1
            
    if not numberOfMinus == 1:
        board[line][column] = blankSpot
        points += 2**numberOfMinus
        
    return [board,points]

#---------------------------------------//----------------------------------------------- 
# "+" piece 

def verifyPlus(board):
    """
    The function checks if a given board has a big plus or a small plus shape, removes the
    plus shape from the board, and returns the modified board along with the corresponding points
    earned.

    Arguments:
        board: an matrix 5x5
    
    Returns:
        boardPoints: [board, points] 
    """
    points = 0
    
    if isBigPlus(board):
        removeBigPlus(board)
        points += 2**9

    elif isSmallPlus(board):
        removeSmallPlus(board)
        points += 2**5
        
    return [board,points]

def isBigPlus(board):
    """
    The function checks if a specific pattern (a big plus) is present on a given board.
    
    Arguments:
        board: an matrix 5x5
    
    Returns:
        haveBigPlus: an bool
    """
    return (board[2][0] == plusPiece and 
            board[2][1] == plusPiece and 
            board[2][2] == plusPiece and 
            board[2][3] == plusPiece and 
            board[2][4] == plusPiece and 
            board[0][2] == plusPiece and 
            board[1][2] == plusPiece and 
            board[3][2] == plusPiece and 
            board[4][2] == plusPiece)

def removeBigPlus(board):
    """
    The function removes a big plus shape from a given board by replacing certain elements with a blank
    spot.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutBigPlus: an matrix 5x5
    """
    board[2] = [blankSpot,blankSpot,blankSpot,blankSpot,blankSpot]
    board[0][2] = blankSpot
    board[1][2] = blankSpot
    board[3][2] = blankSpot
    board[4][2] = blankSpot
    return board

def isSmallPlus(board):
    """
    The function checks, from left to right and top to bottom, if there is a small plus form on the given 
    board and returns the number of the form to remove if found.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        formToBeRemove: an integer
    """
    global whichFormRemove
    whichFormRemove = 0
    
    # indicates with a number which form to remove 
    formToRemove = 0
    
    # list with the positions on the board 
    # of the middle piece of the possible forms 
    possibleSmall=[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]  
    
    for p in possibleSmall:
        formToRemove += 1
        
        if (board[p[0]][p[1]] == plusPiece and 
            board[p[0]+1][p[1]] == plusPiece and 
            board[p[0]-1][p[1]] == plusPiece and 
            board[p[0]][p[1]+1] == plusPiece and
            board[p[0]][p[1]-1] == plusPiece):
            
            whichFormRemove = formToRemove
            break
        
    return whichFormRemove

def removeSmallPlus(board):
    """
    The function takes a board as input and removes a small plus shape from the board
    by replacing the corresponding positions with a blank spot.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutSmallPuls: an matrix 5x5
    """
    # list with the positions on the board 
    # of the middle piece of the possible forms 
    possibleSmall = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    
    # indicates what is the position 
    # of the middle piece of the form to be removed
    p = possibleSmall[whichFormRemove-1]
    
    board[p[0]][p[1]] = blankSpot
    board[p[0]+1][p[1]] = blankSpot
    board[p[0]-1][p[1]] = blankSpot
    board[p[0]][p[1]+1] = blankSpot
    board[p[0]][p[1]-1] = blankSpot
    
    return board

#---------------------------------------//----------------------------------------------- 
# "X" piece 

def verifyX(board):
    """
    The function checks if a given board contains a big X or a small X, removes the X from the
    board, and returns the modified board along with the corresponding points earned.
    
    Arguments:
        board: an matrix 5x5
    
    Returns:
        boardPoints: [board, points] 
    """
    points = 0
    
    if isBigX(board):
        removeBigX(board)
        points += 2**9
    elif isSmallX(board):
        removeSmallX(board)
        points += 2**5
    
    return [board,points]

def isBigX(board):
    """
    The function checks if the board has a big X pattern consisting of xPiece.
    
    Arguments:
        board: an matrix 5x5
    
    Returns:
        haveBigX: an bool
    """
    return (board[0][0] == xPiece and 
            board[1][1] == xPiece and 
            board[2][2] == xPiece and 
            board[3][3] == xPiece and 
            board[4][4] == xPiece and 
            board[0][4] == xPiece and 
            board[1][3] == xPiece and 
            board[3][1] == xPiece and 
            board[4][0] == xPiece)
    
def removeBigX(board):
    """
    The function removes the "X" characters from specific positions on the board 
    replacing it with blankSpots.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutBigX: an matrix 5x5
    """
    board[0][0]=blankSpot
    board[1][1]=blankSpot
    board[2][2]=blankSpot
    board[3][3]=blankSpot
    board[4][4]=blankSpot 
    board[0][4]=blankSpot
    board[1][3]=blankSpot
    board[3][1]=blankSpot
    board[4][0]=blankSpot
    
    return board

def isSmallX(board):
    """
    The function checks, from left to right and top to bottom, if there is a small X shape
    formed by the X pieces on a given board and returns the number of the form to remove if found.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        formToBeRemove: an integer
    """
    global whichFormRemove
    whichFormRemove=0
    
    # indicates with a number which form to remove
    formToRemove = 0
    
    # list with the positions on the board 
    # of the middle piece of the possible forms 
    possibleSmall = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]  
    
    for p in possibleSmall:
        formToRemove += 1
        
        if (board[p[0]][p[1]] == xPiece and 
            board[p[0]-1][p[1]-1] == xPiece and 
            board[p[0]-1][p[1]+1] == xPiece and 
            board[p[0]+1][p[1]-1] == xPiece and 
            board[p[0]+1][p[1]+1] == xPiece):
            whichFormRemove=formToRemove
            break
        
    return whichFormRemove

def removeSmallX(board):
    """
    The function takes a board as input and removes a small X shape from the board by
    replacing the corresponding positions with a blank spot.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutSmallX: an matrix 5x5
    """
    
    # list with the positions on the board 
    # of the middle piece of the possible forms 
    possibleSmall = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    
    # indicates what is the position 
    # of the middle piece of the form to be removed
    p = possibleSmall[whichFormRemove-1]
    
    board[p[0]][p[1]] = blankSpot
    board[p[0]-1][p[1]-1] = blankSpot
    board[p[0]-1][p[1]+1] = blankSpot
    board[p[0]+1][p[1]-1] = blankSpot
    board[p[0]+1][p[1]+1] = blankSpot
    
    return board

#---------------------------------------//----------------------------------------------- 
# "O" piece 

def verifyCircle(board):
    """
    The function takes a board as input and checks if it contains a mega circle, big
    circle, mid circle, or small circle, and returns the updated board and the corresponding points.
    
    Arguments:
        board: an matrix 5x5
    
    Returns:
        boardPoints: [board, points] 
    """
    points=0
    
    if isMegaCircle(board): # if is MEGA, 5x5  16pieces
        board = removeMegaCircle(board)
        points += 2**16
    elif isBigCircle(board):# if is BIG, 4x4  12pieces
        board = removeBigCircle(board)
        points += 2**12
    elif isMidCircle(board):# if is MID, 3x3  8pieces
        board = removeMidCircle(board)
        points += 2**8
    elif isSmallCircle(board):# if is SMALL, 2x2  4pieces
        removeSmallCircle(board)
        points += 2**4
    
    return [board,points]

def isMegaCircle(board):
    """
    The function checks if a specific pattern of "O" pieces is present on a 5x5 board.
    
    Arguments:
        board: an matrix 5x5
    
    Returns:
        haveMegaCircle: an bool
    """

    return (board[0][0] == oPiece and 
            board[0][1] == oPiece and 
            board[0][2] == oPiece and 
            board[0][3] == oPiece and 
            board[0][4] == oPiece and 
            board[1][0] == oPiece and 
            board[2][0] == oPiece and 
            board[3][0] == oPiece and 
            board[4][0] == oPiece and 
            board[4][1] == oPiece and 
            board[4][2] == oPiece and
            board[4][3] == oPiece and 
            board[4][4] == oPiece and
            board[3][4] == oPiece and
            board[2][4] == oPiece and 
            board[1][4] == oPiece)

def removeMegaCircle(board):
    """
    The function removes a "mega circle" from a given board by replacing certain elements with a blank
    spot.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutMegaCircle: an matrix 5x5
    """
    board[0] = [blankSpot,blankSpot,blankSpot,blankSpot,blankSpot]
    board[4] = [blankSpot,blankSpot,blankSpot,blankSpot,blankSpot]
    board[1][0] = blankSpot
    board[2][0] = blankSpot
    board[3][0] = blankSpot
    board[1][4] = blankSpot
    board[2][4] = blankSpot
    board[3][4] = blankSpot
    
    return board

def isBigCircle(board):
    """
    The function checks, from left to right and top to bottom, if there is a big circle formed 
    by the 'o' pieces on the board and returns the number indicating which form to remove.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        formToBeRemove: an integer
    """
    global whichFormRemove
    whichFormRemove = 0
    
    # indicates with a number which form to remove
    formToRemove = 0
    # list with the positions on the board 
    # of the left top 'O' piece in a big form of this piece
    possibleBig = [[0,0],[0,1],[1,0],[1,1]]
    
    for p in possibleBig:
        formToRemove += 1
        if (board[p[0]][p[1]] == oPiece and 
            board[p[0]][p[1]+1] == oPiece and
            board[p[0]][p[1]+2] == oPiece and
            board[p[0]][p[1]+3] == oPiece and
            board[p[0]+1][p[1]] == oPiece and 
            board[p[0]+2][p[1]] == oPiece and
            board[p[0]+3][p[1]] == oPiece and 
            board[p[0]+3][p[1]+1] == oPiece and
            board[p[0]+3][p[1]+2] == oPiece and 
            board[p[0]+3][p[1]+3] == oPiece and
            board[p[0]+2][p[1]+3] == oPiece and
            board[p[0]+1][p[1]+3] == oPiece):
            
            whichFormRemove = formToRemove
            break
    return whichFormRemove

def removeBigCircle (board):
    """
    The function takes a board as input and removes a big circle shape from the board.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutBigCircle: an matrix 5x5
    """
    # list with the positions on the board 
    # of the left top 'O' piece in a big form of this piece
    possibleBig = [[0,0],[0,1],[1,0],[1,1]]
    
    # indicates what is the position 
    # of the left top 'O' piece in a big form of this piece
    p = possibleBig[whichFormRemove-1]
    
    board[p[0]][p[1]] = blankSpot
    board[p[0]][p[1]+1] = blankSpot
    board[p[0]][p[1]+2] = blankSpot
    board[p[0]][p[1]+3] = blankSpot
    board[p[0]+1][p[1]] = blankSpot
    board[p[0]+2][p[1]] = blankSpot
    board[p[0]+3][p[1]] = blankSpot
    board[p[0]+3][p[1]+1] = blankSpot
    board[p[0]+3][p[1]+2] = blankSpot
    board[p[0]+3][p[1]+3] = blankSpot
    board[p[0]+2][p[1]+3] = blankSpot
    board[p[0]+1][p[1]+3] = blankSpot
    
    return board

def isMidCircle(board):
    """
    The function checks, from left to right and top to bottom, if there is a specific pattern 
    of 'O' pieces in a 3x3 grid on the board and returns the number of the form to remove 
    if the pattern is found.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        formToBeRemove: an integer
    """
    global whichFormRemove
    whichFormRemove = 0

    # indicates with a number which form to remove
    formToRemove = 0
    # list with the positions on the board 
    # of the left top 'O' piece in a mid form of this piece
    possibleMid=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    
    for p in possibleMid:
        formToRemove += 1
        if (board[p[0]][p[1]] == oPiece and 
            board[p[0]][p[1]+1] == oPiece and
            board[p[0]][p[1]+2] == oPiece and 
            board[p[0]+1][p[1]] == oPiece and
            board[p[0]+2][p[1]] == oPiece and 
            board[p[0]+2][p[1]+1] == oPiece and 
            board[p[0]+2][p[1]+2] == oPiece and 
            board[p[0]+1][p[1]+2] == oPiece):
            whichFormRemove = formToRemove
            break
    return whichFormRemove

def removeMidCircle (board):
    """
    The function takes a board as input and removes a specific form of the 'O' piece
    from the board.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutMidCircle: an matrix 5x5
    """
    # list with the positions on the board 
    # of the left top 'O' piece in a mid form of this piece
    possibleMid = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    # indicates what is the position 
    # of the left top 'O' piece in a mid form of this piece
    p = possibleMid[whichFormRemove-1]
    
    board[p[0]][p[1]] = blankSpot
    board[p[0]][p[1]+1] = blankSpot
    board[p[0]][p[1]+2] = blankSpot
    board[p[0]+1][p[1]] = blankSpot
    board[p[0]+2][p[1]] = blankSpot
    board[p[0]+2][p[1]+1] = blankSpot
    board[p[0]+2][p[1]+2] = blankSpot
    board[p[0]+1][p[1]+2] = blankSpot
    
    return board

def isSmallCircle(board):
    """
    The function checks, from left to right and top to bottom, if there is a small circle formed 
    by 'O' pieces in a given board and returns the number of the form to remove if found.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        formToBeRemove: an integer
    """
    global whichFormRemove
    whichFormRemove = 0
    
    # indicates with a number which form to remove
    formToRemove = 0
    # list with the positions on the board 
    # of the left top 'O' piece in a small form of this piece
    possibleSmall = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    
    for p in possibleSmall:
        formToRemove+=1
        if (board[p[0]][p[1]] == oPiece and 
            board[p[0]+1][p[1]] == oPiece and 
            board[p[0]][p[1]+1] == oPiece and
            board[p[0]+1][p[1]+1] == oPiece):
            whichFormRemove = formToRemove
            break
    return whichFormRemove

def removeSmallCircle (board):
    """
    The function takes a board as input and removes a small circle shape from the
    board by replacing the corresponding positions with a blank spot.
    
    Arguments:
        board: an matrix 5x5
        
    Returns:
        boardWithoutSmallCircle: an matrix 5x5
    """
    # list with the positions on the board 
    # of the left top 'O' piece in a small form of this piece
    possibleSmall = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    # indicates what is the position 
    # of the left top 'O' piece in a small form of this piece
    p = possibleSmall[whichFormRemove-1]
    
    board[p[0]][p[1]] = blankSpot
    board[p[0]+1][p[1]] = blankSpot
    board[p[0]][p[1]+1] = blankSpot
    board[p[0]+1][p[1]+1] = blankSpot
    
    return board