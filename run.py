import platform
import os
import requests

global arc

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def check_python_architecture():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING FILE TOOL ')
        import data.FILE32
        data.FILE32.main()
    elif architecture[0] == '64bit':
        arc = "64BIT"
        import data.FILE32
        data.FILE32.main()
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING FILE TOOL ')
    else:
        arc = "INVALID"


if __name__ == "__main__":
    check_python_architecture()
