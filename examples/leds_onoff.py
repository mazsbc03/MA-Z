import mraa
import time

control = True

#Set GPIOS pins for testing
gpio_1 = mraa.Gpio(29)
gpio_2 = mraa.Gpio(15)
gpio_3 = mraa.Gpio(18)

#Set GPIOs as OUTs
gpio_1.dir(mraa.DIR_OUT)
gpio_2.dir(mraa.DIR_OUT)
gpio_3.dir(mraa.DIR_OUT)

while True:
    gpio_1.write(0)
    gpio_2.write(0)
    gpio_3.write(0)
    time.sleep(0.5)
    # Pause for half a second to switch the leds states.
    gpio_1.write(1)
    gpio_2.write(1)
    gpio_3.write(1)
    time.sleep(0.5)
