#!/bin/bash
# Google Chrome Setup Tool
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo "       _                               "
echo "   ___| |__  _ __ ___  _ __ ___   ___  "
echo "  / __| '_ \| '__/ _ \| '_ ' _ \ / _ \ "
echo " | (__| | | | | | (_) | | | | | |  __/ "
echo "  \___|_| |_|_|  \___/|_| |_| |_|\___| "
echo "This handy tool will help you get Google Chrome set up."
read -s -n 1 -p "PRESS ANY KEY TO BEGIN"
echo ""
echo ""
while true; do
    read -p "Install the Google Chrome Web Browser? (y/n)" yn
    case $yn in
        [Yy]* ) wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ;
                echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null; sudo apt-get update > /dev/null; sudo apt-get install google-chrome-stable -y; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

while true; do
    read -p "Enable Google Chrome profile autoclean? (y/n)" yn
    case $yn in
        [Yy]* ) cp /opt/corvos/chrome/ephemeral.json /etc/opt/chrome/policies/managed/; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

while true; do
    read -p "Enable Flash Click to Play setting? (y/n)" yn
    case $yn in
        [Yy]* ) cp /opt/corvos/chrome/flash.json /etc/opt/chrome/policies/managed/; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo "============================================================"
echo "Google Chrome setup tool has completed!"
echo "Local Chrome policy configs can be found in /etc/opt/chrome/"
echo "------------------------------------------------------------"
echo "A full list of Chrome policies can be found at:"
echo "https://www.chromium.org/administrators/policy-list-3"
echo "------------------------------------------------------------"
echo -e "We hope you enjoy using \e[1;34mCorvOS\033[0m!"
echo -e "Check out \e[4mhttps://corvos.io\e[0m"
echo "============================================================"
read -s -n 1 -p "PRESS ANY KEY TO EXIT"

