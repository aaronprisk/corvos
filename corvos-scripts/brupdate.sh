#!/bin/bash
# brupdate runs by default every 30 minutes to ensure critical browser updates are always installed. This can be helpful in enviroments where devices are only in use for short bursts e.g., laptop carts
sudo apt update
sudo apt-get --only-upgrade install google-chrome-stable -y
sudo apt-get --only-upgrade install firefox -y
sudo apt-get --only-upgrade install adobe-flashplugin -y
# Add additional browser packages that need to be consistently updated below. After altering this file, be sure to run sudo systemctl reload-daemon
