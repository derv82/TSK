#!/usr/bin/env python
# coding=utf-8

# The Skeleton Key v.the first [ 9-11-2017 ]
# Codename - The Patriotic Penguin Edition
#
# A project by sandmansandito and derv82
#
# This is a very experimental first version
# Hopefully it should improve over time

from colorama import init, Fore, Back, Style
import os

os.system('clear')
init()

# Set variable shotcuts for colorama colors
FR = Fore.RED; FW = Fore.WHITE; FG = Fore.GREEN; FB = Fore.BLACK; FY = Fore.YELLOW; FM = Fore.MAGENTA; FLB = Fore.LIGHTBLUE_EX
BLB = Back.LIGHTBLACK_EX;  BR = Back.RED; BW = Back.WHITE; BB = Back.BLUE
SB = Style.BRIGHT; SD = Style.DIM; SN = Style.NORMAL; BRST = Back.RESET

def print_menu_technicolorama():
    print('\n\n')
    print('\t' + FR + SB + 'TTTTTTTTTTTTTTTTTTTTTTT   SSSSSSSSSSSSSSS KKKKKKKKK    KKKKKKK' + '      ' + BLB + '                                                     ' + BRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::T SS:::::::::::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + 'T:::::::::::::::::::::TS:::::SSSSSS::::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + FG + '   🔑  A framework for the creation and           ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + 'T:::::TT:::::::TT:::::TS:::::S     SSSSSSSK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + 'TTTTTT  T:::::T  TTTTTTS:::::S            KK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + FG + '      deployment of USB/HID based attacks        ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T        S:::::S              K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T         S::::SSSS           K::::::K:::::K' + '          ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T          SS::::::SSSSS      K:::::::::::K' + '           ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T            SSS::::::::SS    K:::::::::::K' + '           ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T               SSSSSS::::S   K::::::K:::::K' + '          ' + BLB + '  ' + BRST + FG + '   💾  A project by sandmansandito & derv82       ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T' + FW +'        [v1.0]' + FR +'      S:::::S  K:::::K K:::::K' + '         ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '        T:::::T                    S:::::SKK::::::K  K:::::KKK' + '      ' + BLB + '  ' + BRST + FG + '      Dreamed up under the wet hot neon lights   ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '      TT:::::::TT      SSSSSSS     S:::::SK:::::::K   K::::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '      T:::::::::T      S::::::SSSSSS:::::SK:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + FG + '      of the Las Vegas Strip                     ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '      T:::::::::T      S:::::::::::::::SS K:::::::K    K:::::K' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t' + FR + SB + '      TTTTTTTTTTT       SSSSSSSSSSSSSSS   KKKKKKKKK    KKKKKKK' + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print(FW + SB + '                 THE                  SKELETON                  KEY' + '         ' + SB + BLB + '  ' + BRST + FG + '   📃  Select a menu option on the left to        ' + BLB + '  ' + BRST)
    print(FW + SD + '              ========================================================' + '      ' + SB + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('                                                                            ' + BLB + '  ' + BRST + FG + '       view payloads for that device.            ' + BLB + '  ' + BRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'T' + BRST + '  [' + FG + SB + 'H' + FW + ']elp  ' + FW + BR + '             Help Me, Rhonda               ' + BRST + ' ' + FW + BLB + 'T' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'S' + BRST + '  [' + FG + SB + 'A' + FW + ']bout ' + FB + BW + '             Check It Out!!!               ' + BRST + ' ' + FW + BLB + 'S' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'K' + BRST + '  [' + FG + SB + 'Q' + FW + ']uit  ' + FW + BB + '             Blow This Joint               ' + BRST + ' ' + FW + BLB + 'K' + BRST + '      ' + BLB + '  ' + BRST + FG + '   📖  Please see the README file or HELP Menu    ' + BLB + '  ' + BRST)
    print('                                                                            ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'M' + BRST + '  [' + FG + SB + 'R' + FW + ']ubber Ducky  ' + FY + '     You\'''re The One                 ' + FW + BLB + 'M' + BRST + '      ' + BLB + '  ' + BRST + FG + '      for more information on using TSK          ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'E' + BRST + '  [' + FG + SB + 'B' + FW + ']ash Bunny  ' + FW + '       Payload Puritania              ' + FW + BLB + 'E' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'N' + BRST + '  [' + FG + SB + 'T' + FW + ']eensy' + FM + '             Teensy HID Attacks             ' + FW + BLB + 'N' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('\t      ' + FW + BLB + 'U' + BRST + '  [' + FG + SB + 'U' + FW + ']SB' + FLB + '                USB Flash Drive Dropper        ' + FW + BLB + 'U' + BRST + '      ' + BLB + '  ' + BRST + '                                                 ' + BLB + '  ' + BRST)
    print('                                                                            ' + BLB + '  ' + BRST + SD + '    v1.0 [ The Patriotic Penguin Edition 🐧 ]     ' + BLB + SB + '  ' + BRST)
    print('\t' + FW + SB + '      ' + BLB + '*' + '                                                     ' + ' ' + BLB + FW + SB + '*' + BRST + '      ' + BLB + '                                                     ' + BRST + Style.RESET_ALL)

print_menu_technicolorama()
