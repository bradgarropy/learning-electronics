from gpiozero import LED, Button
from signal import pause

led = LED(20)
button = Button(21, bounce_time=0.05)

button.when_pressed = led.toggle

pause()
