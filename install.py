import time
from sys import stdout
import os
import funciones as f

# Colores
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
 █████                     █████              ████  ████ 
░░███                     ░░███              ░░███ ░░███ 
 ░███  ████████    █████  ███████    ██████   ░███  ░███ 
 ░███ ░░███░░███  ███░░  ░░░███░    ░░░░░███  ░███  ░███ 
 ░███  ░███ ░███ ░░█████   ░███      ███████  ░███  ░███ 
 ░███  ░███ ░███  ░░░░███  ░███ ███ ███░░███  ░███  ░███ 
 █████ ████ █████ ██████   ░░█████ ░░████████ █████ █████
░░░░░ ░░░░ ░░░░░ ░░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░░░                                                          
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
    time.sleep(1)
    white()
    print("\n[01] Actualizar el sistema")
    time.sleep(0.15)
    print("\n[02] Instalación de herramientas")
    time.sleep(0.15)
    print("\n[03] All in one")
    time.sleep(0.15)
    print("\n[04] Salir")
    time.sleep(0.15)

menu()

blue()
option = int(input("\n---------->> "))
print('\n')
print(banner2)
yellow()
if option == 1:
    f.requerimentos()
elif option == 2:
    f.herramientas()
elif option == 3:
    f.requerimentos()
    f.herramientas()
elif option == 4:
    exit
else:
    exit()

