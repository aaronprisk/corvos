#!/bin/bash

sudo systemctl disable brupdate
sudo rm /etc/systemd/system/brupdate.service
sudo systemctl daemon-reload
