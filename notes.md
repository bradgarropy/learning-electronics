# SSH

```
ssh bradgarropy@raspberrypi.local
```

# Python

Run scripts on Raspberry Pi.  
`venv` is an isolated Python environment.  
`requirements.txt` is like a `package.json`.

```bash
python script.py
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

[circuit-canvas]: https://circuitcanvas.com
[multimeter]: https://www.youtube.com/watch?v=EvAq9zqRB5I
[pi-tutorial]: https://www.youtube.com/watch?v=tIEI3sv_gxM
