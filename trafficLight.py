from gpiozero import LED, Button
from signal import pause
from time import sleep


    

button = Button(2)
#button.when_pressed=led.on
ledred = LED(18)
ledyellow = LED(23)
ledgreen = LED(24)

def trafficlight():
    
    ledgreen.off()
    
    ledred.on()
    sleep(5)
    ledred.off()
    
    ledyellow.on()
    sleep(5)
    ledyellow.off()
    
    ledgreen.on()
ledgreen.on
    
button.when_pressed = trafficlight



pause()
