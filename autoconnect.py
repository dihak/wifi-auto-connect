#!/usr/bin/python
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import sys
import time

if len(sys.argv) != 3:
    print("Usage: python3 autoconnect.py <ip_address> <essid>")
    sys.exit(1)

ip_address = str(sys.argv[1])
essid = str(sys.argv[2])

def ping(host):
    status,result = subprocess.getstatusoutput("ping -c1 -w2 " + host)
    ms = 0

    if status == 0:
        ms = result.split("time=")[1].split(" ")[0] # get the time in ms

    return [status == 0, ms]

def connectToWifi():
    """
    Connects to the wifi network with the given essid and password.
    Returns True if connection is successful, False otherwise.
    """

    command = ['nmcli', 'dev', 'wifi', 'connect', essid]

    return subprocess.call(command) == 0

while True:
    [connected, ms] = ping(ip_address)
    if connected:
        print("Connected to " + ip_address, ms + "ms")
    else:
        print("Could not connect to " + ip_address)
        print("Re-connect wifi to " + essid)
        if connectToWifi():
            print("Connected to " + essid)
    time.sleep(5)
