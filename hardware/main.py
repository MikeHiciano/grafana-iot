import time, ds18x20, onewire, ssd1306, dht, gc, ujson
from machine import Pin, ADC, I2C
from umqtt.simple import MQTTClient
import gc

server = b"test.mosquitto.org"
topic = b"sum_topic"

# I2C OLED DISPLAY
i2c = I2C(scl = Pin(5), sda = Pin(4))
oled = ssd1306.SSD1306_I2C(128,64,i2c, 0x3c)
oled.fill(0)
# ADC,DS18B20 AND DHT11 SENSOR CODE
adc = ADC(0)
dat = Pin(14)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
d = dht.DHT11(Pin(16))
led = Pin(2,Pin.OUT)
#SCANNING THE ADDRESS OF THE DS18B20 SENSOR
roms = ds.scan()

count = 0
mqtt_count = 0

def valmap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def blink():
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(500)

def send_requests(humidity,relative_temp,absolupt_temp):
    
    values = {"humidity":humidity,"relative_temp":relative_temp,"absolupt_temp":absolupt_temp}
    str_json = ujson.dumps(values)
    c = MQTTClient(b"someone", server)
    c.connect()
    c.publish(topic,str_json)
    c.disconnect()

def show_measures():
    
    global count
    global mqtt_count
    ds.convert_temp()
    analog_read = adc.read()
    output = valmap(analog_read, 0,1024,-25,60)  
    count = count + 1
    mqtt_count = mqtt_count + 1

    if True:
      oled.fill(0)
      oled.text("Temp:",0,0)
      oled.text(str(int(ds.read_temp(roms[0]))),40,0)
      oled.text("analog:",0,10)
      oled.text(str(int(output)),60,10)
      oled.text("temp:",0,20)
      oled.text(str(d.temperature()),40,20)
      oled.text("hum:",0,30)
      oled.text(str(d.humidity()),30,30)
      oled.show()
      time.sleep_ms(100)
      oled.fill(0)
      led.on()
      gc.collect()
    
    if count == 10:
      d.measure()
      count = 0

    if mqtt_count == 30:
      send_requests(d.humidity(),d.temperature(),int(ds.read_temp(roms[0])))
      mqtt_count = 0

while True:
  show_measures()

