from pybricks.tools import wait
from pybricks.parameters import Color

# Function to make the robot go to the correct position to 
# put the piece on the board depending on the line and column
# of the matrix
def goToPositionOnBoard(line, column, robot, ev3, rotationMotor,colorSensor):
    """
    The function moves a robot to a specific position on a board by counting the
    number of black lines it passes given by knowing the line and column of the matrix
    he has to put the piece.
    
    Arguments:
        line: an integer
        column: an integer
        robot: an DriveBase 
        colorSensor: an ColorSensor
    """
    # variable that stores the number of black lines 
    # that the robot has to pass to place the piece on the board
    numberOfBlackLinesToPutPiece = (line * 5) + (column + 1)
    # variable that indicates the number of black lines 
    # passed by the robot on board
    numberOfBlackLinesPassed = 0
    rotationMotor.run(-100)
    robot.drive(100, 0)
    
    while numberOfBlackLinesPassed < numberOfBlackLinesToPutPiece:
        if colorSensor.color() == Color.BLACK:
            numberOfBlackLinesPassed += 1
            ev3.speaker.beep()
            wait(100)
            
    robot.stop()

# function of the movement of the robot right before 
# arrived on the position to put the piece on the board 
def putPieceOnTheBoard(robot, rotationMotor):
    """
    The function moves the robot forward, turns it to left, moves it forward again, rotates the grab
    motor and then moves the robot forward and turns it to left again.
    
    Arguments:
        robot: an DriveBase 
        rotationMotor: an Motor
    """
    robot.straight(150)
    wait(200)
    robot.turn(-90)
    wait(100)
    robot.straight(390)
    rotationMotor.stop()
    rotationMotor.run_until_stalled(100)
    robot.straight(200)
    wait(200)
    robot.turn(-90)
    
# function to make the robot come back right after it puts 
# the piece on the board. Note this needs a box in the 
# beginning to this works
def goBackToInitialPosition(distanceToComeBack, robot, ultrasonSensor):
    """
    The function moves the robot back to its initial position using
    distanceToComeBack, robot, and ultrasonSensor.
    
    Arguments:
        distanceToComeBack: an integer
        robot: an DriveBase 
        ultrasonSensor: an UltrasonicSensor
    """
    robot.straight(distanceToComeBack)
    wait(200)
    robot.turn(-90)
    wait(100)
    robot.straight(ultrasonSensor.distance() - 40) # change if box moved from the tests
    robot.turn(-90)