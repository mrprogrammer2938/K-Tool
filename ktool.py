#!/usr/bin/python3
# This Programm Write by Mr.nope
# K-Tool v1.4.0
import os
import sys
import time
import subprocess
import platform
import webbrowser
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
End = '\033[0m'
line = '\033[4m'
system = platform.uname()[0]
opt = Fore.LIGHTBLUE_EX + "\nKTool" + End + Fore.LIGHTGREEN_EX + line + " ~# " + End + Fore.YELLOW
run_Err = "\nPlease, Run This Programm on Linux, Windows, MacOS!\n"
banner = Fore.BLUE + """
                                                                      
                     ....''','..                                      
                   .....'',:ldxo'                                     
                     ...'',,,,,:c;''....                              
                    .....     .:lc;;;;:cc,.    """ + Fore.RED + "Version: " + Fore.YELLOW + "1.4.0" + Fore.BLUE + """                       
                              cl.      .,lc.                          
                              co.         ..                          
                              .:l:;,,,,,'.                            
                                ..'''',;:cc,.                         
                                          .;,.                        
                                           ...                        
                                            .       \n""" + End
black_Tool_banner = Fore.GREEN + """
██████  ██       █████   ██████ ██   ██   ████████  ██████   ██████  ██      
██   ██ ██      ██   ██ ██      ██  ██       ██    ██    ██ ██    ██ ██      
██████  ██      ███████ ██      █████  █████ ██    ██    ██ ██    ██ ██      
██   ██ ██      ██   ██ ██      ██  ██       ██    ██    ██ ██    ██ ██      
██████  ███████ ██   ██  ██████ ██   ██      ██     ██████   ██████  ███████ 
        """ + End
def title():
    if system == 'Linux':
        os.system("printf '\033]2;k-Tool\a'")
    elif system == 'Windows':
        os.system("title K-Tool")
    else:
        print(run_Err)
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(run_Err)
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    start()
def start():
    print("\n{1}.Repositories Clone")
    print("{2}.Termux Pkg Installing")
    print("{3}.Kali Pkg Installing")
    print("{4}.Update & Uninstall")
    print("{5}.Black-Tool (New)")
    print("{0}.Developer")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
        res_clone()
    elif choose == '2':
        termux_pkg()
    elif choose == '3':
        linux_pkg()
    elif choose == '4':
        update_uninstall()
    elif choose == '5':
        black_tool_Installing()
    elif choose == '0':
        dev()
    elif choose == '99':
        ext()
    else:
        main()
def try1():
    try_to_main_menu = input("\nDo you want Back To Main Menu? [y/n] ")
    if try_to_main_menu == 'y':
        main()
    elif try_to_main_menu == 'n':
        ext()
    else:
        try1()
def try2():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        res_clone()
    elif try_again == 'n':
        try1()
    else:
        try2()
def try3():
    try_again_2 = input("\nDo you want to try again? [y/n] ")
    if try_again_2 == 'y':
        termux_pkg()
    elif try_again_2 == 'n':
        try1()
    else:
        try3()
def try4():
    try_again_3 = input("\nDo you want to try again? [y/n] ")
    if try_again_3 =='y':
        linux_pkg()
    elif try_again_3 == 'n':
        try1()
    else:
        try4()
def try5():
    try_to_menu_2 = input("\nDo you want to back to Update & Uninstalling Menu? [y/n] ")
    if try_to_menu_2 == 'y':
        update_uninstall()
    elif try_to_menu_2 == 'n':
        try1()
    else:
        try5()
def res_clone():
    cls()
    print(banner)
    print("\nUsage: Ctrl + D To Back Main Menu!\n")
    res_name = input("\nEnter Repositories Url: ")
    time.sleep(1)
    run_1 = subprocess.getoutput(f"git clone {res_name}")
    print(f"{res_name} Installed!")
    try2()
def termux_pkg():
    cls()
    print(banner)
    print("\nUsage: Ctrl + D To Back Main Menu!\n")
    pkg_name = input("\nEnter pkg Name: ")
    run_2 = subprocess.getoutput(f"pkg install {pkg_name}")
    print("Pkg {} Installed!".format(run_2))
    try3()
def linux_pkg():
    cls()
    print(banner)
    print("\nUsage: Ctrl + D To Back Main Menu!\n")
    apt_name = input("\nEnter apt name: ")
    run_3 = subprocess.getoutput(f"sudo apt install {apt_name}")
    print("Apt {} Installed!".format(run_3))
    try4()
