#---------[FILE MAKER TOOL BY HARRY]---------#
#----->    SCRIPTED BY HARRY AKUMA
#----->    FROM NEPAL NEED STARS
#----->    LOTS OF LOVE <3


#-----> MODULES IMPORT

import platform
import os
import requests
import time

#-----> GLOBAL VALUES

global arc

#-----> CHECKING FOR UPDATES

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

#-----> MAIN DEF

def file_harry():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED');time.sleep(1)
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING FILE TOOL ');time.sleep(1)
        import data.FILE32
        data.FILE32.follow_harry()
        data.FILE32.login()
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED');time.sleep(1)
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING FILE TOOL ');time.sleep(1)
        import data.FILE64
        data.FILE64.follow_harry()
        data.FILE64.login()
    else:
        exit(f' •\x1b[38;5;196m ->\x1b[37m YOU CANT USE THIS TOOL ');time.sleep(1)

#-----> SYSTEM CONTROL

if __name__ == "__main__":
    check_python_architecture()
