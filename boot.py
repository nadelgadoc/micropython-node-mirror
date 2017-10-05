# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import machine
import os
from network import WLAN
gc.collect()

wlan = WLAN(mode=WLAN.STA)

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    # configuration below MUST match your home router settings!!

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('genericSSID', auth=(WLAN.WPA2, 'password'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
