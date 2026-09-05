"""
modify the code to receive two inputs: 

(1) an integer N between 10 and 100 and 

(2) an IP address or a hostname. 

The user interface would also have an execute button. 
Once the button is pressed, 
    the hostname will be pinged for exactly N times.
"""
import tkinter as tk
from tkinter import Label, Entry, Button
# not allowed in python3
# from tkinter import *
import subprocess
validate_ip_script = "./validate_ip"
validate_hostname_script = "./validate_hostname"
send_pings_script = "./send_pings"

import os
for script in [validate_ip_script, validate_hostname_script, send_pings_script]:
    if os.path.exists(script):
        os.chmod(script, os.stat(script).st_mode | 0o111)




# These colors are set in several places, but this lets us change in only one.

mainbg = '#8888FF';

activebg = '#AAAAFF';

root = tk.Tk()

root.title('Temp Conversion')

# This grids the widget object where indicated, then returns it.

def mkgrid(r, c, w):
    w.grid(row=r, column=c, sticky='news')
    return w

def number(n):
    # an integer N between 10 and 100 
    num = 0
    try:
        if isinstance(n, str):
            num = int(n)
    except Exception as e:
        print(f"The thing broken: {e}")
    return num

def numberAction():
    userStr = fnum.get()
    userNum = 1
    userNum = number(userStr)

    if (userNum > 10 and userNum < 100):
        foutnum.configure(text=str(userNum))
    return userNum

def ipaddres(ip: str):
    # returns ip for a valid ip/hostname OR 0
    # an IP address or a hostname.
    # Check if ip address (firts four are type int) or host name (if type str)
    try:
        #first we assume ip str is 
        #1111.1111.1111.1111
        ipParts = ip.split(".")
        int(ipParts[0]) # this causes ValueError
        result = subprocess.run([validate_ip_script, ip], capture_output=True, text=True)
        if result.returncode == 1:
            return ip
        else:
            return 0
    
    except ValueError as v:
        # Check for host name like "localhost"
        
        # # Check with python
        # # Cannot start or end with a dot, 
        # ipParts = ip.split(".")
        # if ipParts[0] == '' or ipParts[-1] == '': 
        #     print("Cannot start or end with a dot")
        # # Cannot contain two consecutive dots
        # if ip.find(".."):
        #     print("Cannot contain two consecutive dots")

        # Check if the IP or hostname is valid with sh script
        # Execute the shell script
        result = subprocess.run([validate_hostname_script, ip], capture_output=True, text=True)
        if result.returncode == 1:
            return ip
        else:
            return 0
    except Exception as e:
        print(f"Error in ipaddres: {e}")
        return 0

def ipAddrAction():
    userStr = faddr.get()
    userAddr = ipaddres(userStr) # ip: str or 0
    if userAddr != "0":
        foutaddr.configure(text=str(userAddr))
    
    return userAddr

def execute_ping():
    try:
        ip = str(ipAddrAction()) # ip address/hostname str or 0
        userNum = str(numberAction()) # number or 0

        result = subprocess.run([send_pings_script, userNum, ip], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing ping: {e}")
    except Exception as e:
        print(f"Something crazy Unexpected broke: {e}")
    pass

# The rest hooks the Fahrenheut and Celsius Temperatures into
# the grid graphics manager widgets.

fnumlab = mkgrid(0, 0, Label(root, text="Number of Pings (N)", anchor='e', bg=mainbg))
fnum = mkgrid(0, 1, Entry(root, bg=mainbg))
foutnum = mkgrid(0, 2, Label(root, text="", relief='sunken', anchor='e', bg=mainbg))

faddrlab = mkgrid(1, 0, Label(root, text="IP Address (100.65.14.60)/ Hostname (localhost)", anchor='e', bg=mainbg))
faddr = mkgrid(1, 1, Entry(root, bg=mainbg))
foutaddr = mkgrid(1, 2, Label(root, text="", relief='sunken', anchor='e', bg=mainbg))


fbutton = mkgrid(0, 3, Button(root, text="execute entered Pings", bg=mainbg, activebackground=activebg,
    command=execute_ping))
# Starts the root main event loop

root.mainloop()
