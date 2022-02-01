#!/bin/bash

# install system dependencies
sudo apt install python-systemd python3-systemd libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libhdf5-dev

# install python dependencies
sudo pip3 install flask numpy opencv-contrib-python imutils opencv-python

# create folders and copy files
sudo mkdir /usr/local/lib/spy-robot-gopigo
sudo cp -r ./* /usr/local/lib/spy-robot-gopigo/
sudo cp ./spy-robot-gopigo.service /etc/systemd/system

# ownership and permissions
sudo chown root:root /usr/local/lib/spy-robot-gopigo/spy-robot-gopigo.py
sudo chmod 644 /usr/local/lib/spy-robot-gopigo/spy-robot-gopigo.py
sudo chown root:root /etc/systemd/system/spy-robot-gopigo.service
sudo chmod 644 /etc/systemd/system/spy-robot-gopigo.service

# systemd systemctl commands
sudo systemctl daemon-reload
sudo systemctl enable spy-robot-gopigo
sudo systemctl restart spy-robot-gopigo
sudo systemctl --property=MainPID show spy-robot-gopigo
