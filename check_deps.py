#!/usr/bin/python3
# coding=utf-8

import os
import apt
import sys
import time
import platform
from colorama import init, Fore, Back, Style

# Function to check for installation of a few dependencies
def dep_checks():

    #FR = Fore.RED; FW = Fore.WHITE; FG = Fore.GREEN; FB = Fore.BLACK; FY = Fore.YELLOW; FM = Fore.MAGENTA; FBL = Fore.BLUE; FLB = Fore.LIGHTBLUE_EX; FLW = Fore.LIGHTWHITE_EX; FLBL = Fore.LIGHTBLACK_EX
    #BLB = Back.LIGHTBLACK_EX;  BR = Back.RED; BW = Back.WHITE; BB = Back.BLUE; BG = Back.GREEN; BM = Back.MAGENTA; BY = Back.YELLOW
    #SRST = Style.RESET_ALL; SB = Style.BRIGHT; SD = Style.DIM; SN = Style.NORMAL; BRST = Back.RESET; FRST = Fore.RESET

    # Are we running inside Kali Linux?
    apt_cache = apt.Cache()

    linux_distro = platform.linux_distribution()

    if 'Kali' in linux_distro:
        isKali = True

    else:
        isKali = False

    # `Kali` Linux Dependencies

    if isKali:

        apt_cache.open()

        os.system('clear')

        depsCheck = input("Check for dependencies? ")

        if depsCheck == 'y' or depsCheck == 'Y':

            os.system('pip3 install -r requirements.txt')

            if apt_cache["fonts-font-awesome"].is_installed == True:

                print("\n[+] Font-Awesome        [INSTALLED]")
                time.sleep(1)

            else:

                print("\n[+] Font-Awesome        [NOT INSTALLED]\n")
                time.sleep(1)

                print("[-] Installing Font-Awesome [ 'apt-get install fonts-font-awesome' ]")
                os.system('apt-get -y update && apt-get -y install fonts-font-awesome')

                print("[-] Rebuilding Font Cache [ 'fc-cache -f']")
                os.system('fc-cache -f')

                print("[+] Font-Awesome        [INSTALLED]")
                time.sleep(1)

            if apt_cache["python3-dialog"].is_installed == True:

                print("[+] pythondialog        [INSTALLED]")
                time.sleep(1)

            else:

                print("[+] pythondialog        [NOT INSTALLED]\n")
                time.sleep(1)

                print("[-] Installing pythondialog [ 'apt-get install python3-dialog' ]")
                os.system('apt-get -y update && apt-get -y install python3-dialog')

            if apt_cache["python-apt"].is_installed == True:

                print("[+] python-apt          [INSTALLED]")
                time.sleep(1)

            else:

                print("[+] python-apt        [NOT INSTALLED]\n")
                time.sleep(1)

                print("[-] Installing python-apt [ 'apt-get install python-apt' ]")
                os.system('apt-get -y update && apt-get -y install python-apt')

            if apt_cache["dfu-programmer"].is_installed == True:

                print("[+] dfu-programmer      [INSTALLED]")
                time.sleep(1)

            else:

                print("[+] dfu-programmer    [NOT INSTALLED]\n")
                time.sleep(1)

                print("[-] Installing dfu-programmer [ 'apt-get install dfu-programmer' ]")
                os.system('apt-get -y update && apt-get -y install dfu-programmer')


            print("\n[+] Looking good, continuing")
            time.sleep(1)

    else:

        os.system('clear')

        print("This version of TSK is currently designed to run on Kali Linux only!")

if __name__ == '__main__':
    dep_checks()
