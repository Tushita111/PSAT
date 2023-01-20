# -*- coding: utf-8 -*-
"""
Created on Fri Nov  25 08:42:49 2022

@author: Gsgwl
"""
import socket

UDP_IP = "127.0.0.2"
UDP_PORT = 5006
MESSAGE = ""

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
except socket.gaierror:
    print("error sending packet")
