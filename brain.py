from pybricks.parameters import Color, Button
from pybricks.tools import wait

#from random import randint

# List that contains the color of the
# pieces outside of the board
listPiecesOutside = []

# Key-value pairs that map a color to
# a board symbol (for visibility purposes)
mapColorToSymbol = { Color.BLUE : "+", Color.YELLOW : "X", Color.RED : "O", Color.GREEN : "-"}

# List of color of the pieces allowed 
# for the game
listColorOfPieces = [color for color in mapColorToSymbol]

# 5x5 matrix that represents the board state
# 0 represents blank spaces with no pieces
board = [["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"]]

# function to read one color with the color sensor 
# and displays it on the screen of the ev3. 
# Stores the color read on a list
def readColorOfPiece(ev3, colorSensor):
    """
    The function reads the color of a piece using a color sensor and updates a list of colors read so 
    far.
    
    Arguments:
        ev3: an EV3brick
        colorSensor:  an ColorSensor
    """
    # stores the color read it by the robot in this instance
    colorPiece = colorSensor.color() 
    
    ev3.screen.clear() 
    if colorPiece in listColorOfPieces:
        # puts the read piece in the 
        # end of the listPiecesOutside
        listPiecesOutside.append(colorPiece)
        # displays that the color has been read on the 
        # color sensor on the ev3 and number of colors read it. 
        ev3.screen.draw_text(10, 20, "COLOR READ IT")
        ev3.screen.draw_text(ev3.screen.width/2, ev3.screen.height/2,str(len(listPiecesOutside)))
        ev3.speaker.beep()
        
# function that read all the colors "allowed" that the user 
# gives till it presses the middle button of the robot 
def readAllColorOfPieces(ev3, colorSensor):
    """
    The function continuously reads the color of a piece using a color sensor until the center button on
    the EV3 brick is pressed.
    
    Arguments:
        ev3: an EV3brick
        colorSensor: an ColorSensor
    """
    while Button.CENTER not in ev3.buttons.pressed():
        readColorOfPiece(ev3, colorSensor)
        wait(1500)

# function that waits till the user gives the robot the piece
# and when gives press the middle button to continue the program
def giveTheRobotThePiece(ev3, rotationMotor):
    """
    The function rotates the grab motor and displays the color of the needed
    piece on the EV3 screen, waiting till the user gives the robot the piece
    by pressing the middle button of the EV3 brick.
    
    Arguments:
        ev3: an EV3brick
        rotationMotor: an Motor
    """
    rotationMotor.run_until_stalled(-100)
    ev3.screen.clear() 
    # displays in the screen of the ev3 
    # the color of the piece to be given
    ev3.screen.draw_text(5, 20, "PIECE COLOR")
    ev3.screen.draw_text(10, ev3.screen.height/2, listPiecesOutside[0])
    while Button.CENTER not in ev3.buttons.pressed():
        wait(1000)
    ev3.screen.clear()

def showBoard():
    """
    The function prints the current state of the board in a formatted way.
    """
    for line in board: 
        strLine = ""
        for column in line:
            strLine += column + " | "
        print(strLine)
        
    print("----------------------")
    
def passColorToPieceInOutsidePieces():
    """
    The function takes a list of pieces outside and maps their colors to symbols, returning a list of
    symbols.
    
    Returns:
        listPiecesOutsideChr: a list of chr
    """
    listPiecesOutsideChr = []
    
    for piece in listPiecesOutside:
        listPiecesOutsideChr.append(mapColorToSymbol[piece])
    
    return listPiecesOutsideChr

def numberOfEmptyPositions():
    """
    The function counts the number of empty positions in a given board.
    
    Returns:
        numberOfEmptyPositions: an integer
    """
    nEmptyPositions = 0
    for line in board:
        nEmptyPositions += line.count('_')
    
    return nEmptyPositions