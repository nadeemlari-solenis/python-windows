import usb.core
import usb.util

for dev in usb.core.find(find_all=True):
    print(dev)