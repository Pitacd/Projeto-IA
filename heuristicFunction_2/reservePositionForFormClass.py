class reservePositionsOnBoard:
    def __init__(self):
        # dictionary that has an tuple with the number of pieces of 
        # each type of piece to form the shapes tinny, big, mega and ultra 
        # (in this sequence)
        self.numberPieceNeedToShape = {'-' : (2,3), '+' : (5,9), 'X' : (5,9), 'O' : (4,8,12,16)}
        # list that contains all the possible combinations
        # to form the shape of a small minus
        self.listPossibleSetMinusReservationSmallShape = [((line, column), (line, column + 1)) for line in range(5) for column in range(4)]
        # list that contains all the possible combinations
        # to form the shape of a big minus
        self.listPossibleSetMinusReservationBigShape = [((line,column),(line,column+1),(line,column+2)) for line in range(5) for column in range(3)]
        # list that contains all the possible combinations 
        # to form the shape of a small plus (left,up,center,right,down)
        self.listPossibleSetPlusReservationSmallShape = [((i,j-1),(i-1,j),(i, j),(i,j+1),(i+1,j)) for i in range(1, 4) for j in range(1, 4)]
        # list that contains all the possible combinations 
        # to form the shape of a big plus 
        # [( down+, up, left, left+, down+, right, up+, center, down)]
        self.listPossiblePlusReservationBigShape = [tuple(set([(2, j) for j in range(5)] + [(i, 2) for i in range(5)]))]
        # list that contains all the possible combinations 
        # to form the shape of a small X (left-up,right-up,center,right-down,left-down)
        self.listPossibleSetXReservationSmallShape = [((i-1,j-1),(i-1,j+1),(i, j),(i+1,j+1),(i+1,j-1)) for i in range(1, 4) for j in range(1, 4)]
        # list that contains all the possible combinations 
        # to form the shape of a big X 
        # [(right-down+, left-down+, right-up+, left-up+, left-down, left-up, right-down, center, right-up)]
        self.listPossibleSetXReservationBigShape = [tuple(set([(j, j) for j in range(5)] + [(i, 4-i) for i in range(5)]))]
        # list that contains all the possible combinations
        # to form the shape of a small circle
        self.listPossibleSetCircleReservationSmallShape = [((i,j),(i,j+1),(i+1,j),(i+1,j+1)) for i in range(4) for j in range(4)]
        # list that contains all the possible combinations
        # to form the shape of a middle circle
        self.listPossibleSetCircleReservationMidShape = [((i,j),(i,j+1),(i,j+2),(i+1,j),(i+1,j+2),(i+2,j),(i+2,j+1),(i+2,j+2)) for i in range(3) for j in range(3)]
        # list that contains all the possible combinations
        # to form the shape of a big circle
        self.listPossibleCircleReservationBigShape = [((i,j),(i,j+1),(i,j+2),(i,j+3),(i+1,j),(i+1,j+3),(i+2,j),(i+2,j+3),(i+3,j),(i+3,j+1),(i+3,j+2),(i+3,j+3)) for i in range(2) for j in range(2)]
        # list that contains all the possible combinations
        # to form the shape of a mega circle
        self.listPossibleCircleReservationMegaShape = [tuple(set([(i,j) for i in range(5) for j in (0,4)] + [(i,j) for i in (0,4) for j in range(5)]))]
    
    def listSmallShapeToUse(self, piece):
        """
        The function returns a list of possible small shapes to use based on the given piece.
        
        Arguments:
            piece : a char, one of the following values: '-', '+', 'X', or 'O'
            
        Returns:
            listOfPossibleSmallShapes: a list
        """
        match piece:
                case '-':
                    return self.listPossibleSetMinusReservationSmallShape
                case '+':
                    return self.listPossibleSetPlusReservationSmallShape
                case 'X':
                    return self.listPossibleSetXReservationSmallShape
                case 'O':
                    return self.listPossibleSetCircleReservationSmallShape
    
    def listBigShapeToUse(self,piece):
        """
        The function returns a list of possible big shapes to use based on the given piece.
        
        Arguments:
            piece : a char, one of the following values: '-', '+', 'X', or 'O'
            
        Returns:
            listOfPossibleBigShapes: a list
        """
        match piece:
            case '-':
                return self.listPossibleSetMinusReservationBigShape
            case '+':
                return self.listPossiblePlusReservationBigShape
            case 'X':
                return self.listPossibleSetXReservationBigShape
            case 'O':
                return self.listPossibleSetCircleReservationMidShape
    
    def possibleFormToDoInTheBoard(self, board, listPossibleFormToDo, listPossibleSetReservationShape):
        """
        The function checks if a list of possible reservations can be made on a board by removing any
        reservations that have occupied positions.
        
        Arguments:
            board: a matrix 5x5
            listPossibleFormToDo: a list 
            listPossibleSetReservationShape: a list
        """
        for possibleSetReservation in listPossibleSetReservationShape:
                for position in possibleSetReservation:
                    if not board[position[0]*5 + position[1]].positionIsEmpty():
                        listPossibleFormToDo.remove(possibleSetReservation)
                        break
    
    def listSetPositionForPieceForm(self, numberOfPieces, piece, board):
        """
        The function returns a list of possible set positions for a given
        piece on a board, based on the number of available pieces and the shape of the piece.
        
        Arguments:
            numberOfPieces: an integer
            piece: a char
            board: a matrix 5x5
        """
        listPossibleSetReservation = []
        numberPiecePerShape = self.numberPieceNeedToShape[piece]
        
        if numberOfPieces >= numberPiecePerShape[0]:
    
            listSmallShapeToUse = self.listSmallShapeToUse(piece)
            listPossibleSetReservation += listSmallShapeToUse.copy()
            
            self.possibleFormToDoInTheBoard(board, listPossibleSetReservation, listSmallShapeToUse)
                    
        if numberOfPieces >= numberPiecePerShape[1]:
            
            listBigShapeToUse = self.listBigShapeToUse(piece)
            listPossibleSetReservation += listBigShapeToUse.copy()
            
            self.possibleFormToDoInTheBoard(board, listPossibleSetReservation, listBigShapeToUse)
        
        if piece == 'O':
            if numberOfPieces >= numberPiecePerShape[2]:
                listPossibleSetReservation += self.listPossibleCircleReservationBigShape.copy()
                
                self.possibleFormToDoInTheBoard(board, listPossibleSetReservation, self.listPossibleCircleReservationBigShape)
            
            if numberOfPieces >= numberPiecePerShape[3]:
                listPossibleSetReservation += self.listPossibleCircleReservationMegaShape.copy()
                
                self.possibleFormToDoInTheBoard(board, listPossibleSetReservation, self.listPossibleCircleReservationMegaShape)
                        
        return listPossibleSetReservation