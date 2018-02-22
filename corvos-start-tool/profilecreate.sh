#!/bin/bash
# Script to create student user and prompt for password.
if [ $(id -u) -eq 0 ]; then
	read -s -p "PLEASE ENTER A PASSWORD FOR THE STUDENT ACCOUNT:" password
	pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
	useradd -m -p $pass student
	[ $? -eq 0 ] && echo "Student User Created!" || echo "Failed to add a user!"
	gpasswd -a student nopasswdlogin
else
	echo "An error has occured. Please run this script with root privileges."
	exit 2
fi
