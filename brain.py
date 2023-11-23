from pybricks.parameters import Color, Button
from pybricks.tools import wait

# List that contains the color of the
# pieces outside of the board
listPiecesOutside = []
# List of color of the pieces allowed 
# for the game
listColorOfPieces = [Color.BLUE, Color.YELLOW, Color.RED, Color.GREEN]
# Number of pieces put on the board
numberPiecesOnBoard = 0


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
    colorPiece = colorSensor.color() # stores the color read it by the robot in this instance
    ev3.screen.clear() 
    if colorPiece in listColorOfPieces:
        # informs that the color exist 
        # and it should be more pieces to get
        listPiecesOutside.insert(0, colorPiece)
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
    ev3.screen.clear() 
    ev3.screen.draw_text(5, 20, "PIECE COLOR")
    ev3.screen.draw_text(10, ev3.screen.height/2, listPiecesOutside[numberPiecesOnBoard])
    rotationMotor.run_angle(100, -90)
    while Button.CENTER not in ev3.buttons.pressed():
        wait(1000)
    ev3.screen.clear()