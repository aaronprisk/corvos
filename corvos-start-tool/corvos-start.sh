#!/bin/bash
# CorvOS setup tool
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo "   ___ ___  _ ____   _____  ___  "
echo "  / __/ _ \| '__\ \ / / _ \/ __| "
echo " | (_| (_) | |   \ V / (_) \__ \ "
echo "  \___\___/|_|    \_/ \___/|___/ "
echo "================================="
echo -e "Welcome to \e[1;34mCorvOS\033[0m!"
echo "This handy tool will help you get everything set up."
read -s -n 1 -p "PRESS ANY KEY TO BEGIN"
echo ""
echo ""
echo -e "\033[1mSTEP 1 - CREATE STUDENT PROFILE\033[0m"
if [ $(id -u) -eq 0 ]; then
	read -s -p "Please enter a password for the Student Profile:" password
	pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
	useradd -m -p $pass student
	[ $? -eq 0 ] && echo "Student User Successfully Created!" || echo "Failed to add a user!"
	gpasswd -a student nopasswdlogin
else
	echo "An error has occured. Please run this script with root privileges."
	exit 2
fi
echo -e "\033[1mSTEP 2 - STUDENT PROFILE LOCKDOWN\033[0m"
while true; do
    read -p "Enable the Student Profile locks? (y/n)" yn
    case $yn in
        [Yy]* ) sudo sed -i "s/,student//g" /etc/xdg/xdg-xubuntu/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml;
                sudo sed -i "s/,student//g" /etc/xdg/xdg-xubuntu/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo -e "\033[1mSTEP 3 - STUDENT PROFILE CLEANER\033[0m"
while true; do
    read -p "Enable the Student Profile Cleaner? (y/n)" yn
    case $yn in
        [Yy]* ) sudo cp /opt/corvos/scripts/profileclean.sh /etc/xdg/autostart/; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo -e "\033[1mSTEP 4 - EXTRA SOFTWARE\033[0m"
while true; do
    read -p "Install Google Chrome Web Browser? (y/n)" yn
    case $yn in
        [Yy]* ) wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ;
                echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null; sudo apt-get update > /dev/null; sudo apt-get install google-chrome-stable -y; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo -e "\033[1mSTEP 5 - SCHOOL LINK\033[0m"
while true; do
    read -p "Create start menu link for school website? (y/n)" yn
    case $yn in
        [Yy]* ) echo "Please enter the URL of your school website(EX: www.corvos.edu):"; read link; sudo cp /opt/corvos/student-profile/school-home.desktop /usr/share/applications/; sudo sed -i "s/MYSCHOOL/$link/g" /usr/share/applications/school-home.desktop; break;;
        [Nn]* ) break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo "==============================================="
echo "Alright, looks like everything is ready to go!"
echo -e "We hope you enjoy using \e[1;34mCorvOS\033[0m!"
echo -e "Check out \e[4mhttps://corvos.io\e[0m"
echo "==============================================="
read -s -n 1 -p "PRESS ANY KEY TO EXIT"
