from pybricks.parameters import Color

# List that contains the color of the
# pieces outside of the board
listPiecesOutside = []
# List of color of the pieces allowed 
# for the game
listColorOfPieces = [Color.BLUE, Color.YELLOW, Color.RED, Color.GREEN]

def readColorOfPiece(colorSensor):
    if colorSensor.color() in listColorOfPieces:
            listPiecesOutside.insert(0, colorSensor.color())
            # informates that the color exist 
            # and it should be more pieces to get
            return 1
    else:  
        # there are no more pieces to get end 
        # of knowing pieces initially 
        return 0
    
