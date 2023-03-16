hc05 connections
hc05 vcc to pin 2 of pi (5v)
hc05 gnd to pin 6 of pi
hc05 txd to pin 10 of pi (rxd)
hc05 rxd to pin 8 of pi (txd)

then optional
pip install pyserial

setup is

Steps to interface HC-05 Bluetooth module

Step-1: 
(i) Enter "sudo nano /boot/config.txt" at the terminal window and add "enable_uart-1" at the end of the file. 
(ii) Press (Ctrl+o) to save, followed by (Ctrl+x) to return to the terminal. (For nano editor) 
(iii) Enter "sudo reboot" in the terminal
Login to your Raspberry Pi board again

Step-2: 
(i) Enter "sudo systemctl stop serial-getty@ttyS0.service" in the terminal window 
(ii) Followed by "sudo systemctl disable serial-getty@tty50.service"
(iii) Then enter "sudo nano /boot/cmdline.txt" and remove console-serial0,115200 (or anything with console-...) 
(iv) Press (Ctrl+o) to save, followed by (Ctrl+x) to return to the terminal.
 (v) Enter "sudo reboot in the terminal
Login to your Raspberry Pi board once again.

Step-3: 
(i) Enter "sudo nano /boot/config.txt" in the terminal window and add "dtoverlay-p13-miniuart-bt" at the end of the file. 
(ii) Press (Ctrl-o) to save, followed by (Ctrl+x) to return to the terminal. 
(iii) Enter "sudo reboot" in the terminal

Now, login to your Raspberry Pi board, pair the device with your mobile and run the program (use "sudo infront of the run command if you are not a user in the dial-out

OPTIONAL: If you see your console login opening in the bluetooth terminal on your mobile, You can try these steps:

(1) Enter "sudo raspl-config", For Raspberry Pi 38 and above, choose Interfacing options-> Serial. For older versions, choose Advanced options-> 48.Serial

(11) For console login using serial port, select No and for interfacing serial hardware, select Yes. Then select OK and Finish.

If the issue still persists, enter "sudo systemctl stop serial-getty@ttyAMAD.service", and then run the program,

Note: If you sas garbage values at the terminal while printing, change the baud rate of the module. For information about the baud rate of the module, refer the datashe



