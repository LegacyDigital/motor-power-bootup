# motor-power-bootup
This script will fix spinning motors when the TVM boots up. Specifically, we will connect a power relay to the Motor PCB that will turn on after 2 minutes. Follow instructions below.

Install your python script into the home directory. If we were starting from scratch, you could do this:
sudo nano /home/pi/motor-power-bootup/motor_power_bootup.py

But in our case, the Python file is already done. So just cd to /home/pi/ and then do this:
git clone https://github.com/mattbrown8454/motor-power-bootup

Then edit your crontab so that the Python script starts on boot:
sudo crontab -e

Then add a line at the bottom of the cron file:
@reboot python /home/pi/motor-power-bootup/motor_power_bootup.py

Then close. And then restart:
sudo reboot

