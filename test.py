#! /usr/bin/python3.3
import robot
import sys
import serial

port = "/dev/TTYUSB0"

r = None

try:
	r = robot.Robot(port)
except serial.SerialException:
	print("Could not connect to '" + port + "'.")
	sys.exit(1)
except ValueError:
	print("Something is wrong with provided baud rate")
	sys.exit(1)

r.send([128, 250, 140])
print(r.read(3))