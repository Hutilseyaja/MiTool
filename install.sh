#!/data/data/com.termux/files/usr/bin/bash

if ! command -v pv &>/dev/null; then
    echo "Installing pv..."
    yes | pkg install pv
fi

if ! command -v adb &>/dev/null || ! command -v fastboot &>/dev/null; then
    yes | apt update && yes | apt upgrade
    echo "Installing ADB and Fastboot..."
    yes | pkg uninstall termux-adb 2>/dev/null
    curl -s https://raw.githubusercontent.com/nohajc/termux-adb/master/install.sh | bash
    ln -s $PREFIX/bin/termux-fastboot $PREFIX/bin/fastboot
    ln -s $PREFIX/bin/termux-adb $PREFIX/bin/adb
fi

if ! command -v python3 &>/dev/null; then
    echo "Installing Python3..."
    yes | pkg install python3
fi

if ! python3 -c "import Cryptodome" &>/dev/null; then
    echo "Installing Cryptodome..."
    yes | pip install pycryptodomex --extra-index-url https://termux-user-repository.github.io/pypi/
fi

if ! python3 -c "import urllib3" &>/dev/null; then
    echo "Installing urllib3..."
    yes | pip install urllib3
fi

if ! python3 -c "import requests" &>/dev/null; then
    echo "Installing requests..."
    yes | pip install requests
fi

echo -e "\033[32mupdate mitool...\033[0m"
curl "https://raw.githubusercontent.com/offici5l/MiTool/master/MT/mitool.py" -o "$PREFIX/bin/mitool" && chmod +x "$PREFIX/bin/mitool"

echo -e "\033[32mupdate flashfastbootrom...\033[0m"
curl "https://raw.githubusercontent.com/offici5l/MiTool/master/MT/flashfastbootrom.py" -o "$PREFIX/bin/flashf" && chmod +x "$PREFIX/bin/flashf"

echo -e "\033[32mupdate flashwithsideloadmode...\033[0m"
curl "https://raw.githubusercontent.com/offici5l/MiTool/master/MT/flashwithsideloadmode.py" -o "$PREFIX/bin/flashz" && chmod +x "$PREFIX/bin/flashz"

echo -e "\033[32mupdate MiUnlockTool...\033[0m"
curl "https://raw.githubusercontent.com/offici5l/MiUnlockTool/master/MiUnlockTool.py" -o "$PREFIX/bin/miunlock" && chmod +x "$PREFIX/bin/miunlock"

echo -e "\033[32mupdate MiBypassTool...\033[0m"
curl "https://raw.githubusercontent.com/offici5l/MiBypassTool/master/MiBypassTool.py" -o "$PREFIX/bin/mibypass" && chmod +x "$PREFIX/bin/mibypass"

echo -e "\033[32mupdate MiAssistantTool...\033[0m"

curl "https://raw.githubusercontent.com/offici5l/MiTool/master/MT/miasst" -o "$PREFIX/bin/miasst" && chmod +x "$PREFIX/bin/miasst"

curl "https://raw.githubusercontent.com/offici5l/MiTool/master/MT/MiAssistantTool.py" -o "$PREFIX/bin/p_miasst" && chmod +x "$PREFIX/bin/p_miasst"

echo -e "\n\e[34mChangelog: https://github.com/offici5l/MiTool/blob/main/CHANGELOG.md\e[0m\n"
printf "use command: \e[1;32mmitool\e[0m\n"