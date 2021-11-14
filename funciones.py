import time
from sys import stdout
import os

# Colores:
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




# Opciones
def requerimentos():
    white()
    print('[+] Instalando requerimientos...\n')

    time.sleep(2)
    print('[+] Actualizando sistema')
    os.system("sudo apt-get update -y\n")

    time.sleep(2)
    os.system("apt upgrade -y")
    
    time.sleep(2)
    os.system("apt install php -y")
    os.system("apt install curl -y")

    time.sleep(2)
    white()
    print('[+] Requerimientos instalados correctamente\n\n')
    time.sleep(1)


def herramientas():
    white()
    print('[+] Instalando herramientas')
    green()
    os.system("mkdir tools")
    os.system("cd /tools")
    os.system("git clone https://github.com/Mebus/cupp.git")
    os.system("cd ..")
    os.system("git clone https://github.com/thelinuxchoice/instainsane")
    os.system("cd ..")
    os.system("git clone https://github.com/Tuch0/Password-Generator.git")
    os.system("cd ..")
    os.system("git clone https://github.com/The-Burning/blackeye-im.git")
    os.system('chmod +x setup.sh')
    os.system('chmod +x blackeye.sh')
    os.system("cd ..")
    os.system("cd ..")
    os.system("git clone https://github.com/Vishnusharma55/TBomb.git")
    os.system("cd TBomb")
    os.system('chmod +x TBomb.sh')
    os.system("pip3 install tbomb")
    os.system("cd ..")
    os.system("git clone https://github.com/yorkox0/autoBspwm.git")
    os.system('chmod +x main.py')
    os.system("cd ..")
    os.system("git clone https://github.com/thewhiteh4t/seeker.git")
    os.system('chmod +x install.sh')
    os.system('./install.sh')
    os.system("mv cupp/ tools/")
    os.system("mv instainsane/ tools/")
    os.system("mv Password-Generator/ tools/")
    os.system("mv blackeye-im/ tools/")
    os.system("mv TBomb/ tools/")
    os.system("mv autoBspwm/ tools/")
    os.system("mv seeker/ tools/")
    os.system("mv tools/ /")

    white()
    print('[+] Herramientas instaladas correctamente\n\n')
