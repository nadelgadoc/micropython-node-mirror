# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import machine
import os
import sys
import multiWifiConnect

gc.collect()
led = machine.Pin('G13', machine.Pin.OUT)
led.value(1)

multiWifiConnect.connectAttempt()

led.value(0)

