# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, time, gc, network
from machine import Pin
#uos.dupterm(None, 1) # disable REPL on UART(0)

led = Pin(2,Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected() == False:
    wlan.connect("<<ssid>>","<<pass>>")

else:
    for i in range(2):
        led.on()
        time.sleep_ms(300)
        led.off()
        time.sleep_ms(300)

#import webrepl
#webrepl.start()
gc.collect()