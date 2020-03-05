import serial

ser = serial.Serial(9600)

def sendOverUART(data):
    ser = serial.Serial ("/dev/ttyAMA0")    #Open named port 
    ser.baudrate = 9600                     #Set baud rate to 9600                     
    ser.write(data)                         #Send back the received data
    ser.close()   

def saveData(gesch, winkel):
    data = [gesch, winkel]
    sendOverUART(data)
