# raspberry-pi-presentation-master
Base/Master for presentation scripts for raspberry pi

## installation
### Step 1
Put git repo in Documents (or edit path in startupbrowser.service)

### Step 2
Move startupbrowser.service to "/etc/systemd/system/"

### Step 3
Enable service with:
sudo systemctl enable startupbrowser.service 

### Step 4
Reboot the Pi
sudo systemctl reboot  
