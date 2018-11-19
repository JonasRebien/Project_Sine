import sys
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

isPulseGoingUp = True


#Borrowed from lib
def colorWipe(strip, color, wait_ms=400):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

#Borrowed from lib
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

#Borrowed from lib
def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

#Our own code
def pulsating(strip, colorStrength, wait_ms=60):
    if colorStrength < 30:
        #print("Under: ", colorStrength)
        setIsPulseGoingUpTo(True)
    
    if colorStrength > 180:
        #print("Over: ", colorStrength)
        setIsPulseGoingUpTo(False)

    if isPulseGoingUp:
        colorStrength = (colorStrength + 2)
    else:
        colorStrength = (colorStrength - 2)

    for i in range(strip.numPixels()):
        strip.setPixelColor(i,Color(colorStrength,0,0))
        strip.show()

    time.sleep(wait_ms/1000.0)
    
    return colorStrength

#Our own code
def loadingCircle(strip, wait_ms=70):
    for i in range(strip.numPixels()):
        if i > 0:
            lastValue = (i - 1)
        else:
            lastValue = 11 

        if i < 11:
            nextValue = (i + 1)
        else:
            nextValue = 0
        #print(nextValue)

        strip.setPixelColor(lastValue, Color(50, 0, 0))
        strip.setPixelColor(i, Color(0, 0, 255))
        strip.show()
        time.sleep(wait_ms/1000.0)




#Our own code
#Kan laves smartere iforhold til... Im just lazy BUT FIIIIIIIIIIIX IT
def fadeFromGreenToRed(strip, wait_ms=2):
    greenColor = 140
    redColor = 0

    while greenColor >= 2:
        greenColor -= 2
        redColor += 2 
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(greenColor,redColor,0))
            strip.show()
        time.sleep(wait_ms/1000.0)

#Our own code
def fadeFromRedToGreen(strip, wait_ms=20):
    greenColor = 0
    redColor = 140

    while redColor >= 2:
        redColor -= 2
        greenColor += 2 
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(greenColor,redColor,0))
            strip.show()
        time.sleep(wait_ms/1000.0)

#Our own code
# Kan nok laves smartere i forbindelse med pulsating
def redFadeInAndOut(strip, wait_ms= 1):
    timesGoingUp = 3
    colorStrength = 140
    setIsPulseGoingUpTo(True)
    
    while timesGoingUp > 0:
        if colorStrength < 30:
            #print("Under: ", colorStrength)
            setIsPulseGoingUpTo(True)

        if colorStrength > 180:
            #print("Over: ", colorStrength)
            setIsPulseGoingUpTo(False)
            timesGoingUp -= 1
            print timesGoingUp

        if isPulseGoingUp:
            colorStrength = (colorStrength + 2)
        else:
            colorStrength = (colorStrength - 2)

        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,colorStrength,0))
            strip.show()

        time.sleep(wait_ms/1000.0)


# DUPLIKATION IN BLUE FIIIIIIIIIX IT AT SOME POINT IN LIFE!
#Our own code
def fadeFromGreenToBlue(strip, wait_ms=2):
    greenColor = 140
    blueColor = 0

    while greenColor >= 2:
        greenColor -= 2
        blueColor += 2 
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(greenColor,0,blueColor))
            strip.show()
        time.sleep(wait_ms/1000.0)

def fadeFromBlueToGreen(strip, wait_ms=20):
    greenColor = 0
    blueColor = 140

    while blueColor >= 2:
        blueColor -= 2
        greenColor += 2 
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(greenColor,0,blueColor))
            strip.show()
        time.sleep(wait_ms/1000.0)

#Our own code
# Kan nok laves smartere i forbindelse med pulsating
def blueFadeInAndOut(strip, wait_ms= 1):
    timesGoingUp = 3
    colorStrength = 140
    setIsPulseGoingUpTo(True)
    
    while timesGoingUp > 0:
        if colorStrength < 30:
            #print("Under: ", colorStrength)
            setIsPulseGoingUpTo(True)

        if colorStrength > 180:
            #print("Over: ", colorStrength)
            setIsPulseGoingUpTo(False)
            timesGoingUp -= 1
            print timesGoingUp

        if isPulseGoingUp:
            colorStrength = (colorStrength + 2)
        else:
            colorStrength = (colorStrength - 2)

        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,0,colorStrength))
            strip.show()

        time.sleep(wait_ms/1000.0)





def setIsPulseGoingUpTo(booleanValue):
    global isPulseGoingUp
    isPulseGoingUp = booleanValue

#Our own code
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # Starting colorstrength
    colorStrength = 140
    
    #Variables for the while loop
    isPulsating = False
    isSearching = False
    searchFailed = False
    searchSuccess = False
    ledsOff = False 

    #Commands[arg] given from nodejs 
    if(sys.argv[1] == 'pulsating'):
        isPulsating = True
    
    if(sys.argv[1] == 'searching'):
        isSearching = True
    
    if(sys.argv[1] == 'searchfailed'):
        searchFailed = True

    if(sys.argv[1] == 'searchsuccess'):
        searchSuccess = True
    
    if(sys.argv[1] == 'ledsoff'):
        ledsOff = True
    
    try:
        while True:
            # Methods to be run depending og commands
            if isPulsating:
                colorStrength = pulsating(strip, colorStrength)
            
            if isSearching:
                loadingCircle(strip)

            if searchFailed:
                fadeFromGreenToRed(strip)
                redFadeInAndOut(strip)
                fadeFromRedToGreen(strip)
                searchFailed = False
                isPulsating = True
            
            if searchSuccess:
                fadeFromGreenToBlue(strip)
                blueFadeInAndOut(strip)
                fadeFromBlueToGreen(strip)
                searchSuccess = False
                isPulsating = True

            if ledsOff:
                colorWipe(strip, Color(0,0,0), 10)
                ledsOff = False
                exit()

    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 10)
