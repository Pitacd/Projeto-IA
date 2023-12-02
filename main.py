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

# Create your objects here.
ev3 = EV3Brick()

# Sounds for the robot

# Motors of the robot
rightMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rotationMotor = Motor(Port.B)

# Sensors of the robot
colorSensor = ColorSensor(Port.S1)
ultrasonSensor = UltrasonicSensor(Port.S2)

# Robot
robot = DriveBase(leftMotor, rightMotor, 56, 130) # initial wheelDiameter = 56 and axleTrack = 119
robot.settings(150, 250, 150, 200)

# Functions
brain.readAllColorOfPieces(ev3, colorSensor)
print(brain.listPiecesOutside) # testing to know that it is working

# make here a loop and it ends when there is 
# no pieces or space to put the pieces ont he board
while len(brain.listPiecesOutside) > 0:
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
    
    # update board state 
    # by adding to the board the first
    # piece from listPiecesOutside
    brain.board[line][column] = brain.listPiecesOutside[0]
    
    # update pieces outside
    # deleting the first piece from list
    # because it was moved to the board
    brain.listPiecesOutside.pop(0) 

    # print the board on the console
    print(brain.board[0])
    print(brain.board[1])
    print(brain.board[2])
    print(brain.board[3])
    print(brain.board[4])

    # put the piece on the board
    putPieceOnTheBoard(robot, rotationMotor)

    # return to the initial position
    goBackToInitialPosition(distanceToComeBack, robot, ultrasonSensor)

ev3.speaker.beep()