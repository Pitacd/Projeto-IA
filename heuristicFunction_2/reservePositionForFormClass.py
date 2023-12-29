class reservePositionsOnBoard:
    # def listSetPositionForForm(self, piece, typeForm):
    #     match piece:
    #         case "-":
                
    #         case "+":
                
    #         case "O":
                
    #         case "X":
    
    def setPositionForMinusForm(typeForm, board):
        listPossibleSetMinusReservation = []
        
        if typeForm == 0:
            for line in range(5):
                for column in range(4):
                    listPossibleSetMinusReservation.append(((line, column),(line, column+1)))
            
            for possibleSetReservation in listPossibleSetMinusReservation.copy():
                if board[possibleSetReservation[0][0]*5 + possibleSetReservation[0][1]].positionIsEmpty():
                    if not board[possibleSetReservation[1][0]*5 + possibleSetReservation[1][1]].positionIsEmpty():
                        listPossibleSetMinusReservation.remove(possibleSetReservation)
                else:
                    listPossibleSetMinusReservation.remove(possibleSetReservation)
        else:
            for line in range(5):
                for column in range(3):
                    listPossibleSetMinusReservation(((line,column),(line,column+1),(line,column+2)))
            
            for possibleSetReservation in listPossibleSetMinusReservation.copy():
                if board[possibleSetReservation[0][0]*5 + possibleSetReservation[0][1]].positionIsEmpty():
                    if board[possibleSetReservation[1][0]*5 + possibleSetReservation[1][1]].positionIsEmpty():
                        if not board[possibleSetReservation[1][0]*5 + possibleSetReservation[1][1]].positionIsEmpty():
                            listPossibleSetMinusReservation.remove(possibleSetReservation)
                    else:
                        listPossibleSetMinusReservation.remove(possibleSetReservation)
                else:
                    listPossibleSetMinusReservation.remove(possibleSetReservation)
                    
        return listPossibleSetMinusReservation
            