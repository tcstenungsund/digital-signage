from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options for removing automation messages from chrome 
chromeOptions = Options()
chromeOptions.add_experimental_option("useAutomationExtension", False)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
#fullscreen
chromeOptions.add_argument("--kiosk")

# Using Chrome to access web
# sudo apt-get install chromium-chromedriver
driver = webdriver.Chrome(chrome_options = chromeOptions)

# Open the website
driver.get('index.html')

###TODO###
#luanch python on startup
#https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/

#starting website on startup
"""
https://raspberrypi.stackexchange.com/questions/110975/simple-way-to-open-webbrowser-in-fullscreen-from-python-script

Create a service file:

sudo nano /etc/systemd/system/startupbrowser.service  
Put all lines below there:

[Unit]
Description=startupbrowser
After=graphical.target

[Service]
User=pi
WorkingDirectory=/home/pi
Environment=DISPLAY=:0
ExecStart=/usr/bin/chromium-browser --start-fullscreen www.google.de

[Install]
WantedBy=graphical.target
Enable the new service and reboot the raspberry pi:

sudo systemctl enable startupbrowser.service 
sudo systemctl reboot  

"""


#rebooting on schedule
#https://smarthomepursuits.com/how-to-reboot-raspberry-pi-on-a-schedule/