#IoT Light, temperature and humidity sensor for indoor plantation growth
import machine, dht, ssd1306
from time import time, sleep
from machine import I2C, Pin

green = Pin(12,Pin.OUT)                 #PIN 12
red = Pin(15,Pin.OUT)                   #PIN 15
yellow = Pin(13,Pin.OUT)                #PIN 13

i2c = I2C(‐1, Pin(5), Pin(4))           #PIN 5 & 4
i2c.scan()
display = ssd1306.SSD1306_I2C(64, 48, i2c)

def plantemp(mint,maxt,minh,maxh): 
light = machine.Pin(2,machine.Pin.IN)   #PIN 2
sensor = dht.DHT22(machine.Pin(16))     #PIN 16
if (light.value()==0):
        green.off()
        yellow.off()
        red.off()
        if (mint<=sensor.temperature()<=maxt and minh<=sensor.humidity()<=maxh):
                green.on()
                print('Everything Perfect')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny, Everything Perfect", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<mint and minh<=sensor.humidity()<=maxh):
                red.on()
                print('Low Temperature, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("Temperature issue, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
        elif (sensor.temperature()>maxt and minh<=sensor.humidity()<=maxh):
                red.on()
                print('High Temperature, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("Temperature issue, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
        elif (mint<=sensor.temperature()<=maxt and sensor.humidity()<minh):
                yellow.on()
                print('Low Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("Humidity issue, please FIX", 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (mint<=sensor.temperature()<=maxt and sensor.humidity()>maxh):
                yellow.on()
                print('High Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("Humidity issue, please FIX", 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()>maxt and sensor.humidity()<minh):
                red.on()
                yellow.on()
                print('High Temperature & Low Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<mint and sensor.humidity()>maxh):
                red.on()
                yellow.on()
                print('Low Temperature & High Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<mint and sensor.humidity()<minh):
                red.on()
                yellow.on()
                print('Low Temperature & Low Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()>maxt and sensor.humidity()>maxh):
                red.on()
                yellow.on()
                print('High Temperature & High Humidity, please FIX')
                print("Sunny,",sensor.temperature(),'°C')
                display.text("Sunny", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
else:
        if ((mint-5)<=sensor.temperature()<=(maxt-5) and (minh-10)<=sensor.humidity()<=(maxh-10)):
                green.on()
                display.text("Bed Time, Nice!", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<(mint-5) and (minh-10)<=sensor.humidity()<=(maxh-10)):
                red.on()
                print('Low Temperature, please FIX')
                print("Bed Time, Nice!,",sensor.temperature(),'°C')
                display.text("Bed Time", 0, 0)
                display.text("Temperature issue, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
        elif (sensor.temperature()>(maxt-5) and (minh-10)<=sensor.humidity()<=(maxh-10)):
                red.on()
                print('High Temperature, please FIX')
                print("Bed Time,",sensor.temperature(),'°C')
                display.text("Bed Time", 0, 0)
                display.text("Temperature issue, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
        elif ((mint-5)<=sensor.temperature()<=(maxt-5) and sensor.humidity()<(minh-10)):
                yellow.on()
                print('Low Humidity, please FIX')
                print("Bed Time,",sensor.temperature(),'°C')
                display.text("Bed Time", 0, 0)
                display.text("Humidity issue, please FIX", 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif ((mint-5)<=sensor.temperature()<=(maxt-5) and sensor.humidity()>(maxh-10)):
                yellow.on()
                print('High Humidity, please FIX')
                print("Bed Time,",sensor.temperature(),'°C')
                display.text("Bed Time", 0, 0)
                display.text("Humidity issue, please FIX", 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()>(maxt-5) and sensor.humidity()<(minh-10)):
                red.on()
                yellow.on()
                print('High Temperature & Low Humidity, please FIX')
                print("BAD Time,",sensor.temperature(),'°C')
                display.text("BAD Time", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<(mint-5) and sensor.humidity()>(maxh-10)):
                red.on()
                yellow.on()
                print('Low Temperature & High Humidity, please FIX')
                print("BAD Time,",sensor.temperature(),'°C')
                display.text("BAD Time", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()<(mint-5) and sensor.humidity()<(minh-10)):
                red.on()
                yellow.on()
                print('Low Temperature & Low Humidity, please FIX')
                print("BAD Time,",sensor.temperature(),'°C')
                display.text("BAD Time", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)
        elif (sensor.temperature()>(maxt-5) and sensor.humidity()>(maxh-10)):
                red.on()
                yellow.on()
                print('High Temperature & High Humidity, please FIX')
                print("BAD Time,",sensor.temperature(),'°C')
                display.text("BAD Time", 0, 0)
                display.text("T & H issues, please FIX", 0, 0)
                display.text("T: "+str(sensor.temperature()), 0, 0)
                display.text("H: "+str(sensor.humidity()), 0, 0)


while True:     #setting temperature humidity limits and refresh rate
        a = 20
        b = 25
        c = 60
        d = 80
        plantemp(a,b,c,d)
time.sleep(300)
