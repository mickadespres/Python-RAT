# Python-Remote Access Tool

This Remote Access Tool (RAT) was written and tested in python 2.7 on Linux Based System. (Ubuntu 16.04 LTS and Kali linux 2.0)

The aim of this project was entirely educational during my cyber security studies.

https://github.com/mickadespres/Python-RAT.git

## Features

* Run commands on the target system (cp, mkdir, touch, rm, shutdown, reboot, ...)
* Get log file of the standard output stream of the target system
* Download files from the target system (text files only)
* Upload files on the target system (text files only)
* Error recognition during socket creation

### Directions

1. You need to specify an available port on the target system which will allow to bind the host/port parameters to the server socket.
2. After that, you will be prompted to choose an attack option
3. checks for uploading and downloading files. The files need to be in current working directory.


### Requirements

* Tested with root privileges
* A linux target system
* A linux client system
* The both systems need to be on the same local network

### Improvements 

* Loop to perform several attacks in same session
* 4th attack : Keylogger

### I really appreciate all kinds of feedback. Thanks for using and testing this tool.
