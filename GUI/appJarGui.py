# import the library
from appJar import gui
import SendOverUART
# create a GUI variable called app
app = gui("Simulator Window", "500x300")
app.setBg("white")
app.addLabel("title", "UART Simulator")
app.setLabelBg("title", "yellow")

#GUI Design
#app.addLabel("gesch_details1", "Die Geschwindigkeit muss zwischen")
#app.addLabel("gesch_details2", "0 bis 21 sein. 21 heisst Rückwärts")
app.addLabelEntry("Geschwindigkeit")
#app.addLabel("winkel_details1", "Winkel muss zwischen")
#app.addLabel("winkel_details2", "0 bis 181 sein. 181 heisst eine Drehung")
app.addLabelEntry("Winkel")

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        gesch1 = app.getEntry("Geschwindigkeit")
        gesch2 = app.getEntry("Winkel")
        SendOverUART.SendOverUART(gesch1, gesch2)
        #print("Geschwindigkeit:", gesch, " Winkel:", wink)

#Buttons
app.addButtons(["Submit", "Cancel"], press)
app.setFocus("Geschwindigkeit")

#Starts the app, dont put any code after this
app.go()