from RPLCD.i2c import CharLCD
import time

def setup():
    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                  cols=16, rows=2, backlight_enabled=True)

    lcd.write_string('Greetings!')
    lcd.cursor_pos = (1, 1)  # Row 1, Column 1
    lcd.write_string('From SunFounder')

    time.sleep(2)

    return lcd

def destroy(lcd):
    lcd.clear()

if __name__ == "__main__":
    lcd = None

    try:
        lcd = setup()
    except KeyboardInterrupt:
        if lcd:
            destroy(lcd)
