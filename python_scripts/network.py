#!/usr/bin/python3
import netifaces
import sys

def getInfo(interface):
	ret = ''
	ipAddress=''
	macAddress=''
	for iface in netifaces.interfaces():
		try:
			iface_data=netifaces.ifaddresses(iface)
			if(iface==interface):
				for family in iface_data:
					for address in iface_data[family]:
						if(family == netifaces.AF_INET):
							ipAddress = str(address['addr'])
						elif(family == netifaces.AF_LINK):
							macAddress = str(address['addr'])
		except ValueError:
			pass
	ret +=macAddress
	if(len(ipAddress)>10):
		ret += " @ "+ipAddress
	return ret

def colorIface(iface,name):
	ret = ""
	color="'white'"
	colorDC="'red'"
	if(name=="eth0"):
			color="'lime'"
			colorDC="'orange'"
	elif(name=="wlan0"):
			color="'aqua'"
			colorDC="'teal'"
	if(len(iface)>30):
		ret = "<span color="+color+"><span font='FontAwesome'>"+iface+"</span></span>"
	else:
		ret = "<span color="+colorDC+"><span font='FontAwesome'>"+iface+" DC</span></span>"
	return ret

def run():
	displayMsg=str(colorIface(getInfo(str(sys.argv[1])),str(sys.argv[1])))
	print(displayMsg)

run()
