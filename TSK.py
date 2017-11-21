#!/usr/bin/python3
# coding=utf-8

##############################################
# The Skeleton Key v.the first [ 9-11-2017 ] #
# Codename - The Patriotic Penguin           #
#                                            #
# - A project by sandmansandito and derv82 - #
#                                            #
# This is a very experimental first version  #
# Hopefully it should improve over time      #
##############################################

import os
import apt
import sys
import time
import locale
import platform
import subprocess
from dialog import Dialog
from colorama import init, Fore, Back, Style
from future.builtins import input

# Set variable shotcuts for colorama colors
FR = Fore.RED; FW = Fore.WHITE; FG = Fore.GREEN; FB = Fore.BLACK; FY = Fore.YELLOW; FM = Fore.MAGENTA; FBL = Fore.BLUE; FLB = Fore.LIGHTBLUE_EX; FLW = Fore.LIGHTWHITE_EX; FLBL = Fore.LIGHTBLACK_EX
BLB = Back.LIGHTBLACK_EX;  BR = Back.RED; BW = Back.WHITE; BB = Back.BLUE; BG = Back.GREEN; BM = Back.MAGENTA; BY = Back.YELLOW
SRST = Style.RESET_ALL; SB = Style.BRIGHT; SD = Style.DIM; SN = Style.NORMAL; BRST = Back.RESET; FRST = Fore.RESET

# Are we running inside Kali Linux?
apt_cache = apt.Cache()

linux_distro = platform.linux_distribution()

if 'Kali' in linux_distro:
    isKali = True

else:
    isKali = False


# Function to check for installation of a few dependencies
def check_deps():

    needed = 0

    # `Kali` Linux Dependencies

    if isKali:

        apt_cache.open()

        # if os.path.isdir('/usr/share/fonts-font-awesome/') == True: [ Another way ]
        if apt_cache["fonts-font-awesome"].is_installed == True:

            print("\t[+] Font-Awesome        [INSTALLED]")
            time.sleep(1)
            print("\t[+] Looking good, continuing")
            time.sleep(1)

        else:

            print("\t[+] Font-Awesome        [NOT INSTALLED]")
            time.sleep(1)
            print("\t[-] Installing Font-Awesome [ 'apt-get install fonts-font-awesome' ]")
            os.system('apt-get update && apt-get install fonts-font-awesome')

            print("\t[-] Rebuilding Font Cache [ 'fc-cache -f']")
            os.system('fc-cache -f')

            needed += 1

        if apt_cache["python3-dialog"].is_installed == True:

            print("\t[+] pythondialog        [INSTALLED]")
            time.sleep(1)
            print("\t[+] Looking good, continuing")
            time.sleep(1)

        else:

            print("\t[+] pythondialog        [NOT INSTALLED]")
            time.sleep(1)
            print("\t[-] Installing pythondialog [ 'apt-get install python3-dialog' ]")
            os.system('apt-get update && apt-get install python3-dialog')

            print("\t[-] Rebuilding Font Cache [ 'fc-cache -f']")
            os.system('fc-cache -f')

            needed += 1

        if needed > 0:
            os.system('./TSK.py')
            sys.exit()

        else:

            os.system('clear')


def help_me_rhonda():

    if isKali:

        os.system('gnome-terminal -- less README.md');

    else:

        os.system('gnome-terminal -x less README.md');


def get_line(lines, index, justification=49):

    """
    Helper method for print_menu_technicolorama.
    Returns the line from `lines` at index `index`, or an empty string if no line exists
    Args:
        lines (list[str]): List of strings
        index (int): Zero-based index of an element in `lines`
        justification (int): Optional. How many characters to justify the text (space-padding)
    """

    if index < len(lines):

        return lines[index].ljust(justification)

    else:

        return "".ljust(justification)

################################################################
# // Right-side box message(s) when Main Menu is displayed // #
main_menu_lines = [
        '',
        FG + '     A framework for the creation and           ',
        '',
        FG + '      deployment of USB/HID based attacks        ',
        '',
        '',
        '',
        '',
        FG + '     A project by sandmansandito & derv82       ',
        '',
        FG + '      Dreamed up under the wet hot neon lights   ',
        '',
        FG + '      of the Las Vegas Strip                     ',
        '',
        '',
        '',
        '',
        FG + '     Select a menu option on the left to        ',
        '',
        FG + '       view payloads for that device.            ',
        '',
        '',
        '',
        FG + '     Please see the README file or HELP Menu    ',
        FG + '      for more information on using TSK          ',
        '',
        '',
        '',
        FLW + '    v1.0 [ The Patriotic Penguin Edition  ]     '
    ]

