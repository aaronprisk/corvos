#!/bin/bash
# Epoptes Setup

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi
echo " ___  __   __   __  ___  ___  __  "
echo "|__  |__) /  \ |__)  |  |__  /__' "
echo "|___ |    \__/ |     |  |___ .__/ "                                  
echo "=================================="
echo "This tool will help you set up the Epoptes classroom management tool"
read -s -n 1 -p "PRESS ANY KEY TO BEGIN"
echo ""
echo ""
echo -e "\033[1mWHAT TYPE OF DEVICE IS THIS?\033[0m"
while true; do
    read -p "Teacher server or Student client? (T/S)" ts
    case $ts in
        [Tt]* ) echo ""; echo "Setting up device as Teacher server"; 
                echo "PLEASE NOTE: It is highly recommended this device has a static IP address set."
                read -s -n 1 -p "PRESS ANY KEY TO CONTINUE WITH SETUP"
                sudo apt-get install epoptes -y > /dev/null/
                gpasswd -a $SUDO_USER epoptes > /dev/null/

                break;;
        [Ss]* ) echo ""; echo "Setting up device as Student client"; 
                echo "Please enter the IP Address of the Teacher Server:"; read servip;
                echo "* Updating host file"
                echo "$servip	server" >> /etc/hosts
                echo "* Connecting epoptes client to server"
                sudo epoptes-client -c

                break;;
        * ) echo "Please answer T or S.";;
    esac
done

echo "==============================================="
echo "Please reboot this device to complete setup."
echo -e "We hope you enjoy using \e[1;34mCorvOS\033[0m!"
echo -e "Check out \e[4mhttps://corvos.io\e[0m"
echo "==============================================="
read -s -n 1 -p "PRESS ANY KEY TO EXIT"
