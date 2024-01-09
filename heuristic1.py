from removePiece import removeForms

# listPiecesOutside = ['-', '+', '+', '-', '+', 'X', '+', 'O', '+', '+', 'X', 'O', '+', 'X', 'O', 'O', '-', 'X', '+', 'X', 'O', 'O', '-', 'O', 'O', 'X', '-', '-', 'X', 'X', 'O', '+', 'O', 'X', '+', '-', 'O', '+', '-', 'X', '+', 'X', '+', '-', 'X', 'X', 'O', 'X', '+', 'O']

minusPiece = "-"
plusPiece = "+"
xPiece = "X"
oPiece = "O"
blankSpot = "_"

# board = [["_", "_", "_", "_", "_"],
#         ["_", "_", "_", "_", "_"],
#         ["_", "_", "_", "_", "_"],
#         ["_", "_", "_", "_", "_"],
#         ["_", "_", "_", "_", "_"]]

def heuristicStaticReservation (initialBoard, listPiecesOutside):
    
    board = initialBoard.copy()
    listPieces = listPiecesOutside.copy()
    sequence = []
    
    while listPieces != []:
        
        piece = listPieces.pop(0)
        
        if piece == oPiece:
            if board[1][0] == blankSpot:
                board[1][0] = piece
                sequence += [(1,0)]
            elif board[1][1] == blankSpot:
                board[1][1] = piece
                sequence += [(1,1)]
            elif board[2][0] == blankSpot:
                board[2][0] = piece
                sequence += [(2,0)]
            else:
                resultRemForm = removeForms(board, piece, 2, 1)
                board = resultRemForm[0]
                sequence += [(2,1)]
        elif(piece == plusPiece):
            if board[0][3] == blankSpot:
                board[0][3] = piece
                sequence += [(0,3)]
            elif board[1][2] == blankSpot:
                board[1][2] = piece
                sequence += [(1,2)]
            elif board[1][3] == blankSpot:
                board[1][3] = piece
                sequence += [(1,3)]
            elif board[1][4] == blankSpot:
                board[1][4] = piece
                sequence += [(1,4)]
            else:
                resultRemForm = removeForms (board,piece,2,3)
                board = resultRemForm[0]
                sequence += [(2,3)]
        elif(piece == xPiece):
            if board[2][2] == blankSpot:
                board[2][2] = piece
                sequence += [(2,2)]
            elif board[2][4] == blankSpot:
                board[2][4] = piece
                sequence += [(2,4)]
            elif board[3][3] == blankSpot:
                board[3][3] = piece
                sequence += [(3,3)]
            elif board[4][2] == blankSpot:
                board[4][2] = piece
                sequence += [(4,2)]
            else:
                resultRemForm = removeForms(board,piece,4,4)
                board = resultRemForm[0]
                sequence += [(4,4)]
        else:
            ExistsAnotherMinusList = False
            for form in listPieces:
                if form == minusPiece:
                    ExistsAnotherMinusList = True
                    break
            if board[0][0] == blankSpot:
                board[0][0] = piece
                sequence += [(0,0)]
            elif board[0][2] == minusPiece:
                resultRemForm = removeForms(board,piece,0,1)
                board = resultRemForm[0]
                sequence += [(0,1)]
            else:
                if ExistsAnotherMinusList:
                    board[0][2] = piece
                    sequence += [(0,2)]
                else:
                    resultRemForm = removeForms(board,piece,0,1)
                    board = resultRemForm[0]
                    sequence += [(0,1)]
    nPieceBoard = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '_':
                nPieceBoard += 1
    print('\n')
    print(sequence)
    print('\n')
    print(board)
    print('\n')

# print('Start')
# heuristicStaticReservation(board, listPiecesOutside)