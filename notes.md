# SSH

```
ssh bradgarropy@raspberrypi.local
```

# Python

Run scripts on Raspberry Pi.

```bash
python script.py
```

`venv` is an isolated Python environment.

```bash
python3 -m venv .venv
```

Do not commit your `.venv` directory.

`requirements.txt` is like a `package.json`.

```bash
pip install -r requirements.txt
```

`lambda` functions are no argument function wrappers.

```python
lamba: led.blink(n=5)
```

Use `pause()` to suspend program.

```python
from signal import pause

pause()
```

# Circuits

[Circuit Canvas][circuit-canvas]

# LEDs

Long leg is positive  
Short leg is negative

Round side is positive  
Flat side is negative

# Buttons

Buttons require defining a `bounce_time` to avoid jitter.

# Videos

[How to use a Multimeter][multimeter]  
[Raspberry Pi 5 Tutorial][pi-tutorial]

# Projects

## LED Strip Integration

Confirm if LED strip can be connected to Pi.  
Investigate if LED strip can be controlled.  
Control with potentiometer or rotary encoder.

## User Controlled LED Strip

Web application where users control individual LEDs.

## Message Marquee

Web application where users can enter messages.  
Messages are displayed on the LCD screen.  
Messages scroll across the screen like a marquee.

[circuit-canvas]: https://circuitcanvas.com
[multimeter]: https://www.youtube.com/watch?v=EvAq9zqRB5I
[pi-tutorial]: https://www.youtube.com/watch?v=tIEI3sv_gxM
