import os
import socket 
import whois
import getpass
import psutil
import platform
from datetime import datetime

# format data output from whois lookup & geolocater if you add it

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    ('cls', 'clear')[os.name!='nt']

def get_host_name():
    clear()
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    username = getpass.getuser()
            
    print(f"Current user: {username} \nHost name: {host_name} \nLocal IP: {local_ip} \nInterface wlan0: ")

def whois_lookup():
    clear()
    whois_input = input("\nWhat website would you like to perform a whois lookup for?\n>> ")
    w = whois.whois(whois_input)
    clear()
    print(f'\n Here is the whois data for {whois_input}: \n\n >>{w}')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return (f"{bytes:.2f}{unit}{suffix}")
        bytes /= factor

clear()

art = '''    ____      ____      ______           __    __             
   /  _/___  / __/___  / ____/________ _/ /_  / /_  ___  _____
   / // __ \/ /_/ __ \/ / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 _/ // / / / __/ /_/ / /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
/___/_/ /_/_/  \____/\____/_/   \__,_/_.___/_.___/\___/_/     
                                                              

'''
print(f'{art}Version: 0.2 \n Written by Camroツ \n')

while True:
    usr_choice = input("\nSelect from the options below: \n 1> Local computer info\n 2> Whois lookup\n 3> IP Geolocater\n 4> Exit\n >> ")

    if usr_choice == "1":
        #System Info
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

        #Boot Time
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

        #Printing CPU information
        print("="*40, "CPU Info", "="*40)
        #Number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        #CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        #CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        #Printing memory usage
        print("="*40, "Memory Info", "="*40)
        #Get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {get_size(svmem.percent)}%")
        print("="*20, "SWAP","="*20)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"{get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

        # Disk Information
        print("="*40, "Disk Information", "="*40)
        print("Partitions and Usage:")
        #Get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint} ===")
            print(f"  File system type: {partition.fstype}")
        
        ##finish above tasks

    elif usr_choice == "2":
        whois_lookup()

    elif usr_choice == "3":
        print("Sorry, this feature isn't enabled yet:)")

    elif usr_choice == "4":
        break    
    else: 
        clear()
        print("Please choose a valid option.")
        
exit