def update_uninstall():
    cls()
    os.system("figlet -f slant K-Tool|lolcat")
    print("\n{1}.Termux")
    print("{2}.Kali Linux")
    print("{3}.Uninstall Pkg & apt")
    print("{99}.Main Menu")
    choose2 = input(opt)
    if choose2 == '1':
        cls()
        run_4 = subprocess.getoutput("pkg updare && pkg-get upgrade")
        print("Update %100\n")
        time.sleep(0.50)
        try5()
    elif choose2 == '2':
        cls()
        run_5 = subprocess.getoutput("apt update && apt-get upgrade")
        print("Update %100\n")
        try5()
    elif choose2 == '3':
        uninstall_pkg()
    elif choose2 == '99':
        main()
    else:
        update_uninstall()
def dev():
    title()
    print(Fore.GREEN + "\n[" + Fore.RED + "~" + Fore.GREEN +"] " + Fore.LIGHTRED_EX + "Open Github...\n" + End)
    time.sleep(2)
    webbrowser.open_new("https://github.com/mrprogrammer2938")
    title()
    time.sleep(1)
    try1()
def ext():
    cls()
    print(Fore.CYAN + "Mr.nope: " + Fore.GREEN + "Good Bye ;)" + End)
    sys.exit()
def uninstall_pkg():
    cls()
    print(banner)
    print("\n{1}.Termux")
    print("{2}.Kali Linux")
    print("{99}.Menu")
    choose3 = input(opt)
    if choose3 == '1':
        termux_un()
    elif choose3 == '2':
        kali_un()
    elif choose3 == '99':
        update_uninstall()
    else:
        uninstall_pkg()
def black_tool_Installing():
    cls()
    print(Fore.GREEN)
    os.system("figlet Black-Tool")
    print(End)
    print("\n{1}.Kali Black-Tool")
    print("{2}.Termux Black-Tool")
    print("{3}.Windows Black-Tool")
    print("{99}.Main Menu")
    choose_black = input(opt)
    if choose_black == '1':
        cls()
        print(black_Tool_banner)
        print("\nInstalling...")
        installing = subprocess.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool")
        print("Black-Tool Installed!")
        try11()
    elif choose_black == '2':
        cls()
        print(black_Tool_banner)
        print("\nInstalling")
        installing_2 = subproces.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-Termux")
        try11()
    elif choose_black ==  '3':
        cls()
        print(black_Tool_banner)
        print("\nInstalling")
        installing_3 = subproces.getoutput("git clone https://github.com/mrprogrammer2938/Black-Tool-For-Windows")
        try11()
    elif choose_black == '99':
        main()
    else:
        black_tool_Installing()
def termux_un():
    cls()
    print(banner)
    apt_pkg_ter_name = input("\nEnter Pkg Name: ")
    run_6 = subprocess.getoutput(f"pkg uninstall {apt_pkg_ter_name}")
    print(f"{apt_pkg_ter_name} Uninstalled!")
    try7()
def kali_un():
    cls()
    print(banner)
    apt_pkg_ter_name_2 = input("\nEnter Apt Name: ")
    run_7 = subprocess.getoutput(f"pkg uninstall {apt_pkg_ter_name_2}")
    print(f"{apt_pkg_ter_name_2} Uninstalled!")
    try8()
def try11():
    try_to_menu_3 = input("\nDo you want to try again? [y/n]  ")
    if try_to_menu_3 == 'y':
        black_tool_Installing()
    elif try_to_menu_3 == 'n':
        try1()
    else:
        try11()
def try7():
    try_again_3 = input("\nDo you want to try again? [y/n] ")
    if try_again_3 == 'y':
        termux_un()
    elif try_again_3 ==  'n':
        try9()
    else:
        try7()
def try9():
    try_again_4 = input("\nDo you want to Back Uninstalling Menu? [y/n] ")
    if try_again_4 == 'y':
        uninstall_pkg()
    elif try_again_4 == 'n':
        try5()
    else:
        try9()
def try8():
    try_again_5 = input("\nDo you want to try again? [y/n] ")
    if try_again_5 == 'y':
        kali_un()
    elif try_again_5 == 'n':
        try10()
    else:
        try8()
def try10():
    try_again_6 = input("\nDo you want to Back Uninstalling Menu? [y/n] ")
    if try_again_6 == 'y':
        uninstall_pkg()
    elif try_again_6 == 'n':
        try5()
    else:
        try10()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print(End +"\nCtrl + C")
            print(
                  "\nExiting...")
            sys.exit()
    except EOFError:
        try1()