#!/bin/bash

sudo cp /opt/corvos/scripts/brupdate.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable brupdate
