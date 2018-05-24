# Python-Remote Access Tool

This Remote Access Tool (RAT) was written and tested in python 2.7 on Linux Based System. (Ubuntu 16.04 LTS and Kali linux 2.0)

The aim of this project was entirely educational during my cyber security studies.

https://github.com/mickadespres/Python-RAT.git

## Features

* Run commands on the target system (cp, mkdir, touch, rm, shutdown, reboot, ...)
* Get log file of the standard output stream of the target system
* Download files from the target system (text files only) (with overwriting checks)
* Upload files on the target system (text files only) (with overwriting checks)
* Error recognition during socket creation
* File detection during transfers
* (4th attack : Keylogger for linux systems)

### Directions

1. You need to specify an available port on the target system which will allow to bind the host/port parameters to the server socket.
2. After that, you will be prompted to choose an attack option
3. Checks for uploading and downloading files. The files need to be in current working directory of the scripts.

  #### Example
  * Run the server script on target system, then run the client script on your system.
  * Specify parameters to connect on target system (IP Address & available port) and choose the 3rd attack in the panel menu
  * Just specify the filename of the keylogger located in the same current working directory of the script, to upload on the target system, press "enter"
  * After that, specify the filename of the library located in the same current working directory of the script, to upload on the target system, then press "enter"
  * Choose 1st attack to run keylogger.py "python keylogger.py" 
  * Wait for key events of the victim...
  * Reload the scripts and choose 1st attack to locate and copy file.log  into current working directory of the server script
  * then, download the script with 2nd attack, specify "file.log" on filename input request.
  
### Requirements

* A linux target system
* A linux client system
* The both systems need to be on the same local network


### Improvements 

* fix loop to perform several attacks in same session
* File detection to upload and download some files away from cwd of the scripts.
* 4th attack : Keylogger

### I really appreciate all kinds of feedback. Thanks for using and testing this tool.
