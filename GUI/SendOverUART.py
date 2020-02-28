import serial

ser = serial.Serial(9600)

#def sendOverUART(data):
    #ser.write(data)

def saveData(gesch, winkel):
    data = [gesch, winkel]
    print(data)
