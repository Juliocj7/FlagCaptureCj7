#!/usr/bin/env -S author=JulioCj7 python3
#-*- coding: utf-8 -*-

"""
:  ¡CaptureThe𝙵𝚕𝚊𝚐!   
"""
###  [+591 79424937]( https://github.com/${author} )


import os
import sys
import time
import random
from datetime import datetime

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

COLOR_PRIMARY   = "\033[1;38;5;155m"
COLOR_SECONDARY = "\033[38;5;245m"
COLOR_HIGHLIGHT = "\033[38;5;252m"
COLOR_HIDDEN    = "\033[38;5;239m"
COLOR_ERROR     = "\033[38;5;196m"
COLOR_RESET     = "\033[0m"

CURSOR_ON       = "\033[?25h"
CURSOR_OFF      = "\033[?25l"

banner = [
    f'''
                         +---+
                         |   |
                             |
                             |
                             |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                             |
                             |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                         {COLOR_PRIMARY}| {COLOR_SECONDARY}  |
                             |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                        {COLOR_PRIMARY}/| {COLOR_SECONDARY}  |
                             |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                        {COLOR_PRIMARY}/|\\ {COLOR_SECONDARY} |
                             |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                        {COLOR_PRIMARY}/|\\ {COLOR_SECONDARY} |
                        {COLOR_PRIMARY}/ {COLOR_SECONDARY}   |
                             |
                      =========''',
    f'''
                         +---+
                         |   |
                         {COLOR_PRIMARY}O {COLOR_SECONDARY}  |
                        {COLOR_PRIMARY}/|\\ {COLOR_SECONDARY} |
                        {COLOR_PRIMARY}/ \\ {COLOR_SECONDARY} |
                             |
                      ========='''
]

def main():
    palabraAdivinar = random.choice(
        'backdoor exploit rootkit keylogger firewall honeypot malware ransomware spyware trojan virus worm brute-force hash cracking cipher encryption payload phishing sniffing spoofing mitm botnet pentest privilege escalation zero-day shellcode forensics darknet osint recon enumeration metasploit nmap hydra sqlmap burpsuite aircrack-ng kali-linux debian ubuntu arch-linux bash terminal shell sudo chmod chown root user apk sideload adb fastboot bootloader selinux kernel initrd recovery ramdisk logcat dmesg syslog iptables ssh vpn tor proxy dns ddos ip mac-address tcp udp port scan engineering'.split(' ')
    )

    listaPalabraAdiv = list(palabraAdivinar)
    listaPalabraMost = [f'{COLOR_SECONDARY}_' for _ in listaPalabraAdiv]
    intentos = 7
    vidas = 0
    run = True

    while run:
        try:
            os.system('clear')
            print(f'\n{CURSOR_OFF}\033[38;5;234m\033[38;5;232;48;5;234m Programa            {COLOR_PRIMARY}El ahorcado             \033[38;5;232mJulioCj7 \033[0m\033[38;5;234m{COLOR_RESET}\n')
            format = datetime.now().strftime(f'{COLOR_SECONDARY} fecha: %d|%m|%Y                   󱎫 hora: %H:%M:%S')
            print("", format, "")
            print(f'\n{COLOR_SECONDARY} 󱐮 te quedan{COLOR_HIGHLIGHT} {intentos} {COLOR_SECONDARY}intentos\n')
            print(banner[vidas])
            print(f'\n\n{COLOR_PRIMARY} 󰭆 {COLOR_SECONDARY}' + ' '.join(listaPalabraMost))
            letra = input(f'\n{COLOR_PRIMARY} 󱚟 {COLOR_SECONDARY}letra :{COLOR_HIGHLIGHT} ')
            fallo = False

            """ !important: this is for women
            if letra and letra[0] not in listaPalabraAdiv:
                fallo = True
                intentos -= 1
                vidas += 1

            else:
                for key, value in enumerate(listaPalabraAdiv):
                    if value == letra:
                        listaPalabraMost[key] = value
            """
            #""" !important: this is for men
            try:
                if letra[0] not in listaPalabraAdiv:
                    fallo = True
                    intentos -= 1
                    vidas += 1

                else:
                    for key, value in enumerate(listaPalabraAdiv):
                        if value == letra:
                            listaPalabraMost[key] = value

            except:
                print(f'\n{COLOR_HIDDEN}¡ No puede estar vacío animal !{COLOR_RESET}')
                time.sleep(1.5)
            #"""

            if intentos <= 0:
                run = False
                print(f'\n{COLOR_ERROR}¡ Perdiste !{COLOR_SECONDARY} la palabra era "{''.join(listaPalabraAdiv)}"{COLOR_RESET}{CURSOR_ON}')

            elif listaPalabraAdiv == listaPalabraMost:
                run = False
                print(f'\n{COLOR_PRIMARY}¡ Ganaste !{COLOR_SECONDARY} la palabra era "{''.join(listaPalabraAdiv)}"{COLOR_RESET}{CURSOR_ON}')

        except KeyboardInterrupt:
            slowprint(f'\n{COLOR_ERROR}¡ ctrl+c ! {COLOR_SECONDARY}programa finalizado por usuario{COLOR_RESET}{CURSOR_ON}')
            sys.exit()
        except EOFError:
            slowprint(f'\n\n{COLOR_ERROR}¡ ctrl+d ! {COLOR_SECONDARY}programa finalizado por usuario{COLOR_RESET}{CURSOR_ON}')
            sys.exit()
        except Exception as er:
            exit(f'\n{COLOR_ERROR}¡ error ! {COLOR_SECONDARY}' + str(er) + f'{COLOR_RESET}{CURSOR_ON}\n')

if __name__ == "__main__":
    main()


"  : ~  Created by ${JulioCj7}  ~ :  "
#        Copyright © 2025 all rights reserved        #

# vim:ft=python ts=4 sts=4 sw=4 et
