# motor-power-bootup
Fix spinning motors when TVM boots up. Wait 2 mins, then supply power to the motor PCB.

Install your python script into the home directory. One way to do this would be:
sudo nano /home/pi/motor_power_bootup.py

Then edit your crontab so that the Python script starts on boot:
sudo crontab -e

Then add a line at the bottom of the cron file:
@reboot python /home/pi/motor_power_bootup.py

Then close. And then restart:
sudo reboot

