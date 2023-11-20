import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()

while True:
    mb_temperature = str(ser.readline())
    print(mb_temperature)