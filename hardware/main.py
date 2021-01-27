import time , ds18x20 , onewire , ssd1306, gc
from machine import Pin, ADC

i2c = machine.I2C(scl = Pin(5), sda = Pin(4))
oled = ssd1306.SSD1306_I2C(128,64,i2c, 0x3c)
oled.fill(0)

adc = ADC(0)
dat = Pin(14)
ds = ds18x20.DS18X20(onewire.OneWire(dat))

led = Pin(2,Pin.OUT)
relay = Pin(16,Pin.OUT)

roms = ds.scan()
print('found devices: %s' %(roms[0]))

def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

while True:
    ds.convert_temp()
    analog_read = adc.read()
    output = valmap(analog_read, 0,1024,-25,60)
    time.sleep_ms(100)

    if output >= ds.read_temp(roms[0]):
        ds.convert_temp()
        analog_read = adc.read()
        oled.fill(0) 
        oled.text("Temperature",0,0)
        oled.text(str(ds.read_temp(roms[0])),0,10)
        oled.text("analog",0,20)
        oled.text(str(output),0,30)
        oled.text("Gas leak, stoping machine",0,40)
        oled.show()
        time.sleep_ms(100)
        oled.fill(0)
        led.off()
        relay.on()       
        gc.collect()

    else:
        oled.text("Temperature",0,0)
        oled.text(str(ds.read_temp(roms[0])),0,10)
        oled.text("analog",0,20)
        oled.text(str(output),0,30)
        oled.show()
        time.sleep_ms(100)
        oled.fill(0)
        led.on()
        relay.off()
        gc.collect()