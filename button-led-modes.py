from gpiozero import LED, Button
from signal import pause

led = LED(20)
button = Button(21, bounce_time=0.05)

mode_fns = [led.off, led.on, led.blink]
mode_names = ["off", "on", "blink"]

mode_index = 0

def change_mode():
    global mode_index

    mode_index = (mode_index + 1) % len(mode_fns)

    mode_fn = mode_fns[mode_index]
    mode_name = mode_names[mode_index]

    print(f"Mode: {mode_name}")
    mode_fn()

button.when_pressed = change_mode

pause()
