#!/usr/bin/python3
import netifaces
import sys

def getTunnel():
	ret='DC'
	for iface in netifaces.interfaces():
		iface_data=netifaces.ifaddresses(iface)
		if(iface=='tun0'):
			for family in iface_data:
				for address in iface_data[family]:
					if(family==netifaces.AF_INET):
						ret=str(address['addr'])
	return ret

def color():
	color="'olive'"
	output='DC'
	tunnel=getTunnel()
	if(len(tunnel)>2):
		color="'lime'"
		output="<span color="+color+"><span font='FontAwesome'>"+tunnel+"</span></span>"
	else:
		output="<span color="+color+"><span font='FontAwesome'>VPN Disabled</span></span>"
	return output

print(color())
