from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

DATA_PIN = 24
SCK_PIN = 23


def main():
    with SHT1x(DATA_PIN, SCK_PIN, gpio_mode=GPIO.BCM) as sensor:
            temp = sensor.read_temperature()
            hum = sensor.read_humidity(temp)
            print(temp)
            print(hum)

if __name__ == "__main__":
    main()
