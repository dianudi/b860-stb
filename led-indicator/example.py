from led import Led
from time import sleep

# Instance Led object
red = Led(474)
green = Led(476)
lan1 = Led(415)
lan2 = Led(416)

# Blink all led

if __name__ == '__main__':
    while True:
        sleep(1)
        red.on()
        green.on()
        lan1.on()
        lan2.on()
        sleep(1)
        red.off()
        green.off()
        lan1.off()
        lan2.off()
