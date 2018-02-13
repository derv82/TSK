#!/usr/bin/python3
# coding=utf-8

import os
import apt
import sys
import time
import locale
#import filecmp
import argparse
import platform
import webbrowser
#import subprocess   ## TODO // Remove if not necessary
from dialog import Dialog


d = Dialog(dialog="dialog", autowidgetsize=True)

# ++ DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) ++ #
linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:

    isKali = True

else:

    isKali = False
# -- DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) -- #

# ++ FUNCTION TO PROVIDE A MAIN MENU OF EXTRA DUCKY FUNCTIONS ++ #

def main_menu():

    global tp_tag, current_menu

    current_menu = 'main_menu'

    mm_code, mm_tag = d.menu('Select an option below:',
                                choices=[("Custom Payload Editor", "Opens an editor for writing a custom ducky payload"),
                                ("Duck Toolkit NG", "Web based Encoders, Decoders, Payloads and other tools"),
                                ("USB Rubber Ducky Docs", "Opens the HAK5 USB Rubber Ducky Documentation Web Site"),
                                ("USB Rubber Ducky Forum", "Opens the HAK5 USB Rubber Ducky Forums Web Site"),],
                                title='USB Rubber Ducky Extra Resources | Main Menu',
                                help_button=True)

    if mm_code == d.OK:

        if mm_tag == "Custom Payload Editor":
            custom_payload()

        if mm_tag == "Duck Toolkit NG":
            webbrowser.open_new('https://ducktoolkit.com/')
            d.infobox("Opening the Duck Toolkit NG Web Site in your browser\n\nPlease wait...")
            time.sleep(3)
            main_menu()

        if mm_tag == "USB Rubber Ducky Docs":
            webbrowser.open_new('https://www.hak5.org/gear/usb-rubber-ducky/docs')
            d.infobox("Opening the USB Rubber Ducky Documentation Web Site in your browser\n\nPlease wait...")
            time.sleep(3)
            main_menu()

        if mm_tag == "USB Rubber Ducky Forums":
            webbrowser.open_new('https://forums.hak5.org/forum/56-usb-rubber-ducky/')
            d.infobox("Opening the USB Rubber Ducky Forums Web Site in your browser\n\nPlease wait...")
            time.sleep(3)
            main_menu()

    if mm_code == d.HELP:
        ducky_help()

    if mm_code == d.CANCEL:

        d.infobox("Returning to the TSK Main Menu...\nQUACK QUACK!", width=37, height=5)

        time.sleep(3)


# -- FUNCTION TO PROVIDE A MAIN MENU OF EXTRA DUCKY FUNCTIONS -- #

def custom_payload():

    cp_yesno = d.yesno('This will ', height=None, width=None, yes_label='Yes', no_label='No')

# ++ STARTUP FUNCTION TO VERIFY OS AND LAUNCH MAIN_MENU ETC ++ #
def ducky_routines():

    if os.getuid() == 0:

        try:

            if isKali:

                #print("\x1b[8;50;140t")

                os.system('clear')

                main_menu()

            else:

                os.system('clear')

                print("This version of TSK is currently designed to run on Kali Linux only!")

        except KeyboardInterrupt:

            print("Exiting in a HURRY!\n")

            sys.exit(0)
    else:

        os.system('clear')

        exit("If you liked it then you should have run it as admin!")

# -- STARTUP FUNCTION TO VERIFY OS AND LAUNCH MAIN_MENU ETC -- #

## ++ MAIN ROUTINE ++ ##
if __name__ == '__main__':

    os.system('clear')

    # For now preventing module functionality unless run from within TSK main menu
    print("This module is intended to be run from within the TSK main program only!")
## -- MAIN ROUTINE -- ##



## TODO // REMOVE THIS BEFORE EDITING ==> Up next is a curses menu with option for Custom Payload Editing / Firmware Flashing |
## TODO // / Encoding -> Such as featured in the HAK5 payloads menu. Also an extra resources section which links to           <
## TODO // The HAK5 docs web site and forums and duck toolkit NG.
