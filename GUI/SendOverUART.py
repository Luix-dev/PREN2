import serial

def sendOverUART(gesch1, gesch2):
    ser = serial.Serial ("/dev/ttyAMA0", 57600)    #Open named port     
    ser.write(gesch1.encode())
    ser.write(gesch2.encode())                        #Send back the received data
    ser.close()