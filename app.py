import time

import psutil

import wmi

import logging

f = wmi.WMI()
logging.basicConfig(format='%(asctime)s %(message)s',datefmt="%d-%b-%y %H:%M:%S" , filename="system.log" )

while True :

    cpu=psutil.cpu_percent(interval=1)
    if(cpu>80):
        logging.warning("CPU Threshold exceeded!!! ")
    memory_usage=psutil.virtual_memory().percent
    if(memory_usage>80):
        logging.warning(f"Memory Limit Exceeding({memory_usage})%!!!")
    # print(psutil.virtual_memory().avail)
    disk_space=psutil.disk_usage("/").percent
    print(disk_space)
    if(disk_space>80):
        logging.warning("Running out of memory!!!!")
        print("pid   Process name")

    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        print(f"{process.ProcessId:<10} {process.Name}")



    time.sleep(1)