# // Right-side box message(s) when USB Rubber Ducky Menu is displayed // #
ducky_menu_lines = [
        '',
        FW + '     ' + BY + 'USB Rubber Ducky Payloads Menu' + BRST + '             ',
        '',
        FY + '      Choose a number below for more options     ',
        '',
        FY + '      Please see README for detailed usage       ',
        '',
        '',
        FW + '   1. ' + BY + 'HAK5 Rubber Ducky Payload Collection' + BRST + '       ',
        '',
        FY + '      Select from a list of payloads to edit     ',
        '',
        FY + '      and optionally flash to the ducky          ',
        '',
        '',
        FW + '   2. ' + BY + 'Install simple-ducky payload generator' + BRST + '     ',
        '',
        FY + '      Install the latest version of simple-ducky ',
        '',
        FY + '      for generating ducky payloads & listeners  ',
        '',
        FW + '   3. ' + BY + 'Encoders | Decoders | Firmwares | Payloads' + BRST + ' ',
        '',
        FY + '      Select from various encoders, decoders,    ',
        FY + '      firmwares and other miscellaneous useful   ',
        '',
        FY + '      payloads for the USB rubber ducky          ',
        '',
        FLBL + '  <<< [P]REV       ' + FW + 'Menu 1 / 1' + FLBL +'        [N]EXT >>>  '
    ]

# // Right-side box message(s) when USB menu is displayed // #
USB_menu_lines = [
        '',
        FW + '     ' + BB + 'USB Flash Drive Dropper Menu' + BRST + '               ',
        '',
        FBL + '      Choose a number below for more options     ',
        '',
        FBL + '      Please see README for detailed usage       ',
        '',
        '',
        FW + '   1. ' + BB + 'Extract dropper files to a location' + BRST + '        ',
        '',
        FBL + '      Copies templated dropper files to a        ',
        '',
        FBL + '      USB drive or specific location             ',
        '',
        '',
        FW + '   2. ' + BB + 'Extract snarfer files to a location' + BRST + '        ',
        '',
        FLB + '      Copies snarf parser & editable config      ',
        '',
        FLB + '      file to a USB drive or specific location   ',
        '',
        FW + '   3. ' + BB + 'Configure a \'BadUSB\' type USB Drive' + BRST + '        ',
        '',
        FLB + '      Copies BadUSB Python implementation for    ',
        FLB + '      Phison 2303 to a specific location         ',
        '',
        '',
        '',
        FLBL + '  <<< [P]REV       ' + FW + 'Menu 1 / 1' + FLBL +'        [N]EXT >>>  '
    ]

# // Right-side box message(s) when Teensy menu is displayed // #
teensy_menu_lines = [
        '',
        FW + '     ' + BM + 'Teensy HID Payloads Menu' + BRST + '                   ',
        '',
        FM + '      Choose an option below for more info       ',
        '',
        '',
        '',
        '',
        FW + '   1. ' + BB + 'Extract dropper files to a USB drive' + BRST + '       ',
        '',
        FLB + '      Copies templated dropper files to a        ',
        '',
        FLB + '      drive or location of your choice           ',
        '',
        '',
        '',
        '',
        FG + '     Select a menu option on the left to        ',
        '',
        FG + '       view payloads for that device.            ',
        '',
        '',
        '',
        FG + '     Please see the README file or HELP Menu    ',
        FG + '      for more information on using TSK          ',
        '',
        '',
        '',
        FLW + '    v1.0 [ The Patriotic Penguin Edition  ]     '
    ]

# END               Right-side box message(s)               END #
#################################################################

