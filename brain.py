from pybricks.parameters import Color, Button
from pybricks.tools import wait

# List that contains the color of the
# pieces outside of the board
listPiecesOutside = []
# List of color of the pieces allowed 
# for the game
listColorOfPieces = [Color.BLUE, Color.YELLOW, Color.RED, Color.GREEN]


# function to read one color with the color sensor 
# and displays it on the screen of the ev3. 
# Stores the color readed on a list
def readColorOfPiece(ev3, colorSensor):
    colorPiece = colorSensor.color() # stores the color readed by the robot in this instance
    ev3.screen.clear() 
    if colorPiece in listColorOfPieces:
        # informates that the color exist 
        # and it should be more pieces to get
        listPiecesOutside.insert(0, colorPiece)
        # displays the color that the robot read on the 
        # color sensor on the ev3. To make the user
        # know when the color is readed
        ev3.screen.draw_text(10, 20, "COLOR READED")
        ev3.screen.draw_text(ev3.screen.width/2, ev3.screen.height/2,str(len(listPiecesOutside)))
        

# function that read all the colors "allowed" that the user 
# gives till it presses the middle button of the robot 
def readAllColorOfPieces(ev3, colorSensor):
    while Button.CENTER not in ev3.buttons.pressed():
        readColorOfPiece(ev3, colorSensor)
        wait(1500)