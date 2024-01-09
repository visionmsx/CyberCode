from time import sleep
from os import system
import time
from colorama import Fore, Style

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(0.01)

system("cls||clear")
printLow("""{}                                   
CyberCode
    """.format(Fore.RED))

printLow(Style.RESET_ALL + Fore.BLUE +'                                                                                 Vision and Proto\n')
