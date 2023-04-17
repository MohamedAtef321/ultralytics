import spidev
import time

def spi_send(data):

    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.mode = 3
    spi.max_speed_hz = 2000000
    #spi.cshigh = False
    #spi.bits_per_word = 8

    try:
        while True: # endless loop, press Ctrl+C to exit
            spi.writebytes(data)
            time.sleep(2) # sleep for 2 seconds
    finally:
        spi.close()
