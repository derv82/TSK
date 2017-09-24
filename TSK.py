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

'''Right-side box message(s) when main menu is displayed'''
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
        SD + '    v1.0 [ The Patriotic Penguin Edition  ]     '
    ]

# Print Main/About Menu
def print_menu_technicolorama(right_menu_lines=main_menu_lines):
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
    print('\t      ' + FW + BLB + 'N' + BRST + '  [' + FG + SB + 'T' + FW + ']eensy' + FM + '             Teensy HID Attacks             ' + FW + BLB + 'N' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 26) + BLB + '  ' + BRST + FRST)
    print('\t      ' + FW + BLB + 'U' + BRST + '  [' + FG + SB + 'U' + FW + ']SB' + FLB + '                USB Flash Drive Dropper        ' + FW + BLB + 'U' + BRST + '      ' + BLB + '  ' + BRST + get_line(right_menu_lines, 27) + BLB + '  ' + BRST + FRST + SRST)
    print(SB + '                                                                            ' + BLB + '  ' + BRST + SRST + get_line(right_menu_lines, 28) + BLB + SB + '  ' + BRST + FRST + SRST)
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
