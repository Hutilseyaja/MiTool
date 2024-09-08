#!/usr/bin/python

c1="\033[1;32m"
c2="\033[0m"
_l =  c1 + "_"*56 + c2 + "\n"

print("\033[H\033[J")
print(f"""
{_l}
Lock Bootloader:

notice: Prior to initiating the process, ensure that the partitions is clean ( If you've previously rooted your device, flash the clean boot.img Or If any modifications have been made to any partition, flash the clean partition-name.img ) to prevent any potential issues in the future

Type: {c1}fastboot oem lock{c2}
{_l}
Flash Custom Recovery:

Type: {c1}fastboot flash recovery /path/name.img{c2}

Example:
fastboot flash recovery /sdcard/download/recovery.img
{_l}
Flash Root:
1. Download and install Magisk app
2. Open Magisk app, press Install in the Magisk card
3. Choose 'Select and Patch a File', select boot.img
   (Note: Choose boot.img for device you want to root)

Type: {c1}fastboot flash boot /path/name.img{c2}

Example: fastboot flash boot /sdcard/download/boot.img
{_l}
Flash Specific Partitions
('recovery', 'boot', 'vbmeta', 'vbmeta_system', 'metadata', 'dtbo', 'cust', 'super', 'userdata', ...):

Type:
{c1}fastboot flash PatitionName /path/FilePartitionName{c2}

Example:
fastboot flash super /sdcard/download/super.img
{_l}
For more fastboot and adb commands:

Type: {c1}fastboot help{c2} or {c1}adb help{c2}
{_l}
For updating MiTool:

Type: {c1}u{c2}
{_l}
To report issues or share feedback, visit:

- GitHub Issues: github.com/offici5l/MiTool/issues
- Telegram Group: t.me/Offici5l_Group
{_l}
""")