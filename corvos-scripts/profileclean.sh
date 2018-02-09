#!/bin/bash
# Student Profile cleaning script for CorvOS
# Purge files created in home directory
rm -r /home/student/*

# Reset Whisker Menu
rm /home/student/.config/xfce4/panel/whiskermenu-1.rc
cp /opt/corvos/whiskermenu-1.rc /home/student/.config/xfce4/panel/

# Reset Firefox
rm -r /home/student/.mozilla/extensions/*
rm -r /home/student/.mozilla/firefox/*

# Add any additional directories to be cleaned below
