import machine
import utime
import dht
from machine import Pin, I2C
from time import sleep
from ADS1115 import *
from scd30 import SCD30


i2c = machine.I2C(1, sda=Pin(14), scl=Pin(15), freq=50000)

ADS1115_ADDRESS = 0x48
adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)
adc.setVoltageRange_mV(ADS1115_RANGE_2048)
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_SINGLE)

scd30 = SCD30(i2c, 0x61)

def readChannel(channel):
    adc.setCompareChannels(channel)
    adc.startSingleMeasurement()
    while adc.isBusy():
        pass
    voltage = adc.getResult_V()
    return voltage

MQ131_POWER = machine.Pin(13, machine.Pin.OUT)
MP503_POWER = machine.Pin(12, machine.Pin.OUT)
#DHT22 Pin 11
DHT22 = dht.DHT22(machine.Pin(10))


#Main

print("Powering MQ131")
MQ131_POWER.value(1)
MP503_POWER.value(1)



scd30.set_measurement_interval(10)
scd30.start_continous_measurement()

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        utime.sleep(0.5)
    print("CO2 PPM,    Temp,     Hum")
    print(scd30.read_measurement())
    print("---------------")
    DHT22.measure()
    temp = DHT22.temperature()
    hum = DHT22.humidity()
    print("Temp: {:<4.2f}".format(temp))
    print("Hum: {:<4.2f}".format(hum))
    print("---------------")
    voltage = readChannel(ADS1115_COMP_0_GND)
    print("MQ-131 (Ozone) Voltage: {:<4.2f}".format(voltage))
    #https://github.com/ostaquet/Arduino-MQ131-driver Used for converstion numbers
    O3Ratio = 0
    if (hum>75):
        O3Ratio = -0.0103 * temp + 1.1507
    elif (hum>50):
        O3Ratio = -0.0119 * temp + 1.3261
    else:
        O3Ratio = -0.0141 * temp + 1.5623
    #print(O3Ratio)
    rS = voltage*1000000/(3.3-voltage)
    #print(rS)
    Ratio = rS / 1000000 * O3Ratio
    #print(Ratio)
    O3PPB = 9.4783 * (Ratio**2.3348)
    print(O3PPB)
    voltage = readChannel(ADS1115_COMP_1_GND)
    print("MP503 (VOC) Voltage: {:<4.2f}".format(voltage))
    voltage = readChannel(ADS1115_COMP_2_GND)
    print("SCD30: {:<4.2f}".format(voltage))
    print("---------------")
