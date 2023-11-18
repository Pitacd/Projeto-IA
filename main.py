#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Brain and Movement of the Robot for the Game
from brain import *
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
robot.settings(150, 130, 150, 200)

# Functions
movementToReadAllPieces(robot, colorSensor)
goToPositionOnBoard(0, 0, robot, colorSensor)
putPieceOnTheBoard(robot, rotationMotor)
print(listPiecesOutside)
# reverseDistanceToPiece = 100

# rotationMotor.run_angle(100, 90)
# movementToReadAllPieces(robot, colorSensor)
# print(listPiecesOutside)
# robot.straight(200)
# robot.turn(90)
# robot.straight(-reverseDistanceToPiece)
# rotationMotor.run_angle(100, -90)
# robot.straight(reverseDistanceToPiece)
# robot.turn(-90)
# robot.straight(300)
# print(ultrasonSensor.distance())
# robot.straight(ultrasonSensor.distance() - 10)
# robot.turn(convertionRate(-90))
# distanceToPiece = ultrasonSensor.distance() 
# print(distanceToPiece)
# robot.turn(convertionRate(-180))
# if distanceToPiece - 20 > 0:
#     robot.stop()
#     robot.straight(-(distanceToPiece + 60))
# rotationMotor.run_angle(100, -90)
# robot.straight(600)

