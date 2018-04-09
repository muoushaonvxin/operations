#!/usr/bin/python3
#
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from net_tools import *
from scapy.all import *

def arp_ping(iface,pdst=None):
	import sys

	localmac = get_interface_mac(iface)
	localip = get_interface_ip(iface)['ip_address']

	result_list = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')/ARP(op=1, hwsrc=localmac, psrc=localip, hwdst='00:00:00:00:00:00', pdst=pdst), iface=iface, verbose=False)
	return result_list[0].res[0][1].getlayer(ARP).fields


a = arp_ping('eth0','192.168.0.233')
print("destination ip address is: " + a['psrc']  + "  destination mac address is: " + a['hwsrc'])
