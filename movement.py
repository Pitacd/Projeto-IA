from pybricks.tools import wait
from brain import *

# Function to make the robot go to the corret position to 
# put the piece on the board depending on the line and column
# of the matrix
def goToPositionOnBoard(line, column, robot, colorSensor):
    # variable that stores the number of black lines 
    # that the robot has to pass to place the piece on the board
    numberOfBlackLinesToPutPiece = (line * 5) + (column + 1)
    # variable that indicates the number of black lines 
    # passed by the robot on board
    numberOfBlackLinesPassed = 0
    robot.drive(100, 0)
    
    while numberOfBlackLinesPassed < numberOfBlackLinesToPutPiece:
        wait(90)
        if colorSensor.color() == Color.BLACK:
            numberOfBlackLinesPassed += 1
            
    robot.stop()

# function of the movement of the robot right before 
# arrived on the position to put the piece on the board 
def putPieceOnTheBoard(distanceToComeBack, robot, rotationMotor):
    robot.straight(150)
    wait(200)
    robot.turn(-90)
    wait(100)
    robot.straight(400)
    rotationMotor.run_angle(100, 90)
    robot.straight(150)
    wait(200)
    robot.turn(-90)
    wait(100)
    robot.straight(distanceToComeBack) 