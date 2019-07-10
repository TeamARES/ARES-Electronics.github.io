##### Inspired from Attrey Bhatt Codes - https://github.com/attreyabhatt/Reverse-Shell ###########

########################IMPORTING LIBRARIES #################################################
#importing socket so that we can connect two computer
import socket
#importing time
import time
#importing Serial to take data from serial port
import serial

###################### SOCKET OBJECT AND VARIABLES ###################################################
s = socket.socket()
host = '162.168.10.105'  #IP Address of the Raspberry pi
port = 9999            #Must be same as that in server.py

#In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
###########################SERIAL OBJECT ##############################################
serialPortMac = '/dev/tty.usbmodem14101' #FOR MACBOOK
serialPortWin = '/dev/ttyUSB0'           #FOR WINDOWS
serialPortUnuntu = '/dev/ttyACM1'        #FOR UBUNTU
ser = serial.Serial(serialPortMac, 9600,timeout=0.005)



while True:
    #Read data from Serial port
    serialData = str(ser.readline())
    #Data comes in format b'.........'
    if(len(serialData) > 3):
        print(serialData + "\n")          #Recieved data successfully from Serial
    
        # Sendng this data from socket to the raspberry pi
        s.send(str.encode(serialData))
    
        # After sending we check if it was recieved or not
        checkDataTranfer = s.recv(1024)
        print(checkDataTranfer)


s.close()
