#!/usr/bin/python3
# coding=utf-8

import os
import apt
import sys
import time
import locale
import filecmp
import argparse
import platform
#import subprocess   ## TODO // Remove if not necessary
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')

print("\x1b[8;50;140t")

d = Dialog(dialog="dialog", autowidgetsize=True)

# ++ VARIABLES FOR FOLDER PATHS ++ #
help_folder =     '../menus/help/'
payload_folder =  '../payloads/ducky/'
exports_folder =  '../payloads/exports/'
firmware_folder = '../tools/ducky/USB-Rubber-Ducky/ducky-flasher/Firmware/'
# -- VARIABLES FOR FOLDER PATHS -- #

# ++ DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) ++ #
linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:
    isKali = True

else:
    isKali = False
# -- DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) -- #

# ++ FUNCTION FOR DISPLAYING A SCROLLABLE TEXT BOX WITH THE HELP FILE ++ #
def ducky_help():

    ## TODO // Update the README File with current features and functionalities

    if current_menu == 'main_menu':

        d.textbox(help_folder + '/payloads_menu', height=None, width=None, title="Payloads Menu Help")

        ducky_main_menu()

    if current_menu == 'tag_proc_menu':

        d.textbox(help_folder + '/payload_functions', height=None, width=None, title="Payload Functions Help")

        tag_proc()

    if current_menu == 'flash_firmware_menu':

        d.textbox(help_folder + '/flash_firmware', height=None, width=None, title="Firmware FLashing Help")

        flash_firmware_menu()
# -- FUNCTION FOR DISPLAYING A SCROLLABLE TEXT BOX WITH THE README FILE -- #

# ++ FUNCTION FOR EDITING THE SELECTED PAYLOAD, STORING THE RESULT & RETURN TO TAG_PROC MENU ++ #
def edit_payload():

    global ptext

    if os.path.exists(exports_folder + script_names[script_number]):

        pcode, ptext = d.editbox(exports_folder + script_names[script_number], height=0, width=0, title="Editing File " + exports_folder + script_names[script_number])

    else:

        pcode, ptext = d.editbox(payload_folder + script_names[script_number], height=0, width=0, title="Editing File " + payload_folder + script_names[script_number])


    if pcode == d.OK:

        with open(exports_folder + script_names[script_number], 'w') as f:
            f.write(ptext)

        d.msgbox("Payload has been successfully written to\n" + exports_folder + script_names[script_number])

        tag_proc()

    if pcode == d.CANCEL:
        tag_proc()

# -- FUNCTION FOR EDITING THE SELECTED PAYLOAD, STORING THE RESULT & RETURN TO TAG_PROC MENU -- #

# ++ FUNCTION FOR ENCODING THE CURRENTLY SELECTED PAYLOAD IN ITS ORIGINAL OR MODIFIED STATE ++ #
def encode_payload():
    fcode, fstring = d.inputbox("Please enter the path to your\nUSB Rubber Ducky SD Card\n\nThis is usually somewhere under /media/SDCARD/", height=0, width=0, init='/media/')

    if fcode == d.OK:

        if os.path.exists(exports_folder + script_names[script_number]):

            encode_result = os.system('java -jar ../tools/ducky/USB-Rubber-Ducky/duckencoder.jar -i ' + exports_folder + script_names[script_number] + ' -o ' + fstring + 'inject.bin')

            if encode_result == 0:
                d.msgbox("\nThe payload has been exported successfully!", height=8, width=35, title="Encode Payload Result")
                tag_proc()

            else:
                d.msgbox("\nAn error occured while encoding the payload!", title="Encode Payload Result")
                tag_proc()

        elif os.path.exists(payload_folder + script_names[script_number]):

            encode_result = os.system('java -jar ../tools/ducky/USB-Rubber-Ducky/duckencoder.jar -i ' + payload_folder + script_names[script_number] + ' -o ' + fstring + 'inject.bin')

            if encode_result == 0:
                d.msgbox("\nThe payload has been exported successfully!", height=8, width=35, title="Encode Payload Result")
                tag_proc()

            else:
                d.msgbox("\nAn error occured while encoding the payload!", title="Encode Payload Result")
                tag_proc()

    if fcode == d.CANCEL:
        tag_proc()
# -- FUNCTION FOR ENCODING THE CURRENTLY SELECTED PAYLOAD IN ITS ORIGINAL OR MODIFIED STATE -- #

def delete_payload():

    if os.path.exists(exports_folder + script_names[script_number]):

        yncode = d.yesno("\nAn exported payload file has been found at\n" + exports_folder + script_names[script_number] + ".\n\nAre you sure you want to delete this file?", title="Delete Exported File?", yes_label="YES", no_label="NO")

        if yncode == d.OK:

            os.remove(exports_folder + script_names[script_number])
            tag_proc()

        else:
            tag_proc()

    else:
        d.msgbox("\nAn exported payload could not be found at\n" + exports_folder + script_names[script_number], width=45, height=8, title='Delete Payload')
        tag_proc()

