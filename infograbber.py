import os
import socket 
import json
import whois
import requests
import getpass
import netifaces

# format data output from whois lookup & geolocater if you add it

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    return("  ")

clear()

art = '''    ____      ____      ______           __    __             
   /  _/___  / __/___  / ____/________ _/ /_  / /_  ___  _____
   / // __ \/ /_/ __ \/ / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 _/ // / / / __/ /_/ / /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
/___/_/ /_/_/  \____/\____/_/   \__,_/_.___/_.___/\___/_/     
                                                              

'''
print(f'{art}Version: 0.2 \n Written by Camroツ \n')

while True:
    usr_choice = input("Select from the options below: \n 1> Local computer info\n 2> Whois lookup\n 3> IP Geolocater\n 4> Exit\n >> ")

    if usr_choice == "1":
        
        def get_host_name():
            host_name = socket.gethostname()
            local_ip = socket.gethostbyname(host_name)
            username = getpass.getuser()
            
            print(f"Current user: {username} \nHost name: {host_name} \nLocal IP: {local_ip} \nInterface wlan0: ")

          # to do: add interface information
          # add other local information  

        get_host_name()

    elif usr_choice == "2":

        def whois_lookup():
            whois_input = input("\nWhat website would you like to perform a whois lookup for?\n>> ")
            w = whois.whois(whois_input)
            print(f'\n Here is the whois data for {whois_input}: \n\n >>{w}')
            
        whois_lookup()

    elif usr_choice == "3":
        print("Sorry, this feature isn't enabled yet:)")

    elif usr_choice == "4":
        break    
    else: 
        print("Please choose a valid option.")
        
exit