#This is a check round for the IoT device in use, mostly to check connections

import machine, dht, ssd1306, time
from machine import I2C, Pin

#Traffic Light
green = Pin(12,Pin.OUT)                 #PIN 12
red = Pin(15,Pin.OUT)                   #PIN 15
yellow = Pin(13,Pin.OUT)                #PIN 13

#Display
i2c = I2C(‐1, Pin(5), Pin(4))           #PIN 4 & 5
i2c.scan()
display = ssd1306.SSD1306_I2C(64, 48, i2c)

#Light Sensor
light = machine.Pin(2,machine.Pin.IN)   #PIN 2

#Temperature Sensor
sensor = dht.DHT22(machine.Pin(16))     #PIN 16

#Tests
print ('test',30,'degree')
light.value()
sensor.humidity()
sensor.temperature()
display.fill(0)
display.text("T: "+str(sensor.temperature()), 0, 0)

if (light.value()==0):
	print("light on,",sensor.temperature(),'°C')
	display.text("T: "+str(sensor.temperature()), 0, 0
else:
	print("light off,",sensor.temperature(),'°C')
        display.text("T: "+str(sensor.temperature()), 0, 0



while True
        if (light.value()==0):
                green.on()
                print("Sunny,",sensor.temperature(),'°C')
                if (20 < sensor.temperature() < 25):
                        display.text("Sunny", 0, 0)
                        display.text("T: "+str(sensor.temperature()), 0, 0)
                        display.text("H: "+str(sensor.humidity()), 0, 8)
                else:
                        red.on()
                        print("Sunny,",sensor.temperature(),'°C')
                        print('Temperature issues, please FIX')
                        display.text("Sunny", 0, 0)
                        display.text("Temperature issues, please FIX", 0, 0)
                        display.text("T: "+str(sensor.temperature()), 0, 0)
time.sleep(10)


status = (light.value(),red.value())
if(status==(0,0)):
    print('soleggiato e luce spenta')
elif(status==(0,1)):
    print('soleggiato e luce accesa')
