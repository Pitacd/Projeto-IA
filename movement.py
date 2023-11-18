from pybricks.tools import wait
from brain import *
# Variable that defines the distance
# that the robot has to move to 
# identify the next piece of the game
distanceToNextColor = 50 # 5cm

# Function to identify all the pieces
# initially outside the board 
def movementToReadAllPieces(robot, colorSensor):
    stop = False
    while not stop:
        if readColorOfPiece(colorSensor):
            robot.straight(distanceToNextColor)
        else:
            stop = True

# Function to make the robot go to the corret position to 
# put the piece on the board depending on the line and column
# of the matrix
def goToPositionOnBoard(line, column, robot, colorSensor):
    # variable that stores the number of black lines 
    # that the robot has to pass to place the piece on the board
    numberOfBlackLinesToPutPiece = (line * 5) + (column + 1)
    # variable that sotres the number of black lines 
    # passed by the robot on board
    numberOfBlackLinesPassed = 0
    robot.drive(100, 0)
    
    while numberOfBlackLinesPassed < numberOfBlackLinesToPutPiece:
        wait(100)
        if colorSensor.color() == Color.BLACK:
            numberOfBlackLinesPassed += 1
            
    robot.stop()
    
# def putPieceOnTheBoard(robot):
    