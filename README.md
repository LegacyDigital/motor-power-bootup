# motor-power-bootup
This script will fix spinning motors when the TVM boots up. Specifically, we will connect a power relay to the Motor PCB that will turn on after 2 minutes. Follow instructions below.

Install your python script into the home directory. One way to do this would be:
sudo nano /home/pi/motor_power_bootup.py

Then edit your crontab so that the Python script starts on boot:
sudo crontab -e

Then add a line at the bottom of the cron file:
@reboot python /home/pi/motor_power_bootup.py

Then close. And then restart:
sudo reboot

