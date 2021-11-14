import time
from sys import stdout
import os
import funciones as f

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
   █████████                                                   ████ 
  ███░░░░░███                                                 ░░███ 
 ░███    ░███  ████████   █████   ██████  ████████    ██████   ░███ 
 ░███████████ ░░███░░███ ███░░   ███░░███░░███░░███  ░░░░░███  ░███ 
 ░███░░░░░███  ░███ ░░░ ░░█████ ░███████  ░███ ░███   ███████  ░███ 
 ░███    ░███  ░███      ░░░░███░███░░░   ░███ ░███  ███░░███  ░███ 
 █████   █████ █████     ██████ ░░██████  ████ █████░░████████ █████
░░░░░   ░░░░░ ░░░░░     ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░                                                                                                                               
"""
banner2 = """ ██████████ ██████████ ██████████ ██████████ ██████████
░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ 
"""
os.system("clear")

def menu():
    yellow()
    print(banner)
    blue()
    print(banner2)
    white()
    time.sleep(1)
    print(" [01] Cupp")
    time.sleep(0.05)
    print(" [02] Seeker")
    time.sleep(0.05)
    print(" [03] Password-Generator")
    time.sleep(0.05)
    print(" [04] TBomb")
    time.sleep(0.05)
    print(" [05] Auto-Bspwm")
    time.sleep(0.05)
    print(" [06] blackeye-im")
    time.sleep(0.05)
    yellow()
    print(' [99] Salir')
    time.sleep(0.05)
    white()
menu()
blue()
option1 = int(input("\n---------->> "))
print('\n')
blue()
print(banner2)
yellow()
if option1 == 1:
    os.system('python3 /tools/cupp/cupp.py -i')
elif option1 == 2:
    os.system('python3 /tools/seeker/seeker.py')
elif option1 == 3:
    os.system('python3 /tools/Password-Generator/generador.py')
elif option1 == 4:
    os.system('bash /tools/TBomb/TBomb.sh')
elif option1 == 5:
    os.system('python3 /tools/autoBspwm/main.py')
elif option1 == 6:
    os.system('bash /tools/blackeye-im/blackeye.sh')
elif option1 == 99:
    exit()
else:
    exit()

