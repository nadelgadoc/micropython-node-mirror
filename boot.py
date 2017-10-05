# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
import machine
import sdcard
import os
from network import WLAN
#webrepl.start()
gc.collect()
sd = sdcard.SDCard(machine.SPI(1),machine.Pin(16))
os.mount(sd, '/sd2')

wlan = WLAN()

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('192.168.178.107', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('C3D-ING-2', auth=(WLAN.WPA2, 'c3dc3dc3ding'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
