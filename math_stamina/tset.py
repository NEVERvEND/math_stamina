import random
import os
import time



#COLORS
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'


RESET = '\033[0m' # called to return to standard terminal text color
#-------0


RUN = True
score = 0
list_symvol = ["+","-","/","*","//","%"]


os.system('cls')
while RUN:
    line = f"{random.randint(-100,100)} {list_symvol[random.randint(0,len(list_symvol)-1)]} {random.randint(-100,100)}"
    print("-"*10)
    print(f"u score - {BLUE}{score}{RESET}")
    res = input(f"{YELLOW}{line} = {RESET}")


    if res == "Exit":
        print("gl :)")
        print(f"u res - {BLUE}{score}{RESET}")
        RUN = False

    elif res in ("-","skip"):
        print("skip")
        score -= 0.5
        

    elif int(res) == eval(line):
        print(f"{BRIGHT_GREEN}Yep{RESET}")
        score += 1
        

    else:
        print(f"{BRIGHT_RED}No{RESET}")
        score -= 1
    
    print(f"right res - {BLUE}{eval(line)}{RESET}")
    input("end to continue...")
    os.system('cls')
