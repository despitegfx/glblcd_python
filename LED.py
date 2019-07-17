"""from gpiozero import LED
import time

led = LED(18)

led.on()
time.sleep(50)
led.off()"""


"""
from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)
    
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)
    
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)
    
    led.on()
    sleep(2)
    led.off()
    sleep(2)
    
  
 from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()"""



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
    
button.when_pressed = light



pause()