# Print Main/About Menu
def print_menu_technicolorama(right_menu_lines = main_menu_lines):

    """
    Prints the Main/About menu which are one in the same.
    The colors are defined from colorama and given custom shortcuts to cut down on the amount of bloat.
    This should also make it easier to change color/style combinations for future updates.

    Args:
        right_menu_lines (list[str]): List of strings to print in the right-side menu box.
                                      Each line should not exceed 49 characters
                                      Optional. Default is the main menu.
    """
    print('\n\n')
    print('\t' + FR + SB + 'TTTTTTTTTTTTTTTTTTTTTTT   SSSSSSSSSSSSSSS KKKKKKKKK    KKKKKKK' + '      ' + BLB + '                                                     ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::T SS:::::::::::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 0) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::TS:::::SSSSSS::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 1) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::TT:::::::TT:::::TS:::::S     SSSSSSSK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 2) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'TTTTTT  T:::::T  TTTTTTS:::::S            KK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 3) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T        S:::::S              K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + get_line(right_menu_lines, 4) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T         S::::SSSS           K::::::K:::::K' + '          ' + BLB + '  ' + BRST + get_line(right_menu_lines, 5) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T          SS::::::SSSSS      K:::::::::::K' + '           ' + BLB + '  ' + BRST + get_line(right_menu_lines, 6) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T            SSS::::::::SS    K:::::::::::K' + '           ' + BLB + '  ' + BRST + get_line(right_menu_lines, 7) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T               SSSSSS::::S   K::::::K:::::K' + '          ' + BLB + '  ' + BRST + get_line(right_menu_lines, 8) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T' + FW +'        [v1.0]' + FR +'      S:::::S  K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + get_line(right_menu_lines, 9) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T                    S:::::SKK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 10) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      TT:::::::TT      SSSSSSS     S:::::SK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 11) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      T:::::::::T      S::::::SSSSSS:::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 12) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      T:::::::::T      S:::::::::::::::SS K:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 13) + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      TTTTTTTTTTT       SSSSSSSSSSSSSSS   KKKKKKKKK    KKKKKKK' + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 14) + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + get_line(right_menu_lines, 15) + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + get_line(right_menu_lines, 16) + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SB + '                 THE                  SKELETON                  KEY' + '         ' + SB + BLB + '  ' + BRST + get_line(right_menu_lines, 17) + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + get_line(right_menu_lines, 18) + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '                                                                            ' + BLB + '  ' + SB + BRST + get_line(right_menu_lines, 19) + BLB + '  ' + BRST + FRST+ SRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 20) + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'T' + BRST + '  [' + FG + SB + 'H' + FW + ']elp  ' + FW + BR + '             Help Me, Rhonda               ' + BRST + ' ' + FW + BLB + 'T' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 21) + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'S' + BRST + '  [' + FG + SB + 'A' + FW + ']bout ' + FB + BW + '             Check It Out!!!               ' + BRST + ' ' + FW + BLB + 'S' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 22) + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'K' + BRST + '  [' + FG + SB + 'Q' + FW + ']uit  ' + FW + BB + '             Blow This Joint               ' + BRST + ' ' + FW + BLB + 'K' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 23) + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'M' + BRST + '  [' + FG + SB + 'R' + FW + ']ubber Ducky  ' + FY + '     You\'''re The One                 ' + FW + BLB + 'M' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 24) + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'E' + BRST + '  [' + FG + SB + 'B' + FW + ']ash Bunny  ' + FW + '       Payload Puritania              ' + FW + BLB + 'E' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 25) + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '\t      ' + FW + BLB + 'N' + BRST + '  [' + FG + SB + 'T' + FW + ']eensy' + FM + '             Teensy HID Attacks             ' + FW + BLB + 'N' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 26) + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '\t      ' + FW + BLB + 'U' + BRST + '  [' + FG + SB + 'U' + FW + ']SB' + FLB + '                USB Related Deployments        ' + FW + BLB + 'U' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 27) + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '                                                                            ' + BLB + '  ' + BRST + SRST + get_line(right_menu_lines, 28) + BLB + SB + '  ' + BRST + FRST + SRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '                                                     ' + BRST + Style.RESET_ALL)

def ducky_menu(right_menu_lines = ducky_menu_lines):

    os.system('clear')

    print_menu_technicolorama(right_menu_lines)

    ducky_menuLoop = True

    while ducky_menuLoop == True:

        ducky_choice = input("\n\t      Enter your Ducky selection : ")

        if ducky_choice == 'R' or ducky_choice == 'r':
            print("\t      " + SB + BR + "ALREADY HERE!" + BRST)
            time.sleep(2)
            ducky_menu()

        elif ducky_choice == 'B' or ducky_choice == 'b':
            bunny_menu()

        elif ducky_choice == 'T' or ducky_choice == 't':
            teensy_menu()

        elif ducky_choice == 'U' or ducky_choice == 'u':
            USB_menu()

        elif ducky_choice == 'H' or ducky_choice == 'h':
            help_me_rhonda()
            ducky_menu(right_menu_lines = ducky_menu_lines)
            continue

        elif ducky_choice == 'A' or ducky_choice == 'a':
            main_menu()

        elif ducky_choice == 'Q' or ducky_choice == 'q':
            print("\n\t      Thank you for checking out TSK! [ HACK THE PLANET!!! ]\n")
            sys.exit()

        else:
            input("\n\t      No such option " + "\'" + ducky_choice + "\'" + " exists." + " Press ENTER key to try again.")
            ducky_menu(right_menu_lines = ducky_menu_lines)

def teensy_menu(right_menu_lines = teensy_menu_lines):

    os.system('clear')

    print_menu_technicolorama(right_menu_lines)

    teensy_menuLoop = True

    while teensy_menuLoop == True:

        teensy_choice = input("\n\t      Enter your USB selection : ")

        if teensy_choice == 'R' or teensy_choice == 'r':
            ducky_menu()

        elif teensy_choice == 'B' or teensy_choice == 'b':
            bunny_menu()

        elif teensy_choice == 'T' or teensy_choice == 't':
            print("\t      " + SB + BR + "ALREADY HERE!" + BRST)
            time.sleep(2)
            teensy_menu()

        elif teensy_choice == 'U' or teensy_choice == 'u':
            USB_menu()

        elif teensy_choice == 'H' or teensy_choice == 'h':
            help_me_rhonda()
            teensy_menu(right_menu_lines = teensy_menu_lines)
            continue

        elif teensy_choice == 'A' or teensy_choice == 'a':
            main_menu()

        elif teensy_choice == 'Q' or teensy_choice == 'q':
            print("\n\t      Thank you for checking out TSK! [ HACK THE PLANET!!! ]\n")
            sys.exit()

        else:
            input("\n\t      No such option " + "\'" + teensy_choice + "\'" + " exists." + " Press ENTER key to try again.")
            teensy_menu(right_menu_lines = teensy_menu_lines)


def USB_menu(right_menu_lines = USB_menu_lines):

    os.system('clear')

    print_menu_technicolorama(right_menu_lines)

    USB_menuLoop = True

    while USB_menuLoop == True:

        USB_choice = input("\n\t      Enter your USB selection : ")

        if USB_choice == 'R' or USB_choice == 'r':
            ducky_menu()

        elif USB_choice == 'B' or USB_choice == 'b':
            bunny_menu()

        elif USB_choice == 'T' or USB_choice == 't':
            teensy_menu()

        elif USB_choice == 'U' or USB_choice == 'u':
            USB_menu()

        elif USB_choice == 'H' or USB_choice == 'h':
            help_me_rhonda()
            USB_menu(right_menu_lines = USB_menu_lines)
            continue

        elif USB_choice == 'A' or USB_choice == 'a':
            main_menu()

        elif USB_choice == 'Q' or USB_choice == 'q':
            print("\n\t      Thank you for checking out TSK! [ HACK THE PLANET!!! ]\n")
            sys.exit()

        else:
            input("\n\t      No such option " + "\'" + USB_choice + "\'" + " exists." + " Press ENTER key to try again.")
            USB_menu(right_menu_lines = USB_menu_lines)


def main_menu():

    os.system('clear')

    print_menu_technicolorama(right_menu_lines = main_menu_lines)

    # While loop for asking for menu input. The choices here are obvious and display appropriate menu selection
    while menuLoop == True:

        try:

            choice = input("\n\t      Enter your selection : ")

            if choice == 'R' or choice == 'r':
                ducky_menu()

            elif choice == 'B' or choice == 'b':
                bunny_menu()

            elif choice == 'T' or choice == 't':
                teensy_menu()

            elif choice == 'U' or choice == 'u':
                USB_menu()

            elif choice == 'H' or choice == 'h':
                help_me_rhonda()
                print_menu_technicolorama(right_menu_lines = main_menu_lines)
                continue

            elif choice == 'A' or choice == 'a':
                main_menu()

            elif choice == 'Q' or choice == 'q':
                print("\n\t      Thank you for checking out TSK! [ HACK THE PLANET!!! ]\n")
                sys.exit()

            else:
                input("\n\t      No such option " + "\'" + choice + "\'" + " exists." + " Press ENTER key to try again.")
                print_menu_technicolorama(right_menu_lines = main_menu_lines)

        except KeyboardInterrupt:
            print("\n\n\t      Exiting in a HURRY!\n")
            sys.exit(0)



if os.getuid() == 0:

    # On startup, set the menuLoop variable for menu choices, check dependencies and print the main menu
    os.system('clear')

    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=140))

    menuLoop = True; check_deps(); main_menu();

else:

    exit("If you liked it then you should have run it as admin!")

init()
