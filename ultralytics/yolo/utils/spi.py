#import spidev
import time

def spi_send(data, spi_mode, spi_speed, spi_sleep):

    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.mode = spi_mode
    spi.max_speed_hz = spi_speed
    #spi.cshigh = False
    #spi.bits_per_word = 8

    try:
        while True: # endless loop, press Ctrl+C to exit
            spi.writebytes(data)
            time.sleep(spi_sleep) # sleep for n seconds
    finally:
        spi.close()

def spi_remap(c):
    ################ Adel Requirements ##############
    if(c >= 9  and c <= 18):
        c = c + 128
    return c
    ################################################# 