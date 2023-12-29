class reservePositionsOnBoard:
    def __init__(self):
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
        # [down+, up, left, left+, down+, right, up+, center, down]
        self.listPossiblePlusReservationBigShape = [tuple(set([(2, j) for j in range(5)] + [(i, 2) for i in range(5)]))]
        
        self.listPossibleSetXReservationSmallShape = [((i-1,j-1),(i-1,j+1),(i, j),(i+1,j+1),(i+1,j-1)) for i in range(1, 4) for j in range(1, 4)]
    # def listSetPositionForForm(self, piece, typeForm):
    #     match piece:
    #         case "-":
                
    #         case "+":
                
    #         case "O":
                
    #         case "X":
    #TODO change the above functions to receive the position of the piece put on the board and give its possible reservations to make a shape
     
    def setPositionForMinusForm(self, numberOfPieces, board):
        listPossibleSetMinusReservation = []
        
        if numberOfPieces >= 2:
            # copy of the list that contains all the possible combinations
            # to form the shape of a small minus
            listPossibleSetMinusReservation += self.listPossibleSetMinusReservationSmallShape.copy()
            
            for possibleSetReservation in self.listPossibleSetMinusReservationSmallShape:
                for position in possibleSetReservation:
                    if not board[position[0]*5 + position[1]].positionIsEmpty():
                        listPossibleSetMinusReservation.remove(possibleSetReservation)
                        break
        if numberOfPieces >= 3:
            # copy of the list that contains all the possible combinations
            # to form the shape of a big minus
            listPossibleSetMinusReservation += self.listPossibleSetMinusReservationBigShape.copy()
            
            for possibleSetReservation in self.listPossibleSetMinusReservationBigShape:
                for position in possibleSetReservation:
                    if not board[position[0]*5 + position[1]].positionIsEmpty():
                        listPossibleSetMinusReservation.remove(possibleSetReservation)
                        break
                    
        return listPossibleSetMinusReservation
        
    def setPositionForPlusForm(self, numberOfPieces, board):
        listPossibleSetPlusReservation = []
        
        if numberOfPieces >= 5:
            # copy of list that contains all the possible combinations 
            # to form the shape of a small plus (left,up,center,right,down)
            listPossibleSetPlusReservation += self.listPossibleSetPlusReservationSmallShape.copy()
            
            for possibleSetReservation in self.listPossibleSetPlusReservationSmallShape:
                for position in possibleSetReservation:
                    if not  board[position[0]*5 + position[1]].positionIsEmpty():
                        listPossibleSetPlusReservation.remove(possibleSetReservation)
                        break
        if numberOfPieces >= 9:
            # list that contains all the possible combinations 
            # to form the shape of a big plus 
            # [down+, up, left, left+, down+, right, up+, center, down]
            listPossibleSetPlusReservation = self.listPossibleSetPlusReservationBigShape.copy()
            
            for possibleSetReservation in self.listPossibleSetPlusReservationBigShape:
                for position in possibleSetReservation:
                    if not  board[position[0]*5 + position[1]].positionIsEmpty():
                        listPossibleSetPlusReservation.remove(possibleSetReservation)
                        break
        
        return listPossibleSetPlusReservation
    
    # def setPositionForXForm(self,typeForm, board):
    #     listPossibleSetXReservation = []
        
    #     if typeForm == 0:
            