import spidev
import time


spi = spidev.SpiDev()

def spiRead(channel):
    spi.open(0,channel)
    spiValue = spi.xfer2([0])
    time.sleep(0.5)
    spi.close()
    return spiValue

while True:
    resp = spiRead(1)
    resp = spiRead(0)
    print("Input Response = {}".format(resp))
    time.sleep(1)