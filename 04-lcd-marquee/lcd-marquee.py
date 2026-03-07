from RPLCD.i2c import CharLCD
import time

MESSAGES = [
    ("Hey y'all!", "From ATX"),
    ("Hello World!", "Raspberry Pi"),
    ("Learning", "Electronics"),
    ("LCD1602", "Display Demo"),
    ("Goodbye!", "See ya later"),
]

def show_messages(lcd):
    while True:
        for line1, line2 in MESSAGES:
            lcd.clear()
            lcd.write_string(line1)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(line2)
            time.sleep(5)

if __name__ == "__main__":
    lcd = None

    try:
        lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)
        show_messages(lcd)
    finally:
        if lcd:
            lcd.clear()
