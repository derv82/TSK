#!/usr/bin/python3
# coding=utf-8

import os
import apt
import platform

locale.setlocale(locale.LC_ALL, '')

simple_ducky_tools_folder = './tools/ducky/simple-ducky/'
simple_ducky_local_folder = '/usr/share/simple-ducky/'

apt_cache = apt.Cache()

linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:
    isKali = True

else:
    isKali = False


def simple_ducky_checker():

    if os.path.exists(simple_ducky_local_folder):
        os.system(simple_ducky_tools_folder + 'update.sh')
        os.system('simple-ducky')

    else:

        while True:

            install_confirm = input("simple-ducky was not found, would you like to install now (y/N)? ")

            if install_confirm == 'y' or install_confirm == 'Y':

                os.system(simple_ducky_tools_folder + 'install.sh')

            elif install_confirm == 'n' or install_confirm == 'N':

                print("simple-ducky must be installed before it can be launched.\nPlease install simple-ducky and try again.")


def ducky_routines():

    if os.getuid() == 0:

        try:

            if isKali:

                #print("\x1b[8;50;140t")

                os.system('clear')

                simple_ducky_checker()

            else:

                os.system('clear')

                print("This version of TSK is currently designed to run on Kali Linux only!")

        except KeyboardInterrupt:

            print("Exiting in a HURRY!\n")

            sys.exit(0)
    else:

        os.system('clear')

        exit("If you liked it then you should have run it as admin!")

## ++ MAIN ROUTINE ++ ##
if __name__ == '__main__':

    os.system('clear')

    # For now preventing module functionality unless run from within TSK main menu
    print("This module is intended to be run from within the TSK main program only!")
## -- MAIN ROUTINE -- ##
