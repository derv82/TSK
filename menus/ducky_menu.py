#!/usr/bin/python3
# coding=utf-8

import os
import apt
import sys
import time
import locale
import argparse
import platform
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')

print("\x1b[8;50;140t")

payload_folder = '../payloads/ducky/'
exports_folder = '../payloads/exports/'

d = Dialog(dialog="dialog", autowidgetsize=True)

button_names = {d.OK:     "OK",
                d.CANCEL: "Cancel",
                d.HELP:   "Help",
                d.EXTRA:  "Extra"}

linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:
    isKali = True

else:
    isKali = False

def main_menu_cancel():

    if d.CANCEL:
        sys.exit(0)

def payload_cancel():

    if d.CANCEL:
        ducky_main_menu()

def ducky_help_menu():

    help_file = "README.md"
    d.textbox(help_file, height=None, width=None)
    ducky_main_menu()

def tag_proc():
    global curr_code, curr_tag

    curr_code, curr_tag = d.menu("\n" + desc_tag,
                                choices=[("Edit Payload", "Edits the currently selected payload"),
                                ("Export Payload", "Exports the original or edited payload to the 'payloads/exports' folder"),
                                ("Flash Payload", "Flashes the original or edited payload to the USB Rubber Ducky"),],
                                title=main_tag)

def ducky_main_menu():
    global ptext, main_code, main_tag, desc_tag

    script_names = {'01' : '01_Hello_World', '02' : '02_WiFi_Password_Grabber', '03' : '03_Basic_Terminal_Commands_Ubuntu', '04' : '04_Information_Gathering_Ubuntu'}

    main_code, main_tag = d.menu("\nSelect a payload below for more options",
                       choices=[("Hello World", "A payload for testing the USB Rubber ducky’s functionality"),
                                ("WiFi Password Grabber", "Grabs, Logs and Emails WiFi Passwords"),
                                ("Basic Terminal Commands Ubuntu", "Example of how to execute commands in Ubuntu through Xterm"),
                                ("Information Gathering Ubuntu", "Collects info from a running Ubuntu OS and saves it to a file"),
                                ("Hide CMD Window 1", "Example of how to hide the Windows Command Prompt - Version 1"),
                                ("Hide CMD Window 2", "Example of how to hide the Windows Command Prompt - Version 2"),
                                ("Hide CMD Window 3", "Example of how to hide the Windows Command Prompt - Version 3"),
                                ("Netcat FTP Download & Reverse Shell", "Log into FTP Server and start a Netcat reverse shell"),
                                ("Wallpaper Prank 1", "The ol' set your disabled desktop as your wallpaper prank - Version 1"),
                                ("Wallpaper Prank 2", "The ol' set your disabled desktop as your wallpaper prank - Version 2"),
                                ("Wallpaper Prank 3", "The ol' set your disabled desktop as your wallpaper prank - Version 3"),
                                ("You Got Quacked!", "Changes the users desktop background to “YOU GOT QUACKED!” with a Hak5 logo"),
                                ("Reverse Shell", "Uses some ASCII to Binary tricks to open a reverse shell"),
                                ("Reverse Shell + Persistence", "Persistent netcat reverse shell that runs in the background every 5 minutes"),
                                ("Fork Bomb 1", "Creates a Fork Bomb batch file in startup for Windows 7"),
                                ("Fork Bomb 2", "Creates a Fork Bomb batch file in startup for Windows 10"),
                                ("Utilman Exploit", "Uses the Utilman.exe Exploit to create a new local administrator account"),
                                ("WiFi Backdoor", "Open a CMD bypassing UAC then create a wireless access point"),
                                ("Non Malicious Auto Defacer", "Automatically defaces index page of an apache web server"),
                                ("Lock Your Computer Message", "Opens notepad and types a message concerning locking the computer"),
                                ("Ducky Downloader", "Opens the command prompt & creates a VBscript to download a file from any URL"),
                                ("Ducky Phisher", "Modifies hosts file to redirect web sites to a site of your choosing"),
                                ("FTP Download/Upload", "Downloads WinSCP and uploads the user profile, recursive, to a FTP server"),
                                ("Restart Prank", "Adds a batch file to startup to restart the users PC"),
                                ("Silly Mouse, Windows Is For Kids", "Changes cursor to loading sign and kills windows explorer"),
                                ("Powershell Wget Execute 1", "Execute Powershell script from run box - Version 1"),
                                ("Powershell Wget Execute 2", "Execute Powershell script from run box - Version 2"),
                                ("Powershell Wget Execute 3", "Execute Powershell script from run box - Version 3"),
                                ("Mimikatz Payload 1", "Downloads mimikatz from web server and grabs passwords - Version 1"),
                                ("Mimikatz Payload 2", "Downloads mimikatz from web server and grabs passwords - Version 2"),
                                ("MobileTabs", "Sends command line arguments to IE to open tabs of your choosing"),
                                ("Create Wireless Network Association", "Creates a network association for the wifi pineapple"),
                                ("Retrieve SAM & SYSTEM From a Live File System 1", "Grabs the SAM and SYSTEM files for hash retrieval later on - Version 1")
                                ],
                       title="HAK5 USB Rubber Ducky Payload Collection",
                       backtitle="TSK | USB Rubber Ducky Menu",
                       no_shadow=True,
                       help_button=True,)


    if main_code == d.CANCEL:
        print(title)
        main_menu_cancel()

    if main_code == d.OK:

        if main_tag == "Hello World":
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

            if curr_code == d.OK:

                if curr_tag == "Edit Payload":
                    pcode, ptext = d.editbox(payload_folder + script_names['01'], height=0, width=0)

                    if pcode == d.CANCEL:
                        tag_proc()

                if curr_tag == "Export Payload":
                    pfo = open(exports_folder + script_names['01'], 'w')
                    pfo.write(ptext)
                    pfo.close()

                if curr_code == d.CANCEL:
                    pass

            payload_cancel()

    if main_code == d.HELP:
        ducky_help_menu()


if os.getuid() == 0:

    try:
    # On startup, set the menuLoop variable for menu choices, check dependencies and print the main menu
        if not isKali:

            os.system('clear')

            ducky_main_menu()

        else:

            os.system('clear')

            print("This version of TSK is currently designed to run on Kali Linux only!")

    except KeyboardInterrupt:

        print("Exiting in a HURRY!\n")

        sys.exit(0)
else:

    os.system('clear')

    exit("If you liked it then you should have run it as admin!")