# ++ FUNCTION FOR FLASHING DIFFERENT FIRMWARES TO THE USB RUBBER DUCKY (CURRENTLY SUPPORTS 6 FW'S) ++ #
def flash_firmware_updater(firmware):

    ## TODO // First version of the updater as a prototype. Intending to rewrite in the future

    odf_count = 0

    d.gauge_start(title="Flashing The Ducky, Please Wait...")

    d.gauge_update(33, "Erasing Firmware...", update_text= True);

    odf_count += os.system('sudo dfu-programmer at32uc3b1256 erase');

    time.sleep(1);

    d.gauge_update(67, "Flashing Firmware...", update_text= True);

    odf_count += os.system('sudo dfu-programmer at32uc3b1256 flash --suppress-bootloader-mem --quiet ' + firmware_folder + firmware);

    time.sleep(1);

    d.gauge_update(100, "Resetting Ducky...", update_text= True);

    odf_count += os.system('sudo dfu-programmer at32uc3b1256 reset');

    time.sleep(1)

    d.gauge_stop()

    if odf_count == 0:

        d.msgbox("\nOriginal Duck Firmware has been flashed successfully",
                 title="Firmware Status")

        tag_proc()

    else:

        d.msgbox("\nAn error occured while flashing the ducky.\n\nPlease ensure the following and try again:\n\n1. 'dfu-programmer' is installed. You can attempt to install it with\n\t\t\t'apt-get install dfu-programmer'.\n\n2. You have placed the ducky in DFU Programming Mode by holding the\n\t\t\tbutton while plugging in the ducky and then try flashing again.",
                 title="Firmware Status")

        flash_firmware_menu()
# -- FUNCTION FOR FLASHING DIFFERENT FIRMWARES TO THE USB RUBBER DUCKY (CURRENTLY SUPPORTS 6 FW'S) -- #

# ++ FUNCTION TO PROVIDE A MENU TO SELECT A DUCKY FIRMWARE TO FLASH (CURRENTLY SUPPORTS 6 FW'S) ++ #
def flash_firmware_menu():

    global current_menu

    current_menu = 'flash_firmware_menu'

    firmwares = ['duck_v2.hex', 'USB_v2.hex', 'm_duck_v2.hex', 'c_duck_v2.hex', 'c_duck_v2_S001.hex', 'c_duck_v2_S002.hex']

    flash_desc = "\nThis menu will allow you to flash a specific firmware to the USB Rubber Ducky\n\nIn order to do so, you must place your ducky in DFU Programming Mode\nby holding down the button while plugging it in\n\nSee the help section for more information on firmwares"

    fp_code, fp_tag = d.radiolist(flash_desc, height=None, width=None, list_height=None, title="Select Ducky Firmware To Flash",
                choices=[("Original Duck Firmware", "The original ducky firmware", False),
                         ("FAT Duck", "Turns the ducky into a USB Mass Storage Device", False),
                         ("Detour Duck", "A firmware that supports multiple payloads", False),
                         ("Twin Duck", "HID injection and Mass Storage support", False),
                         ("Twin Duck Special Request 1", "Executes payload on LED trigger (Cap Locks, Num Locks, etc)", False),
                         ("Twin Duck Special Request 2", "Executes payload on pressing the GPIO pin", False)],
                         help_button=True)

    if fp_code == d.OK:

        if fp_tag == "Original Duck Firmware":

            flash_firmware_updater(firmwares[0])

        if fp_tag == "FAT Duck":

            flash_firmware_updater(firmwares[1])

        if fp_tag == "Detour Duck":

            flash_firmware_updater(firmwares[2])

        if fp_tag == "Twin Duck":

            flash_firmware_updater(firmwares[3])

        if fp_tag == "Twin Duck Special Request 1":

            flash_firmware_updater(firmwares[4])

        if fp_tag == "Twin Duck Special Request 2":

            flash_firmware_updater(firmwares[5])

    if fp_code == d.HELP:
        ducky_help()

    if fp_code == d.CANCEL:
        tag_proc()
# -- FUNCTION TO PROVIDE A MENU TO SELECT A DUCKY FIRMWARE TO FLASH (CURRENTLY SUPPORTS 6 FW'S) -- #

# ++ FUNCTION TO PROVIDE A MENU TO PROCESS EACH TAG ASSIGNED PAYLOAD (CURRENTLY SUPPORTS 4 FUNCTIONS) ++ #
def tag_proc():

    global tp_code, tp_tag, current_menu

    current_menu = 'tag_proc_menu'

    tp_code, tp_tag = d.menu("\n" + desc_tag,
                                choices=[("Edit Payload", "Edits the currently selected payload"),
                                #("Export Payload", "Exports the original or edited payload to the 'payloads/exports' folder"),
                                ("Encode Payload", "Encodes the original or edited payload to a folder or SD card"),
                                ("Delete Payload", "Deletes the exported payload from /payloads/exports/ if it exists"),
                                ("Flash Firmware", "Flashes a specific firmware to the USB Rubber Ducky")],
                                title=main_tag,
                                help_button=True)

    if tp_code == d.OK:

        if tp_tag == "Edit Payload":
            edit_payload()

        if tp_tag == "Export Payload":
            export_payload()

        if tp_tag == "Encode Payload":
            encode_payload()

        if tp_tag == "Delete Payload":
            delete_payload()

        if tp_tag == "Flash Firmware":
            flash_firmware_menu()

    if tp_code == d.HELP:
        ducky_help()

    if tp_code == d.CANCEL:
        ducky_main_menu()
# -- FUNCTION TO PROVIDE A MENU TO PROCESS EACH TAG ASSIGNED PAYLOAD (CURRENTLY SUPPORTS 4 FUNCTIONS) -- #

# ++ FUNCTION FOR THE DUCKY PAYLOADS MAIN MENU ++ #
def ducky_main_menu():

    global main_code, main_tag, desc_tag, script_names, script_number, current_menu

    current_menu = 'main_menu'

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

    if main_code == d.OK:

        if main_tag == "Hello World":
            script_number = '01'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()


    if main_code == d.HELP:
        ducky_help()

    if main_code == d.CANCEL:
        sys.exit("Exiting Gracefully | Thank You For Using TSK!")
# ++ FUNCTION FOR THE DUCKY PAYLOADS MAIN MENU ++ #


#################################################
# START MAIN ROUTINES
#################################################
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
