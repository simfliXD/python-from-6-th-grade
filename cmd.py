import os
import time

os.system('cmd /k "sfc /scannow"')
os.system('cmd /k "Driverquery"')

owerwrite_files = input("Do you want to actually encrypt all files on hard drive? \nThis will overwrite/encrypt all files making them harder to recover \n  (y/n)")

if owerwrite_files == "y":
          os.system('cmd /k "cipher"')
          
ip_commands = input("\n\nDo you want to look what your ip is or somthing with ip to do? \n \n"
                      "A) look if a speficic place receviec a pakage \n \n"
                      "B) you want to know what ur ip addres is \n \n"
                    "C) you want to change ip addres (changes you ip but you will may need to log in to aplications like steam again \n \n"
                    "D) renews your ip addres \n \n"
                    "E) lets you know the state of ports or related ip addreses \n \n"
                    "NO) this will skip this section if you dont want any of the options above \n \n")

if ip_commands == "a":
    os.system('cmd /k "ping"')
    
elif ip_commands == "b":
    os.system('cmd /k "ipconfig"')
    
elif ip_commands == "c":
    os.system('cmd /k "ipconfig /relese"')
    
elif ip_commands == "e":
    os.system('cmd /k "netstat -an"')


clean_disk = input ("\n\nDo you want to clean a disk to free up space \n"
                    "This will not delete any usefull files only crap \n \n"
                    "  (y/n)\n")
if clean_disk == "y":
    os.system('cmd /c "cleanmgr.exe"')

system_info = input("DO you want to check system info? \n"
                   "(y/n)\n")
if system_info == "y":
    os.system('cmd /k "systeminfo"')

check_disk = input("do you want to check the disk? \n"
                   "A) This will check for physical damage to the disk ( this will take a while ) \n \n"
                   "B) This will check for misspelled and corupt files and try to fix them ( this will take a while ) \n"
                   "NO) this will skip this section if you dont want any of the options above \n \n")

if check_disk == "a":
    os.system('cmd /k "chkdsk /r"')

elif check_disk == "b":
    os.system('cmd /k "chkdsk /f"')

msg = input("Do you want to send a massage to all the computers connected to your internet?\n"
       "Ofcorse you do! Entre (y/n) to proced the prosses.")

if msf == "y":
       os.system('cmd /k "msg * hello your computer has virus"')

