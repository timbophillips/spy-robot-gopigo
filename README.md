# spy-robot-gopigo
Web driven GoPiGo controls with live pi camera video feed
Python Flask backend and JS frontend

### Installation (on a raspberry pi running raspbian)
```
git clone https://github.com/timbophillips/spy-robot-gopigo.git
cd spy-robot-gopigo
sudo bash install.sh
```

By default the server is installed as a service to automatically start at boot

To stop the service
```
sudo systemctl stop spy-robot-gopigo
```
To disable the service
```
sudo systemctl disable spy-robot-gopigo
```
To start the service (if not already running)
```
sudo systemctl start spy-robot-gopigo
```
to re-enable the service if you disabled it
```
sudo systemctl enable spy-robot-gopigo
```
