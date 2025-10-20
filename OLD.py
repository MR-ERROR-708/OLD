import platform
import os
import socket
import subprocess
import time
arc = None
os.system('clear')
print(f' [</=/>] CHECKING FOR UPDATED')
os.system('git pull --qui_pet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f" [</=/>] 32BIT DETECTED")
        print(f" [</=/>] STARTING ERROR TOOL")
        time.sleep(5)
        os.system('chmod 777 OLD32;./OLD32')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f" [</=/>] 64BIT DETECTED")
        print(f" [</=/>] STARTING ERROR TOOL")
        time.sleep(5)
        os.system('chmod 777 OLD64;./OLD64')
    else:
        arc = "INVALID"
        print(f" [</!/>] UNKNOWN DEVICE TYPE")
        exit()

if __name__ == "__main__":
    main()
