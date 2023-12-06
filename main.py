#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Color, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Brain and Movement of the Robot for the Game
import brain
from movement import *
from removePiece import *

# Create your objects here.
ev3 = EV3Brick()

# Sounds for the robot

# Motors of the robot
rightMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rotationMotor = Motor(Port.B)

# Sensors of the robot
colorSensor = ColorSensor(Port.S1)
ultrasoundSensor = UltrasonicSensor(Port.S2)

# Robot
robot = DriveBase(leftMotor, rightMotor, 56, 133) 
robot.settings(150, 100, 150, 100)

# Points
points = 0

# Functions
brain.readAllColorOfPieces(ev3, colorSensor)
print(brain.listPiecesOutside) # testing to know that it is working

# The loop is checking if either pieces 
# to put on the board or the board is full
while len(brain.listPiecesOutside) > 0 and len(brain.listPossiblePositions) > 0:
    # obtain the piece
    brain.giveTheRobotThePiece(ev3, rotationMotor)
    
    # reset the distance traveled
    robot.reset() 

    # choose the next position 
    (line, column) = brain.choosePosition()
    print("The line is: " + str(line))
    print("The column is: " + str(column))
    
    # go to the next board position
    goToPositionOnBoard(line, column, robot, ev3, rotationMotor, colorSensor)
    
    # get the distance to come back
    distanceToComeBack = robot.distance() + 150    
    
    # update board state on the robot's brain
    # by adding to the board the first
    # piece from listPiecesOutside
    # removing it from there
    pieceColor = brain.listPiecesOutside.pop(0)
    pieceSymbol = brain.mapColorToSymbol.get(pieceColor)
    
    # check for full shapes in the board, remove them and get the acquired points 
    (board, pointsAcquired) = removeForms(brain.board, pieceSymbol, line, column)
    brain.board = board

    # if points were made, shapes were removed  
    # in that case, update the possible positions on the board
    if (pointsAcquired > 0):
        brain.updateListOfPossiblePositions()

    # update score 
    points += pointsAcquired

    # print the board on the console
    brain.showBoard()

    # put the piece on the board
    putPieceOnTheBoard(robot, rotationMotor)

    # return to the initial position
    goBackToInitialPosition(distanceToComeBack, robot, ultrasoundSensor)

print(points) 

ev3.speaker.beep()