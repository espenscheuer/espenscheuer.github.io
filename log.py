import time
import serial 
portName ='COM3'

ser = serial.Serial(portName, 9600)

while True: 
	print(ser.readline())
	time.sleep(.1)