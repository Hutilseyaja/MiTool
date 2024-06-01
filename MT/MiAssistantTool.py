#!/usr/bin/python

import subprocess
import time
import sys

c1="\033[1;32m"
c2="\033[0m"

print("\033[H\033[J")

print(f"""

\n━ {c1}1{c2} Read-Info\n
\n━ {c1}2{c2} Check-ROM-Compatibility(With MD5)\n
\n━ {c1}3{c2} Flash-Official-Recovery-ROM\n

""")
    

choice = input(f'Enter your {c1}choice{c2}: ')
if choice == "1":
    choice_s = "info"
elif choice == "2":
    choice_s = "checkrom"
elif choice == "3":
    choice_s = "flash"
else:
   print("\nInvalid choice\n")
   exit()

print("\n\033[H\033[J\nPlease connect Xiaomi in Recovery mode > MI Assistant\n")

animation_chars = "📱 ⚡"
animation_index = 0

while True:
    try:
        usb_devices = subprocess.check_output(["termux-usb", "-l"]).decode("utf-8").strip().split("\n")
        if len(usb_devices) > 1: 
            device_path = usb_devices[1].strip().strip('"')
            result = subprocess.check_output(["termux-usb", "-r", device_path])
            if "Access granted" in result.decode("utf-8"):
                print("\nDevice connected!\n")
                break
        else:
            sys.stdout.write(f"\rNo USB device found {animation_chars[animation_index]}")
            sys.stdout.flush()
            animation_index = (animation_index + 1) % len(animation_chars)
        time.sleep(0.5)
    except subprocess.CalledProcessError as e:
        time.sleep(2)

if choice_s == "info":
    subprocess.run(["termux-usb", "-E", "-e", "miasst info", "-r", device_path])
elif choice_s == "checkrom":
    subprocess.run(["termux-usb", "-E", "-e", "miasst checkrom", "-r", device_path])
elif choice_s == "flash":
    subprocess.run(["termux-usb", "-E", "-e", "miasst", "-r", device_path])

