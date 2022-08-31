import serial
from itom import *
import time

#step_size = float(input('Please input the step size in mm: ')) 
#step_number = int(input('Please input the number of steps: ') )
win = ui("motor.ui", ui.TYPEWINDOW, childOfMainWindow=True)
ser= serial.Serial('COM6', 115200)



def ManualMoveXF():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    distance =float(stepsize)*float(stepnumber)
    gcode = "G21G91X"+str(stepsize)+"F25 \r\n"
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in x by",distance,"mm")

def ManualMoveXB():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    gcode = "G21G91X"+str(stepsize)+"F25 \r\n"
    distance =float(stepsize)*float(stepnumber)
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in x by",distance,"mm")


def ManualMoveYF():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    gcode = "G21G91Y"+str(stepsize)+"F25 \r\n"
    distance =float(stepsize)*float(stepnumber)
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in y by",distance,"mm")

def ManualMoveYB():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    gcode = "G21G91Y"+str(stepsize)+"F25 \r\n"
    distance =float(stepsize)*float(stepnumber)
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in y by",distance,"mm")


def ManualMoveZF():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    gcode = "G21G91Z"+str(stepsize)+"F25 \r\n"
    distance =float(stepsize)*float(stepnumber)
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in z by",distance,"mm")
 

def ManualMoveZB():
    stepsize =win.stepsizelineEdit["text"]
    stepnumber =win.stepnumberlineEdit["text"]
    distance =float(stepsize)*float(stepnumber)
    gcode = "G21G91Z-"+str(stepsize)+"F25 \r\n"
    for i in range(int(stepnumber)):
        ser.write(str.encode(gcode))
        time.sleep(0.01)
    print("Moved in z by",distance,"mm")
win.XFButton.connect("clicked()", ManualMoveXF)
win.XBButton.connect("clicked()", ManualMoveXB)
win.YFButton.connect("clicked()", ManualMoveYF)
win.YBButton.connect("clicked()", ManualMoveYB)
win.ZFButton.connect("clicked()", ManualMoveZF)
win.ZBButton.connect("clicked()", ManualMoveZB)

win.show(0)
