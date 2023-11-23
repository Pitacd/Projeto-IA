#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Color, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Brain and Movement of the Robot for the Game
from brain import *
from movement import *

from random import randint

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
robot.settings(150, 100, 150, 100)

# Functions
readAllColorOfPieces(ev3, colorSensor)
print(listPiecesOutside) # testing to know that it is working
rotationMotor.run_angle(100, 90)
# make here a loop and it ends when there is 
# no pieces or space to put the pieces ont he board
while numberPiecesOnBoard < len(listPiecesOutside):
    giveTheRobotThePiece(ev3, rotationMotor)
    robot.reset() # need it to reset the distance traveled

    # choose position #
    positionChoosed = False
    while not positionChoosed:
        line = randint(0, 5)
        column = randint(0, 5)  
        if brain.board[column][line] == 0:
            positionChoosed = True
    # # # # # # # # # #

    goToPositionOnBoard(line, column, robot, colorSensor)
    distanceToComeBack = robot.distance() + 150 # plus the distance that he will make to straight right after
    
    # update board state # 
    brain.board[column][line] = brain.listPiecesOutside[brain.numberPiecesOnBoard]
    # # # # # # # # # # # 

    putPieceOnTheBoard(robot, rotationMotor)
    goBackToInitialPosition(distanceToComeBack, robot, ultrasonSensor)
