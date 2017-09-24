#!/usr/bin/python3
# coding=utf-8

# The Skeleton Key v.the first [ 9-11-2017 ]
# Codename - The Patriotic Penguin Edition
#
# A project by sandmansandito and derv82
#
# This is a very experimental first version
# Hopefully it should improve over time

import os
import apt
import sys
import platform
from colorama import init, Fore, Back, Style
from future.builtins import input

os.system('reset')
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=140))

init()

# Set variable shotcuts for colorama colors
FR = Fore.RED; FW = Fore.WHITE; FG = Fore.GREEN; FB = Fore.BLACK; FY = Fore.YELLOW; FM = Fore.MAGENTA; FLB = Fore.LIGHTBLUE_EX
BLB = Back.LIGHTBLACK_EX;  BR = Back.RED; BW = Back.WHITE; BB = Back.BLUE
SRST = Style.RESET_ALL; SB = Style.BRIGHT; SD = Style.DIM; SN = Style.NORMAL; BRST = Back.RESET; FRST = Fore.RESET

system = platform.dist()
print(system)
    # Print Main/About Menu
def print_menu_technicolorama():
    """
    Prints the Main/About menu which are one in the same.
    The colors are defined from colorama and given custom shortcuts to cut down on the amount of bloat.
    This should also make it easier to change color/style combinations for future updates.

    """
    print('\n\n')
    print('\t' + FR + SB + 'TTTTTTTTTTTTTTTTTTTTTTT   SSSSSSSSSSSSSSS KKKKKKKKK    KKKKKKK' + '      ' + BLB + '                                                     ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::T SS:::::::::::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::TS:::::SSSSSS::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + FG + '     A framework for the creation and           ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'T:::::TT:::::::TT:::::TS:::::S     SSSSSSSK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + 'TTTTTT  T:::::T  TTTTTTS:::::S            KK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + FG + '      deployment of USB/HID based attacks        ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T        S:::::S              K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T         S::::SSSS           K::::::K:::::K' + '          ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T          SS::::::SSSSS      K:::::::::::K' + '           ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T            SSS::::::::SS    K:::::::::::K' + '           ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T               SSSSSS::::S   K::::::K:::::K' + '          ' + BLB + '  ' + BRST + FG + '     A project by sandmansandito & derv82       ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T' + FW +'        [v1.0]' + FR +'      S:::::S  K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '        T:::::T                    S:::::SKK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + FG + '      Dreamed up under the wet hot neon lights   ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      TT:::::::TT      SSSSSSS     S:::::SK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      T:::::::::T      S::::::SSSSSS:::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + FG + '      of the Las Vegas Strip                     ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      T:::::::::T      S:::::::::::::::SS K:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t' + FR + SB + '      TTTTTTTTTTT       SSSSSSSSSSSSSSS   KKKKKKKKK    KKKKKKK' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SB + '                 THE                  SKELETON                  KEY' + '         ' + SB + BLB + '  ' + BRST + FG + '     Select a menu option on the left to        ' + BLB + '  ' + BRST + FRST + SRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '                                                                            ' + BLB + '  ' + SB + BRST + FG + '       view payloads for that device.            ' + BLB + '  ' + BRST + FRST+ SRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'T' + BRST + '  [' + FG + SB + 'H' + FW + ']elp  ' + FW + BR + '             Help Me, Rhonda               ' + BRST + ' ' + FW + BLB + 'T' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'S' + BRST + '  [' + FG + SB + 'A' + FW + ']bout ' + FB + BW + '             Check It Out!!!               ' + BRST + ' ' + FW + BLB + 'S' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'K' + BRST + '  [' + FG + SB + 'Q' + FW + ']uit  ' + FW + BB + '             Blow This Joint               ' + BRST + ' ' + FW + BLB + 'K' + BRST + '      ' + BLB + '  ' + BRST + FG + '     Please see the README file or HELP Menu    ' + BLB + '  ' + BRST + FRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'M' + BRST + '  [' + FG + SB + 'R' + FW + ']ubber Ducky  ' + FY + '     You\'''re The One                 ' + FW + BLB + 'M' + BRST + '      ' + BLB + '  ' + BRST + FG + '      for more information on using TSK          ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'E' + BRST + '  [' + FG + SB + 'B' + FW + ']ash Bunny  ' + FW + '       Payload Puritania              ' + FW + BLB + 'E' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST + SRST)
    print('\t      ' + FW + BLB + 'N' + BRST + '  [' + FG + SB + 'T' + FW + ']eensy' + FM + '             Teensy HID Attacks             ' + FW + BLB + 'N' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'U' + BRST + '  [' + FG + SB + 'U' + FW + ']SB' + FLB + '                USB Flash Drive Dropper        ' + FW + BLB + 'U' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '                                                                            ' + BLB + '  ' + BRST + SRST + SD + '    v1.0 [ The Patriotic Penguin Edition  ]     ' + BLB + SB + '  ' + BRST + FRST + SRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '                                                     ' + BRST + Style.RESET_ALL)


def check_deps():

    needed = 0

    apt_cache = apt.Cache()

    linux_distro = platform.linux_distribution()

    # Kali Linux Dependencies

    if 'Kali' in linux_distro:
        apt_cache.open()

        # if os.path.isdir('/usr/share/fonts-font-awesome/') == True: [ Another way ]
        if apt_cache["fonts-font-awesome"].is_installed == True:

            print("\t[+] Font-Awesome        [INSTALLED]")

        else:

            print("\t[+] Font-Awesome        [NOT INSTALLED]")

            print("\t[-] Installing Font-Awesome [ 'apt-get install fonts-font-awesome' ]")
            os.system('apt-get update && apt-get install fonts-font-awesome')

            print("\t[-] Rebuilding Font Cache [ 'fc-cache -f']")
            os.system('fc-cache -f')

            needed += 1

        if needed > 0:
            os.system('./TSK.py')
            sys.exit()

        else:

            os.system('reset')

menuLoop = True

while menuLoop == True:

    try:

        check_deps()
        print_menu_technicolorama()

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

            os.system('xdg-open README.md')
            continue

        elif choice == 'A' or choice == 'a':
            print_menu_technicolorama()

        elif choice == 'Q' or choice == 'q':
            print("\n\t      Thank you for checking out TSK! [ HACK THE PLANET!!! ]\n")
            menuLoop = False

        else:

            input("\n\t      No such option " + "\'" + choice + "\'" + " exists." + " Press ENTER key to try again.")

    except KeyboardInterrupt:
        print("\n\n\t      Exiting in a HURRY!\n")
        sys.exit(0)
