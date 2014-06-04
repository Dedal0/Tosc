#!/usr/bin/python

import fileinput
import os.path
import commands
import time

def buscartorrc():
	if (os.path.isfile("/usr/local/etc/tor/torrc")):
		ruta = "/usr/local/etc/tor/torrc"
		return ruta
	elif (os.path.isfile("/etc/tor/torrc")):
		ruta = "/etc/tor/torrc"
		return ruta
	elif (os.path.isfile("/etc/torrc")):
		ruta = "/etc/torrc"
		return ruta
	else:
		ruta = raw_input("give us torrc dir: ")
		return ruta

def onion():
	r = buscartorrc()
	for line in fileinput.FileInput(r, inplace=1):
		line=line.replace("#HiddenServiceDir /var/lib/tor/hidden_service/","HiddenServiceDir /var/www/tor/")
		line=line.replace("#HiddenServicePort 80 127.0.0.1:80","HiddenServicePort 80 127.0.0.1:80")
		print line
	
	commands.getoutput("mkdir /var/www/tor")
	print "Creating Directory..."
	time.sleep(3)
	commands.getoutput("chown debian-tor /var/www/tor")
	print "Chowning..."
	time.sleep(3)
	commands.getoutput("service tor restart")
	print "Restarting Tor..."	
	time.sleep(5)
	myonion = commands.getoutput("cat /var/www/tor/hostname")
	print "Your onion Url: " + myonion

onion()
