The physical wiring of the project is discribed below

USB for 5V power

![image](https://user-images.githubusercontent.com/10062769/221706488-5e8f32f3-e09b-4a4a-a71e-bcd695ef7cf8.png)

PMS5003

![image](https://user-images.githubusercontent.com/10062769/221706288-a19117c9-2fbd-4e9e-a6d5-4cd5cff3bb84.png)

DHT22

![image](https://user-images.githubusercontent.com/10062769/221706159-139d3d75-ca8f-40d3-bfbd-dde017c47228.png)

SCD30 

![image](https://user-images.githubusercontent.com/10062769/221700527-9cdd1936-d9d3-493a-89b7-3b4ea8e3b7c6.png)

ADS1115 I choose an external ADC as the Pico has a poor ADC

![image](https://user-images.githubusercontent.com/10062769/221700287-cdae4323-8b6f-4942-a93a-5a9fe0a65848.png)

MQ-131 Wiring, POWER_MQ131 is connected to a output pin, AIN 0 is connected to the ADS1115

![image](https://user-images.githubusercontent.com/10062769/221700023-99742f07-1861-4bd2-b2eb-6ef3ce07330c.png)

MP503 DOES NOT CURRENTLY WORK

![image](https://user-images.githubusercontent.com/10062769/221706676-92e21db3-ac59-457a-8438-9bdf78068442.png)




Inspired by How To Mechatronics Air Quaility Monitor using the Arduino Pro Platform
https://howtomechatronics.com/projects/diy-air-quality-monitor-pm2-5-co2-voc-ozone-temp-hum-arduino-meter/

MicroPython packages used

https://github.com/agners/micropython-scd30

https://github.com/wollewald/ADS1115_mpy
