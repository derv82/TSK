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

    ## TODO // Add a section for users to write their custom payloads in the editor and save them to a customs dir under /payloads/ducky/customs /payloads/bunny/customs etc. Also performing the same dynamic processing as listed above.

    script_names = {'01' : '01_Hello_World', '02' : '02_WiFi_Password_Grabber', '03' : '03_Basic_Terminal_Commands_Ubuntu', '04' : '04_Information_Gathering_Ubuntu', '05.1' : '05.1_Hide_CMD_Window', '05.2' : '05.2_Hide_CMD_Window', '05.3' : '05.3_Hide_CMD_Window', '06' : '06_Netcat_FTP_Download_And_Reverse_Shell', '07.1' : '07.1_Wallpaper_Prank', '07.2' : '07.2_Wallpaper_Prank', '07.3' : '07.3_Wallpaper_Prank', '08' : '08_Wallpaper_Prank', '09' : '09_Reverse_Shell',
                    '10' : '10_Reverse_Shell_With_Persistence', '11.1' : '11.1_Fork_Bomb', '11.2' : '11.2_Fork_Bomb', '12' : '12_Utilman_Exploit', '13' : '13_WiFi_Backdoor', '14' : '14_Non_Malicious_Auto_Defacer', '15' : '15_Lock_Your_Computer_Message', '16' : '16_Ducky_Downloader', '17' : '17_Ducky_Phisher', '18' : '18_FTP_Download_Upload', '19' : '19_Restart_Prank', '20.1' : '20.1_Silly_Mouse_Windows_Is_For_Kids', '20.2' : '20.2_Silly_Mouse_Windows_Is_For_Kids',
                    '21.1' : '21.1_Windows_Screen_Rotation_Hack', '21.2' : '21.2_Windows_Screen_Rotation_Hack', '22.1' : '22.1_Powershell_Wget_Execute', '22.2' : '22.2_Powershell_Wget_Execute', '22.3' : '22.3_Powershell_Wget_Execute', '23.1' : '23.1_Mimikatz_Payload', '23.2' : '23.2_Mimikatz_Payload', '24' : '24_MobileTabs', '25' : '25_Create_Wireless_Network_Association_Auto_Connect_Pineapple', '26.1' : '26.1_Retrieve_SAM_And_SYSTEM_From_A_Live_File_System',
                    '26.2' : '26.2_Retrieve_SAM_And_SYSTEM_From_A_Live_File_System', '27' : '27_Ugly_Rolled_Prank', '28' : '28_XMAS', '29' : '29_Pineapple_Association_Very_Fast', '30' : '30_WiFun', '31' : '31_MissDirection', '32' : '32_Remotely_Possible', '33' : '33_Batch_Wiper_Drive_Eraser', '34' : '34_Generic_Batch', '35' : '35_Paint_Hack', '36' : '36_Local_DNS_Poisoning', '37' : '37_Deny_Net_Access', '38.1' : '38.1_Run_EXE_From_SD', '38.2' : '38.2_Run_EXE_From_SD',
                    '38.3' : '38.3_Run_EXE_From_SD', '39' : '39_Run_JAVA_From_SD', '40' : '40_OSX_Sudo_Passwords_Grabber', '41' : '41_OSX_Root_Backdoor', '42' : '42_OSX_User_Backdoor', '43' : '43_OSX_Local_DNS_Poisoning', '44' : '44_OSX_YouTube_Blaster', '45' : '45_OSX_Photo_Booth_Prank', '46' : '46_OSX_Internet_Protocol_Slurp', '47' : '47_OSX_ASCII_Prank', '48' : '48_OSX_iMessage_Capture', '49' : '49_OSX_Grab_Minecraft_Account_Password_And_Upload_To_FTP',
                    '50' : '50_OSX_Wget_And_Execute', '51' : '51_OSX_Passwordless_SSH_Access', '52' : '52_OSX_Bella_RAT_Installation', '53' : '53_OSX_Sudo_For_All_Users_Without_Password', '54' : '54_Mr_Grays_Rubber_Hacks', '55' : '55_Copy_File_To_Desktop', '56' : '56_YouTube_Roll', '57' : '57_Disable_AVG_2012', '58' : '58_Disable_AVG_2013', '59' : '59_EICAR_AV_Test', '60' : '60_Download_Mimikatz_Grab_Passwords_And_Email', '61' : '61_Hotdog_Wallpaper', '62' : '62_Android_5.x_Lockscreen',
                    '63' : '63_Chrome_Password_Stealer', '64' : '64_Website_Lock', '65' : '65_Windows_10_Download_And_Execute_File_With_Powershell', '66' : '66_Windows_10_Disable_Windows_Defender', '67' : '67_Windows_10_Disable_Windows_Defender_Through_Powershell', '68.1' : '68.1_Windows_7_Logoff_Prank', '68.2' : '68.2_Windows_7_Logoff_Prank', '69' : '69_Netcat_Reverse_Shell', '70' : '70_Fake_Update_Screen', '71' : '71_Rickroll'}

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
                                ],
                       title="HAK5 USB Rubber Ducky Payload Collection",
                       backtitle="TSK | USB Rubber Ducky Menu",
                       no_shadow=True,
                       help_button=True,)

    if main_code == d.OK:
        ## TODO // Add a help_desc variable to hold the help descriptions from the wiki pages which displays in a msgbox before the edit window displays. If help_desc = '' then show no msgbox
        if main_tag == "Hello World":
            script_number = '01'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "WiFi Password Grabber":
            script_number = '02'
            desc_tag = "Grabs, Logs and Emails WiFi Passwords"
            tag_proc()

        if main_tag == "Basic Terminal Commands Ubuntu":
            script_number = '03'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Information Gathering Ubuntu":
            script_number = '04'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Hide CMD Window 1":
            script_number = '05.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Hide CMD Window 2":
            script_number = '05.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Hide CMD Window 3":
            script_number = '05.3'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Netcat FTP Download & Reverse Shell":
            script_number = '06'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Wallpaper Prank 1":
            script_number = '07.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Wallpaper Prank 2":
            script_number = '07.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Wallpaper Prank 3":
            script_number = '07.3'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "You Got Quacked!":
            script_number = '08'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Reverse Shell":
            script_number = '09'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Reverse Shell + Persistence":
            script_number = '10'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Fork Bomb 1":
            script_number = '11.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Fork Bomb 2":
            script_number = '11.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Utilman Exploit":
            script_number = '12'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "WiFi Backdoor":
            script_number = '13'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Non Malicious Auto Defacer":
            script_number = '14'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Lock Your Computer Message":
            script_number = '15'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Ducky Downloader":
            script_number = '16'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Ducky Phisher":
            script_number = '17'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "FTP Download/Upload":
            script_number = '18'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Restart Prank":
            script_number = '19'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Silly Mouse, Windows Is For Kids 1":
            script_number = '20.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Silly Mouse, Windows Is For Kids 2":
            script_number = '20.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Windows Screen Rotation Hack 1":
            script_number = '21.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Windows Screen Rotation Hack 2":
            script_number = '21.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Powershell Wget Execute 1":
            script_number = '22.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Powershell Wget Execute 2":
            script_number = '22.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Powershell Wget Execute 3":
            script_number = '22.3'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Mimikatz Payload 1":
            script_number = '23.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Mimikatz Payload 2":
            script_number = '23.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "MobileTabs":
            script_number = '24'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Create Wireless Network Association":
            script_number = '25'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Retrieve SAM & SYSTEM From a Live File System 1":
            script_number = '26.1'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Retrieve SAM & SYSTEM From a Live File System 2":
            script_number = '26.2'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Ugly Rolled Prank":
            script_number = '27'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "XMAS":
            script_number = '28'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Pineapple Association":
            script_number = '29'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "WiFun":
            script_number = '30'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "MissDirection":
            script_number = '31'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Remotely Possible":
            script_number = '32'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Batch Wiper Drive Eraser":
            script_number = '33'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Generic Batch":
            script_number = '34'
            desc_tag = "A payload for testing the USB Rubber ducky’s functionality"
            tag_proc()

        if main_tag == "Paint Hack":
            script_number = '35'
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
